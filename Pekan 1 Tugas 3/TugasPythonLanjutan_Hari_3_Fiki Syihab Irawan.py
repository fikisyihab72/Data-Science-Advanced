from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

alamat = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

table = data.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

for row in rows:
    for cell in row.findAll(["td", "th"]):
        cell.get_text()

hasil = []
for row in rows:
    info = []
    for cell in row.findAll(["td", "th"]):
        info.append(cell.get_text().strip())
    hasil.append(info)

df = pd.DataFrame(hasil)
new_header = df.iloc[0] #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
df.reset_index(drop=True, inplace=True)
print("Nomor 1")
print(df)

print("------------------------------------------------------------------------")
print("Nomor 2")

alamat = "https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

x=0
hasil_akhir = []

while(x<2):
    table = data.findAll("table", {"class":"wikitable"})[x]
    rows = table.findAll("tr")

    for row in rows:
        for cell in row.findAll(["td", "th"]):
            cell.get_text()

    hasil_2020_2021 = []
    for row in rows:
        info = []
        for cell in row.findAll(["td", "th"]):
            info.append(cell.get_text().strip())
        hasil_2020_2021.append(info)

    hasil_akhir = hasil_akhir + hasil_2020_2021
    x=x+1

print(hasil_akhir)