# Homework 6.5.1

# import sqlite3, connect to cars.db and get cursor.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # Add 5 records to the inventory table (cars.db); 3 Fords
    # and 2 Hondas.
    new_stock = [('Ford', 'GT', 1), 
        ('Ford', 'Fiesta', 23),
        ('Ford', 'Focus RS', 2),
        ('Honda', 'NSX', 2),
        ('Honda', 'Jazz', 1)
        ]

    c.executemany("INSERT INTO cars VALUES (?, ?, ?)",\
        new_stock)
