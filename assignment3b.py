# Assignment 3b

# Prompt the user whether they would like to perform an
# aggregation (AVG, MAX, MIN, SUM) or exit the programme.

# import sqlite3
import sqlite3

# open connection
with sqlite3.connect("newnum.db") as connection:
    # get a cursor
    c = connection.cursor()

    # Ask user what they want to do
    print("""\nWhat would you like to do?

        1. Average
        2. Maximum
        3. Minimum
        4. Sum
        5. Exit\n""")

    # infinite loop until gives 1-5 as input
    while True:
        agg = input("Enter your choice: ")

        # if input is 1-4, use relevant operation on num column
        # in newnum.db to calculate the requested thing and then
        # return the result back to the user
        if agg in ["1", "2", "3", "4"]:
            operation = {1: "AVG", 2: "MAX", 3: "MIN", 4: "SUM"}\
            [int(agg)]
            c.execute("SELECT {}(num) FROM numbers"\
                .format(operation))
            result = c.fetchone()[0]
            print(result)
            break

        # if 5 given, exit the programme and show a message
        elif agg == "5":
            print("Programme terminated.")
            exit()