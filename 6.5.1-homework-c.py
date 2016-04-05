# Output records from cars that are Ford vehicles.

############## Note: alternative (better?) solution can be
# found in 6.5.1-homework-c-2.py #########################

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM cars")
    rows = c.fetchall()
    for r in rows:
        if r[0] == 'Ford':
            print(r[0], r[1], r[2])
