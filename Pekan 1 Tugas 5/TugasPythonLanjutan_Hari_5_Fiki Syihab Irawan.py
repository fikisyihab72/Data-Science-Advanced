#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

response = requests.get('https://pokemondb.net/pokedex/all')

if __name__ == '__main__':
  df = pd.read_html(response.content, flavor='bs4')

  pokedex_850 = df[0]['#'] <= 850
  pokemon = df[0][pokedex_850]

  pokemon.to_csv('pokemon.csv', index=False)

print(pokemon.head())


# In[20]:


pokemon_x = pokemon.iloc[:, 5:7]
pokemon_x


# In[21]:


x_array = np.array(pokemon_x)
print(x_array)


# In[10]:


#scaler = MinMaxScaler()
#x_scaled = scaler.fit_transform(x_array)
#x_scaled


# In[22]:


# Menentukan dan mengkonfigurasi fungsi kmeans
kmeans = KMeans(n_clusters = 3)
# Menentukan kluster dari data
kmeans.fit(x_array)


# In[23]:


print(kmeans.cluster_centers_)


# In[40]:



pokemon["kluster"] = kmeans.labels_
pokemon.head()


# In[31]:


c = pokemon.kluster
plt.scatter(x_array[:,1], x_array[:,0], s =10, c = c, marker = "o", alpha = 1)
plt.title("Hasil Klustering K-Means")
plt.xlabel("ATK")
plt.ylabel("DEF")
plt.show()


# In[ ]:


#Kesimpulan
# 1. Titik terendah adalah pokemon yang memiliki ATK 5 dan DEF 5
# 2. Terdapat pokemon yang memiliki ATK tinggi yatu lebih dari 250 dan Def kecil +-15 
# 3. Distribusi data paling banyak berpusat antara range 30 hingga 150 ATK dan DEF
# 4. Terdapat pokemon yang memiliki DEF tinggi yaitu >175 namun memiliki ATK rendah +-18
# 5. Data terbagi menjadi 3 klaster utama
# 6. Klaster hijau cenderung memiliki DEF dan ATK yang paling rendah dibanding klaster lain
# 7. Klaster Kuning cenderung memiliki DEF yang tinggi namun ATK rendah
# 8. Klaster Ungu cenderung memiliki ATK yang tinggi namun DEF rendah

