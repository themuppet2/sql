# Add a table to accompany "inventory" (my table is called
# "cars") called "orders" with the fields "make", "model" and
# "order date".
# Only include makes and models for cars in the cars table (i.e.
# Honda and Ford)
# Add 15 records - 3 for each car - each with a separate order
# date (YYYY-MM-DD).

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders(Make TEXT, Model TEXT, 
        Order_Date DATE)""")

    orders = [
    ('Ford', 'GT', '2016-01-23'),
    ('Ford', 'GT', '2016-03-23'),
    ('Ford', 'GT', '2016-04-07'),
    ('Ford', 'Focus RS', '2016-01-05'),
    ('Ford', 'Focus RS', '2016-01-29'),
    ('Ford', 'Focus RS', '2016-03-01'),
    ('Ford', 'Fiesta', '2016-01-05'),
    ('Ford', 'Fiesta', '2016-01-05'),
    ('Ford', 'Fiesta', '2016-01-13'),
    ('Honda', 'Jazz', '2016-01-20'),
    ('Honda', 'Jazz', '2016-03-20'),
    ('Honda', 'Jazz', '2016-04-22'),
    ('Honda', 'NSX', '2016-02-29'),
    ('Honda', 'NSX', '2016-03-30'),
    ('Honda', 'NSX', '2016-04-01')
    ]

    c.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)

    # output car details
    c.execute("""SELECT cars.make, cars.model, cars.quantity,
    orders.order_date FROM cars INNER JOIN orders ON
    cars.model=orders.model""")

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1])
        print(r[2])
        print(r[3])


