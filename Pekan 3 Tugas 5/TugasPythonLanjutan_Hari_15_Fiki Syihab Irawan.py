#!/usr/bin/env python
# coding: utf-8

# In[8]:


from openpyxl import load_workbook, Workbook
import sqlite3


# In[12]:


def open_excel():
    data = load_workbook(filename="pokemon_db.xlsx")
    sheet = data.active
    return sheet


# In[43]:


def convert_dict(sheet):
    pokemon_data = []
    for row_index in range (len(sheet['A'])):
        if sheet[row_index+1][0].value == "Name":
            continue

        pokemon = {}
        pokemon['Name']=sheet[row_index+1][0].value
        pokemon['Type']=sheet[row_index+1][1].value
        pokemon['Total']=sheet[row_index+1][2].value
        pokemon['HP']=sheet[row_index+1][3].value
        pokemon['Attack']=sheet[row_index+1][4].value
        pokemon['Defense']=sheet[row_index+1][5].value
        pokemon['Sp. Atk']=sheet[row_index+1][6].value
        pokemon['Sp. Def']=sheet[row_index+1][7].value
        pokemon['Speed']=sheet[row_index+1][8].value

        pokemon_data.append(pokemon)
    return pokemon_data


# In[45]:


data = open_excel()
poke_dict = convert_dict(data)


# In[46]:


import json
with open('Fiki.json', 'w') as outfile:
    json.dump(poke_dict, outfile)

