# -*- coding: utf-8 -*-

import sqlite3


__all__ = ['initiate_db', 'get_all_products', 'add_user', 'is_included']


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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT  NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.close()
    return all_products


def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username=?',(username,))
    check_user = cursor.fetchone() is not None
    connection.close()
    return check_user


def _add_test_products_and_users():
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
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',
    #         (f'Username{i}', f'user{i}@example.com', f'{i * 10}', 1000)
    #     )
    connection.commit()
    connection.close()


if __name__ == '__main__':
    # tests
    initiate_db()
    # _add_test_products_and_users()
    print(get_all_products())
    print(is_included('Usename5'))
    add_user('Usename5', 'user5@example.com', 50)
