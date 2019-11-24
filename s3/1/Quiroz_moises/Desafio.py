#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[5]:


df = df = pd.read_csv('train_delivery_data.csv', header=None)


# In[8]:


df.columns = ['deliverer_id', 'delivery_zone', 'monthly_app_usage','subscription_type', 'paid_price','customer_size', 'menu','delay_time']


# In[9]:


df.head()


# In[10]:


media_delay = np.mean(df.delay_time)
media_delay


# In[12]:


df['delay_time'] = np.where(df['delay_time']>media_delay, 1, 0)
df.head()


# In[13]:


df = pd.get_dummies(df,columns=['subscription_type','delivery_zone','menu'],drop_first=True)


# In[15]:


df.head()


# In[16]:


from sklearn.model_selection import train_test_split


# In[17]:


y = df.pop('delay_time')


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.33, random_state=11238)


# In[20]:


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.naive_bayes import BernoulliNB


# In[25]:


logi = LogisticRegression().fit(X_train, y_train)
Ber = BernoulliNB().fit(X_train, y_train)
Desi = DecisionTreeClassifier().fit(X_train, y_train)
rand = RandomForestClassifier().fit(X_train, y_train)


# In[26]:


from sklearn.metrics import classification_report


# In[ ]:





# In[31]:


modelos = [logi,Ber,Desi,rand]
text_file = open("candidate_models.txt", "w")
for mo in modelos:
    text_file.write("modelo: "+type(mo).__name__+'\n')
    print("modelo:",type(mo).__name__)
    text_file.write(classification_report(y_test,mo.predict(X_test)))
    print(classification_report(y_test,mo.predict(X_test)))
text_file.close()


# In[32]:


from sklearn.externals import joblib


# In[34]:


filename = 'DecisionTreeClassifier.pkl'
joblib.dump(Desi, filename)
print("mejor modelo DesionTree")


# In[ ]:




