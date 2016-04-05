# alternative solution (using techniques from the answers)
# output only Ford cars

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM cars WHERE make='Ford'")
    rows = c.fetchall()
    print("Only printing Fords: \n")
    for r in rows:
        print(r[0], r[1], r[2])