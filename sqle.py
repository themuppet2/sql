# INSERT command with Error Handler

import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    # insert data (notice we have incorrectly called the table
        # populations rather than population)
    cursor.execute("INSERT INTO populations VALUES(\
        'New York City', 'NY', 820000)")
    cursor.execute("INSERT INTO populations VALUES(\
        'San Francisco', 'CA', 800000)")

    # commit the changes
    conn.commit()

except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")

# close the database connection
conn.close()