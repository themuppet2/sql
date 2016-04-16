# Output the make and model on one line, the quantity on
# another line and the order count on the next line.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT make, model, quantity FROM cars")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], '\n', 'Stock:', r[2])

        c.execute("""SELECT count(order_date) FROM orders 
            WHERE model=?""", (r[1],))

        result = c.fetchone()[0]
        print('No. orders:', result)