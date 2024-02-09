import pandas as pd 
from bs4 import BeautifulSOup
import requests
import sqlite3


url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/project/top_50_films.csv'
df = pd.DataFrame (columns = ["Average Rank","Film","Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSOup(html_page,'html_parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# for row in rows:
#     if count <50:
#         col = row.find_all('td')
#         if len(col) != 0:
#             data_dict = {"average rank"}