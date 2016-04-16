import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    count = {'Count Focus RS': """SELECT count(order_date)
    FROM orders WHERE model='Focus RS'""", 
    'Count GT': """SELECT count(order_date)
    FROM orders WHERE model='GT'""", 
    'Count Fiesta': """SELECT count(order_date)
    FROM orders WHERE model='Fiesta'""", 
    'Count NSX': """SELECT count(order_date)
    FROM orders WHERE model='NSX'""", 
    'Count Jazz': """SELECT count(order_date)
    FROM orders WHERE model='Jazz'"""}



    for keys, values in count.items():
        c.execute(values)
        result = c.fetchone()
        print(keys, result[0])
