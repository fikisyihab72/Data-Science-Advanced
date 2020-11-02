#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import requests
import numpy as np


response = requests.get('https://pokemondb.net/pokedex/all')

if __name__ == '__main__':
  df = pd.read_html(response.content, flavor='bs4')

  pokedex_12 = df[0]['#'] <= 12
  pokemon = df[0][pokedex_12]


# In[21]:


print(pokemon)


# In[24]:


pokemon.to_excel("TugasPythonLanjutan_Hari_10_Fiki Syihab Irawan.xlsx", index=False)

