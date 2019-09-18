# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:01:11 2019

@author: SAYELI
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


# importing dataset

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
# CTR is click trough rate of the 10 ads.
''' Each time the user login  we will show on ad version. and see weather he cliked it
or not. Then again when he comes next time we will do it with a different ad. THis way we will find 
out which ad version cliking the most. And Showing each version of the Ad will have some strategy.
we will not do it randomly. it will have a particular strategy. Which will dependent on the
previous result'''

# Implementing UCB
# Implementing UCB
import math
N = 10000
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

#Visulization
plt.hist(ads_selected)
plt.title('Histogram of Ads Selection')
plt.xlabel('Ads')
plt.ylabel('Number of TImes Ad selected')
plt.show()

    
    
    