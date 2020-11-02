#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


consumer_key = "ZTc8gleb1HkEN3CpJCsVgGCva"
consumer_secret = "1ixVSxHJHQPwMJUswkg6PiTqkptHMgEGsNxfo4O3jeB4x0qUn1"
access_token = "844846590649032706-QrO5iNylPUyfYBq23ZrB7wQp13PGtUq"
access_token_secret = "HknBidwR0BWZ0nibDBZt4CHbyaAnCxv7QeL48EyP9Hhwf"


# In[3]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[11]:


search_words = "jouska"
search_words2 = "anies baswedan"
search_words3 = "terawan agus putranto"
date_since = "2020-07-27"
new_search = search_words + " -filter:retweets"
new_search2 = search_words2 + " -filter:retweets"
new_search3 = search_words3 + " -filter:retweets"

tweets = tweepy.Cursor(api.search,
        q=new_search,
        lang="id",
        since=date_since).items(1000)
tweets2 = tweepy.Cursor(api.search,
        q=new_search2,
        lang="id",
        since=date_since).items(1000)
tweets3 = tweepy.Cursor(api.search,
        q=new_search3,
        lang="id",
        since=date_since).items(1000)


# In[12]:


items = []
for tweet in tweets:
    item = []
    item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
    items.append(item)
    items.append(item)
hasil = pd.DataFrame(data=items, columns=['tweet'])

items2 = []
for tweet2 in tweets2:
    item2 = []
    item2.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet2.text).split()))
    items2.append(item2)
    items2.append(item2)
hasil2 = pd.DataFrame(data=items2, columns=['tweet'])

items3 = []
for tweet3 in tweets3:
    item3 = []
    item3.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet3.text).split()))
    items3.append(item3)
    items3.append(item3)
hasil3 = pd.DataFrame(data=items3, columns=['tweet'])


# In[ ]:


pos_list= open("./kata_positif.txt","r")
pos_kata = pos_list.readlines()
neg_list= open("./kata_negatif.txt","r")
neg_kata = neg_list.readlines()


# In[37]:


S=[]
for item in items:
    count_p = 0
    count_n = 0
    for kata_pos in pos_kata:
        if kata_pos.strip() in item[0]:
            count_p +=1
    for kata_neg in neg_kata:
        if kata_neg.strip() in item[0]:
            count_n +=1
    S.append(count_p - count_n)
hasil["value"] = S
print('Sentimen analisis pada tweet Penipuan oleh Jouska')
print ("Nilai rata-rata: "+str(np.mean(hasil["value"])))
print ("Nilai median : "+str(np.median(hasil["value"])))

labels, counts = np.unique(hasil["value"], return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()


# In[38]:


S2=[]
for item2 in items2:
    count_p2 = 0
    count_n2 = 0
    for kata_pos2 in pos_kata:
        if kata_pos2.strip() in item2[0]:
            count_p2 +=1
    for kata_neg2 in neg_kata:
        if kata_neg2.strip() in item2[0]:
            count_n2 +=1
    S2.append(count_p2 - count_n2)
hasil2["value"] = S2
print('Sentimen analisis pada tweet Gubernur Jakarta, Anies Baswedan')
print ("Nilai rata-rata: "+str(np.mean(hasil2["value"])))
print ("Nilai median : "+str(np.median(hasil2["value"])))

labels, counts = np.unique(hasil2["value"], return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()


# In[39]:


S3=[]
for item3 in items3:
    count_p3 = 0
    count_n3 = 0
    for kata_pos3 in pos_kata:
        if kata_pos3.strip() in item3[0]:
            count_p3 +=1
    for kata_neg3 in neg_kata:
        if kata_neg3.strip() in item3[0]:
            count_n3 +=1
    S3.append(count_p3 - count_n3)
hasil3["value"] = S3
print('Sentimen analisis pada tweet Menteri Kesehatan, Pak Terawan Agus Putranto')
print ("Nilai rata-rata: "+str(np.mean(hasil3["value"])))
print ("Nilai median : "+str(np.median(hasil3["value"])))

labels, counts = np.unique(hasil3["value"], return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()


# In[36]:


print('KESIMPULAN')
print('Sentimen analisis pada tweet Penipuan oleh Jouska')
print('1. Hasil tweet yang berhasil discrapping memiliki jumlah paling banyak dibanding 2 tweet lainnya')
print('2. Nilai rata-rata yang dihasilkan adalah  -0.5159235668789809')
print('3. Nilai median yang dihasilkan adalah 0.0')
print('4. Sentimen analisis yang dihasilkan cenderung negatif dilihat dari nilai rata-rata point sentimen')
print('5. Bar graph menunjukan tweet paling banyak memiliki sentimen netral yaitu 0 point dengan jumlah tweet lebih dari 500')
print('6. Tweet yang memiliki point sentimen paling tinggi adalah 5 point')
print('7. Tweet yang memiliki point sentimen paling rendah adalah -9 point')
print('')
print('Sentimen analisis pada tweet Gubernur Jakarta, Anies Baswedan')
print('1. Hasil tweet yang berhasil discrapping memiliki jumlah paling banyak kedua setelah tweet Penipuan oleh Jouska')
print('2. Nilai rata-rata yang dihasilkan adalah  -0.6739606126914661')
print('3. Nilai median yang dihasilkan adalah -1.0')
print('4. Sentimen analisis yang dihasilkan cenderung negatif dilihat dari nilai rata-rata point sentimen')
print('5. Bar graph menunjukan tweet paling banyak memiliki sentimen negatif yaitu -1 point dengan jumlah tweet lebih dari 350')
print('6. Tweet yang memiliki point sentimen paling tinggi adalah 5 point')
print('7. Tweet yang memiliki point sentimen paling rendah adalah -7 point')
print('')
print('Sentimen analisis pada tweet Menteri Kesehatan, Pak Terawan Agus Putranto')
print('1. Hasil tweet yang berhasil discrapping memiliki jumlah paling sedikit dibandingkan 2 tweet lainnya')
print('2. Nilai rata-rata yang dihasilkan adalah  0.75')
print('3. Nilai median yang dihasilkan adalah 1.0')
print('4. Sentimen analisis yang dihasilkan cenderung positif dilihat dari nilai rata-rata point sentimen yaitu 0.75')
print('5. Bar graph menunjukan tweet paling banyak memiliki sentimen positif yaitu 1 point dengan jumlah 9 tweet')
print('6. Tweet yang memiliki point sentimen paling tinggi adalah 2 point')
print('7. Tweet yang memiliki point sentimen paling rendah adalah -1 point')
      


# In[ ]:





# In[ ]:




