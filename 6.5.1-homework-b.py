# Update the quantity of two of the records, and then output all
# all the records from the table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # update quantity of the records
    c.execute("UPDATE cars SET quantity=10 WHERE model='GT'")
    c.execute("UPDATE cars SET quantity=-1 WHERE model='Jazz'")

    # output all the records
    print('\noutputting data:\n')

    c.execute("SELECT * FROM cars")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])