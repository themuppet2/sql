# sqlb.py file re-written using the with command. No need to 
# commit changes when using with keyword.

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', \
        'NY', 820000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \
        'CA', 800000)")