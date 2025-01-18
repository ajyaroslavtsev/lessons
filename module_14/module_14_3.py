# -*- coding: utf-8 -*-

from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

import config


api = config.TELEGRAM_BOT_TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard= True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.row(button1, button2)
kb.add(button3)

# Inline-клавиатура
kbi = InlineKeyboardMarkup(resize_keyboard= True)
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kbi.add(button3,button4)

inline_kb_menu = InlineKeyboardMarkup(resize_keyboard=True)
button_prod1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
button_prod2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
button_prod3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
button_prod4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')

inline_kb_menu.row(button_prod1,button_prod2,button_prod3,button_prod4)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


class UserState(StatesGroup):
    age = State()    # возраст
    growth = State() # рост
    weight = State() # вес


@dp.message_handler(text=['Рассчитать',])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kbi)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


products_img_urls = {
    'apple' : 'https://goo.su/G9v6HG',
    'lemon' : 'https://goo.su/eDwt',
    'ananas' : 'https://goo.su/60dBrr4',
    'grape' : 'https://goo.su/spMbU'
}

@dp.message_handler(text=['Купить',])
async def get_buying_list(message):
    for i,(prod_name,url) in enumerate(products_img_urls.items(), start=1):
        await message.answer(f'Название: Product {i}| Описание: описание {i} | Цена: {i * 100}')
        await bot.send_photo(message.chat.id, types.InputFile.from_url(url))
    await message.answer(f'Выберите продукт для покупки:', reply_markup=inline_kb_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')



@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
