from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

alamat = "https://pokemondb.net/pokedex/all"
safeAdd = Request(alamat, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(safeAdd)
data = BeautifulSoup(html, 'html.parser')

table = data.findAll("table",{"class":"data-table"})[0]
rows = table.findAll("tr")[1:28]

csvFile = open("Pokemonn.csv",'wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)  
try:   
        for cell in rows:
            th = cell.find_all('th')
            th_data = [col.text.strip('\n') for col in th]
            td = cell.find_all('td')
            row = [i.text.replace('\n','') for i in td]
            writer.writerow(th_data+row)      
        
finally:   
    csvFile.close()