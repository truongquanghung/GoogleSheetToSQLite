import pandas as pd
from urllib.parse import urlparse
link = input()
domain = urlparse(link).netloc
segments = link.rpartition('/')
link = segments[0] + "/export?format=csv"
csv_content = pd.read_csv(link)
file_path = 'test.csv'
csv_content.to_csv(file_path, index=False)
print(csv_content.to_csv())