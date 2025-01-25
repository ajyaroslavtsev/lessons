# -*- coding: utf-8 -*-

import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description  TEXT,
        price INTEGER NOT NULL,
        img_urls TEXT
    )
    ''')
    connection.commit()
    connection.close()


def _add_products():
    products_img_urls = {
        'apple': 'https://goo.su/G9v6HG',
        'lemon': 'https://goo.su/eDwt',
        'ananas': 'https://goo.su/60dBrr4',
        'grape': 'https://goo.su/spMbU'
    }
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    for i, (prod_name, url) in enumerate(products_img_urls.items(), start=1):
        cursor.execute(
            'INSERT INTO Products(title, description, price, img_urls) VALUES(?,?,?,?)',
            (f'Продукт {i}', f'Описание {i}', f'{i * 100}', f'{url}')
        )
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.close()
    return all_products


if __name__ == '__main__':
    initiate_db()
    _add_products()
    print(get_all_products())