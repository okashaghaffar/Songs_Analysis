# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 09:59:50 2022

@author: PC
"""

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
songs=pd.read_csv("songs.csv")
#print(songs.head())

print("Total Values are : ",np.product(songs.shape))
print("missing values are : ",songs.isnull().sum().sum())
print("missing percent values are :",(songs.isnull().sum().sum()/np.product(songs.shape))*100,"%")
songs.dropna(axis=1,inplace=True)

gp = pd.DataFrame({"Songs Existed":songs.groupby("peak-rank").song.count()}).reset_index()
gp=gp.sort_values(by='peak-rank')
print(gp)
plt.figure(figsize=(100,50))
sns.barplot(data=gp, x="peak-rank",y="Songs Existed")

plt.show()