# Import required modules
import pandas as pd
import csv
from urllib.parse import urlparse
import sqlite3
from io import StringIO

print('link: ')
link = input()
print('table name: ')
name = input()

try:
    # Download data form Google Sheet to csv file 
    domain = urlparse(link).netloc
    segments = link.rpartition('/')
    link = segments[0] + "/export?format=csv"
    csv_content = pd.read_csv(link)
    buffer = StringIO()  #creating an empty buffer
    csv_content.to_csv(buffer, index=False)  #filling that buffer
    buffer.seek(0)

    # Connecting to the database
    connection = sqlite3.connect('db.sqlite3')

    # Creating a cursor object to execute SQL queries on a database table
    cursor = connection.cursor()

    # Table Definition
    create_table = f'CREATE TABLE {name}(id INTEGER PRIMARY KEY AUTOINCREMENT, '

    # Opening the .csv file
    contents = csv.reader(buffer)
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
except Exception as e:
    print(e)
