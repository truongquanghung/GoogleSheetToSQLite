# Import required modules
import pandas as pd
import sqlite3

def make_table(link, name):
    try:
        # Download data form Google Sheet 
        segments = link.rpartition('/')
        gid = link.rpartition('gid')
        link = segments[0] + "/export?format=csv&gid" + gid[2]
        df = pd.read_csv(link)

        # Connecting to the database
        connection = sqlite3.connect('db.sqlite3')
        df.index += 1
        df.columns = df.columns.str.replace(' ','_')
        df.to_sql(name, connection)

        # closing the database connection
        connection.close()
    except Exception as e:
        print(e)

print('link: ')
link = input()
print('table name: ')
name = input()
make_table(link, name)