# This script imports data from a csv file to the
# database.

import csv
import sqlite3

path = "/Users/jamescollins/Documents/RealPython/\
Course two/book2-exercises-master/sql/"

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign it to a variable
    employees = csv.reader(open(path + "employees.csv", "rU"))

    # create a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT,\
        lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname)\
        VALUES (?, ?)", employees) # not sure why we need the
    # employees(firstname, lastname), rather than just employees;
    # it appears to do the same thing either way??