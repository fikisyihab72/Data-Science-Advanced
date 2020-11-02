#!/usr/bin/env python
# coding: utf-8

# In[2]:


#IDENTITAS
#Nama : Fiki Syihab Irawan
#Email : fikiruztiez@gmail.com


import tweepy
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta
import sqlite3


# In[3]:


connection = sqlite3.connect('db_tugas_akhir.db')
cursor = connection.cursor()
#print("Database created and Successfully Connected to SQLite")
cursor.close()


# In[4]:


connection = sqlite3.connect("db_tugas_akhir.db")
create_tabel_tweet = '''CREATE TABLE IF NOT EXISTS tabel_tweet (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             user TEXT,
                             tanggal TEXTL,
                             tweet TEXT UNIQUE,
                             sentiment INTEGER);'''

cursor = connection.cursor()
cursor.execute(create_tabel_tweet)
connection.commit()
cursor.close()
connection.close()


# In[5]:


def autentikasi():
    consumer_key = "ZTc8gleb1HkEN3CpJCsVgGCva"
    consumer_secret = "1ixVSxHJHQPwMJUswkg6PiTqkptHMgEGsNxfo4O3jeB4x0qUn1"
    access_token = "844846590649032706-QrO5iNylPUyfYBq23ZrB7wQp13PGtUq"
    access_token_secret = "HknBidwR0BWZ0nibDBZt4CHbyaAnCxv7QeL48EyP9Hhwf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return(api)


# In[6]:


#Menu 1 ambil data + preprocessing
def updateData():
    api = autentikasi()
    #scrape()
    print("Silahkan tunggu beberapa saat....")
    print("*Proses scraping berlangsung 1-5 menit tergantung koneksi")
    search_words = "vaksin covid"
    date_since = date.today() - timedelta(days=1)
    new_search = search_words + " -filter:retweets"

    tweets = tweepy.Cursor(api.search, tweet_mode='extended',
            q=new_search,
            lang="id",
            since=date_since).items(1000)
    
    items = []
    for tweet in tweets:
        item = []
        item.append(tweet.user.screen_name)
        item.append(tweet.created_at)
        item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.full_text).split()))
        items.append(item)
    #hasil = pd.DataFrame(data=items, columns=['user','tanggal','tweet'])
    input_data(items)
    print("Data telah terupdate!")
    mainMenu()


# In[7]:


#Menu 1 Insert ke sqlite
def input_data(items):
    connection = sqlite3.connect("db_tugas_akhir.db")
    crud_query = '''INSERT OR IGNORE INTO tabel_tweet (user, tanggal, tweet) values (?,?,?)'''

    cursor = connection.cursor()
    cursor.executemany(crud_query,items)
    connection.commit()
    cursor.close()
    connection.close()


# In[8]:


#Menu 2 get all
def ambil_data():
    connection = sqlite3.connect("db_tugas_akhir.db")
    crud_query = '''SELECT * FROM tabel_tweet'''

    cursor = connection.cursor()
    cursor.execute(crud_query)
    hasilsemua =  cursor.fetchall()

    cursor.close()
    connection.close()
    return(hasilsemua)
    #hasil = pd.DataFrame(data=hasilsemua, columns=['id','user','tanggal','tweet','sentiment'])


# In[9]:


#Menu 2 scoring sentimen
def updateNilaiSentiment():
    print("Mohon tunggu sebentar....")
    hasilsemua = ambil_data()
    #perpustakaan_kata()
    
    pos_list= open("./kata_positif.txt","r")
    pos_kata = pos_list.readlines()
    neg_list= open("./kata_negatif.txt","r")
    neg_kata = neg_list.readlines()
    
    Sen=[]

    for item in hasilsemua:
        count_p = 0
        count_n = 0
        for kata_pos in pos_kata:
            if kata_pos.strip() in item[3]:
                count_p +=1
        for kata_neg in neg_kata:
            if kata_neg.strip() in item[3]:
                count_n +=1
        Sen.append(count_p - count_n)
    input_nilai_sentiment(Sen)
    #print(Sen)
    print("Nilai sentiment telah terupdate!")
    mainMenu()
    


# In[10]:


#Menu 2 Update sentimen
def input_nilai_sentiment(Sen):
    connection = sqlite3.connect("db_tugas_akhir.db")
    crud_query_sentiment = '''UPDATE tabel_tweet SET sentiment = ? WHERE id = ?'''


    cursor = connection.cursor()
    rowids = [id[0] for id in cursor.execute('SELECT id FROM tabel_tweet')]
    cursor.executemany(crud_query_sentiment, list(zip(Sen, sorted(rowids))))

    connection.commit()
    cursor.close()
    connection.close()


# In[11]:


def ambil_score_sentiment():
    print("Visualisasi Sentimen berdasarkan range tanggal")
    print("Format tanggal (yyyy-mm-dd)")
    print("Contoh : ")
    print("Tanggal awal = 2020-08-14")
    print("Tanggal akhir = 2020-08-15")
    print("--------------------------------------------")
    tgl1=input("Masukkan tanggal awal : ")
    tgl2=input("Masukkan tanggal akhir : ")
    hasilsemua = ambil_data_berdasar_tanggal(tgl1, tgl2)
    vv = []
    for item in hasilsemua:
        vv.append(item[4])
    return(vv)


# In[12]:


def visualisasi():
    #Menu 4
    #hasil["value"] = S
    vv = ambil_score_sentiment()
    print('Sentimen analisis')
    print ("Nilai rata-rata: "+str(np.mean(vv)))
    print ("Nilai median : "+str(np.median(vv)))
    print ("Nilai Standar Deviasi : "+str(np.std(vv)))

    labels, counts = np.unique(vv, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.gca().set_xticks(labels)
    plt.show()
    mainMenu()


# In[20]:


def lihatData():
    print("Menampilkan data berdasarkan range tanggal")
    print("Format tanggal (yyyy-mm-dd)")
    print("Contoh : ")
    print("Tanggal awal = 2020-08-14")
    print("Tanggal akhir = 2020-08-15")
    print("--------------------------------------------")
    tgl1=input("Masukkan tanggal awal : ")
    tgl2=input("Masukkan tanggal akhir : ")
    #print(tgl)
    hasil_query_tgl = ambil_data_berdasar_tanggal_visual(tgl1,tgl2)
    #hasil_tabel = pd.DataFrame(data=hasil_query_tgl, columns=['user','tanggal','tweet'])
    #pd.set_option('display.max_rows', 10000000)
    #print(hasil_tabel.to_string())
    for row in hasil_query_tgl:
      print(row)
    mainMenu()
    


# In[14]:


def ambil_data_berdasar_tanggal_visual(tgl1, tgl2):
    connection = sqlite3.connect("db_tugas_akhir.db")
    cursor = connection.cursor()
    cursor.execute("SELECT user, tanggal, tweet FROM tabel_tweet WHERE date(tanggal) BETWEEN date(?) AND date(?)",(tgl1,tgl2,))
    hasilsemua =  cursor.fetchall()

    cursor.close()
    connection.close()
    return(hasilsemua)


# In[15]:


def ambil_data_berdasar_tanggal(tgl1, tgl2):
    connection = sqlite3.connect("db_tugas_akhir.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tabel_tweet WHERE date(tanggal) BETWEEN date(?) AND date(?)",(tgl1,tgl2,))
    hasilsemua =  cursor.fetchall()

    cursor.close()
    connection.close()
    return(hasilsemua)


# In[16]:


def mainMenu():
    print('')
    print('===========================')
    print('Main Menu')
    print('1. Update data')
    print('2. Update Nilai sentiment')
    print('3. Lihat data')
    print('4. Visualisasi')
    print('5. Keluar')
    print('===========================')
    while True:
        try:
            selection=int(input("Pilih menu (1-5) : "))
            print("")
            if selection == 1:
                updateData()
                break
            elif selection == 2:
                updateNilaiSentiment()
                break
            elif selection == 3:
                lihatData()
                break
            elif selection == 4:
                visualisasi()
                break
            elif selection == 5:
                print("Program telah dihentikan")
                break
            else:
                print("Input salah. masukkan angka 1-5")
                mainMenu()
                break
        except ValueError:
            print("Input salah. masukkan angka 1-5")
    exit

                


# In[21]:


mainMenu()


# In[ ]:




