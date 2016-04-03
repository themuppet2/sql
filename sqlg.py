# SELECT statement, remove unicode characters
# Not sure if this will do anything as didn't notice
# any unicode u in output using python 3.

# However, this code does print it more neatly.

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1])