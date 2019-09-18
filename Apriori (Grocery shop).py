# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:54:59 2019

@author: SAYELI
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset



# Now we need to prepaire the into correctly. where all the transactions should be a list.
# And all the items in the trasaction should be a list. for that we run a for loop.
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

#Training of the Apriors of the dataset.
from apyori import apriori   
rules = apriori(transactions, min_support =0.003, min_confidence = 0.20, min_lift = 3, min_lenght = 2 )
''' We Considered a product that is purchased three times a day, So for a week its
3*7 = 21. We have total 7501 transaction. So min_support = 21/7501 = 0.0027'''

''' We have seen earlier that minimum confidence when set high takes products which
are bought very frequently not because they are truly associated instead they 
purchased more number of time'''

#Visualization of the results

results = list(rules)

output = []
for row in results:
    output.append(str(row.items))