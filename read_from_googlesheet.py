import pandas as pd

link = input()
segments = link.rpartition('/')
link = segments[0] + "/export?format=csv"
csv_content = pd.read_csv(link)
file_path = 'test.csv'
csv_content.to_csv(file_path, index=False)