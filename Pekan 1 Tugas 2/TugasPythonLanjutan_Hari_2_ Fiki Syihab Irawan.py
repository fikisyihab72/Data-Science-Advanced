from urllib.request import urlopen
from bs4 import BeautifulSoup

alamat = "https://blog.sanbercode.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

items = data.findAll("a", {"class":"text-dark"})[1]
items2 = data.findAll("a", {"class":"text-dark"})[2]
items3 = data.findAll("a", {"class":"text-dark"})[3]

pengarang1 = data.findAll("a", {"class":"text-muted text-capitalize"})[1]
pengarang2 = data.findAll("a", {"class":"text-muted text-capitalize"})[1]
pengarang3 = data.findAll("a", {"class":"text-muted text-capitalize"})[2]

items = items.get_text().strip()
items2 = items2.get_text().strip()
items3 = items3.get_text().strip()

pengarangz = pengarang1.get_text().strip()
pengarangx = pengarang2.get_text().strip()
pengarangc = pengarang3.get_text().strip()

judul = [items, items2, items3]
penulis = [pengarangz, pengarangx, pengarangc]

print (judul)
print (penulis)