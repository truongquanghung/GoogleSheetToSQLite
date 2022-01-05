import pandas as pd

link = input()
segments = link.rpartition('/')
gid = link.rpartition('gid')
link = segments[0] + "/export?format=csv&gid" + gid[2]
csv_content = pd.read_csv(link)
file_path = 'test.csv'
csv_content.to_csv(file_path, index=False)