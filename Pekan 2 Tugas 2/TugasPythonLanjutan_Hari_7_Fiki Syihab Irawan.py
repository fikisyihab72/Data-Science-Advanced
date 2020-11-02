#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy


# In[20]:


consumer_key = "ZTc8gleb1HkEN3CpJCsVgGCva"
consumer_secret = "1ixVSxHJHQPwMJUswkg6PiTqkptHMgEGsNxfo4O3jeB4x0qUn1"
access_token = "844846590649032706-QrO5iNylPUyfYBq23ZrB7wQp13PGtUq"
access_token_secret = "HknBidwR0BWZ0nibDBZt4CHbyaAnCxv7QeL48EyP9Hhwf"


# In[21]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[22]:


nama = "jokowi"
jumlahtweet = 200

data_tweet = []
hasil = api.user_timeline(id=nama, count=jumlahtweet)

for tweet in hasil:
   data_tweet.append(tweet.text)


# In[23]:


#data_tweet


# In[24]:


counter = 0

for cov in data_tweet:
    if 'Covid' in cov:
        counter=counter+1


# In[25]:


print("Banyak Tweet Pak Jokowi yang diambil adalah :",jumlahtweet)
print("Banyaknya Pak Jokowi membicarakan tetang Covid sebanyak :",counter)


# In[ ]:




