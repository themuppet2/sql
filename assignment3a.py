# Assignment 3a
# Add 100 random integers, ranging from 0 to 100, to a new
# database called newnum.db.

# import sqlite3 ans random librarys
import sqlite3
import random

# create/open newnum database
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # remove table if it already exists, then create one called
    # numbers with INT type
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num INT)")

    # Insert 100 random integers into 'num' column. The 'num'
    # column does not have to be given, but I have done so.
    for i in range(100):
        c.execute("""INSERT INTO numbers (num) VALUES(?)""",
        (random.randint(0,100),))