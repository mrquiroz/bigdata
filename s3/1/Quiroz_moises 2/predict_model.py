#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.metrics import classification_report


# In[2]:


df = pd.read_csv('test_delivery_data.csv', header=None)
df.columns = ['deliverer_id', 'delivery_zone', 'monthly_app_usage','subscription_type', 'paid_price','customer_size', 'menu','delay_time']
df['delay_time'] = np.where(df['delay_time']>np.mean(df.delay_time), 1, 0)
df = pd.get_dummies(df,columns=['subscription_type','delivery_zone','menu'],drop_first=True)
df.head()


# In[3]:


modelo = joblib.load('DecisionTreeClassifier.pkl')
y = df.pop('delay_time')
y = modelo.predict(df)


# In[4]:


df2 = pd.read_csv('test_delivery_data.csv', header=None)
df2.columns = ['deliverer_id', 'delivery_zone', 'monthly_app_usage','subscription_type', 'paid_price','customer_size', 'menu','delay_time']
df2['delay_time'] = np.where(df2['delay_time']>np.mean(df2.delay_time), 1, 0)
df2['prediction'] = y


# In[5]:


def probabilidad(clase):
    print('*'*50)
    print('Probabilidad de atraso sobre media para la clase:', clase,'\n')
    for i in df2[clase].unique():
        print('la probabilidad de atraso para',clase,i,'es:',df2[df2[clase] == i]['prediction'].mean())
    print('\n')


# In[6]:


probabilidad('delivery_zone')
probabilidad('deliverer_id')
probabilidad('menu')
probabilidad('subscription_type')


# In[ ]:




