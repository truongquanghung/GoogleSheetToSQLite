# Import required modules
import csv
import sqlite3
import time

start = time.time()
# Connecting to the database
connection = sqlite3.connect('db.sqlite3')

# Creating a cursor object to execute SQL queries on a database table
cursor = connection.cursor()

name = input()
file_name = input()

# Table Definition
try:
    create_table = f'CREATE TABLE {name}(id INTEGER PRIMARY KEY AUTOINCREMENT, '
    # Opening the .csv file
    file = open(file_name)

    # Reading the contents of the .csv file
    contents = csv.reader(file)
    row1 = next(contents)
    row_name = ""
    value = ""
    for i in range(0, len(row1)-1):
        tg = str(row1[i]).replace(' ','_')
        create_table = create_table + "'" + tg + "' TEXT ,"
        row_name = row_name + "'" + tg + "', "
        value = value + "?, "

    tg = str(row1[len(row1)-1]).replace(' ','_')
    create_table = create_table + "'" + tg + "' TEXT);"
    row_name = row_name + "'" + tg + "'"
    value = value + "?"

    # Creating the table into our database
    cursor.execute(create_table)

    # SQL query to insert data into the table
    insert_records = f"INSERT INTO {name} ({row_name}) VALUES({value})"

    # Importing the contents of the file into our person table
    cursor.executemany(insert_records, contents)

    # Commiting the changes
    connection.commit()

    # closing the database connection
    connection.close()

except:
    print('Table exist')



end = time.time()

print("Time: "+str(end-start))
