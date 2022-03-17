# Import required modules
import pandas as pd
import sqlite3
import time

start = time.time()
# Connecting to the database
connection = sqlite3.connect('db.sqlite3')

name = input()
file_name = input()

# Table Definition
try:
    if '.csv' in file_name:
        # Reading the contents of the .csv file
        df = pd.read_csv(file_name)
        df.index += 1
        df.columns = df.columns.str.replace(' ','_')
        df.to_sql(name, connection)
    else:
        dfs = pd.read_excel(file_name, sheet_name=None)
        for sheet, df in dfs.items():
            df.index += 1
            df.columns = df.columns.str.replace(' ','_')
            df.to_sql(name, connection)
    # closing the database connection
    connection.close()

except Exception as e:
    print(e)

end = time.time()

print("Time: "+str(end-start))
