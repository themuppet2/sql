'''Homework to create a database called "cars" and a table
called "inventory" that includes the following fields: "Make",
"Model", and "Quantity".'''

# import sqlite3
import sqlite3

# create database
conn = sqlite3.connect("cars.db")

# get a cursor to execute sql commands
cursor = conn.cursor()

# create table 'cars'
cursor.execute("""CREATE TABLE cars
    (Make TEXT, Model TEXT, Quantity INT)
    """)

# close the connection
conn.close()