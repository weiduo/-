
#coding:utf-8
import numpy as np
import pandas as pd
#import visuals as vs
from IPython.display import display 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.decomposition import PCA
from sklearn.decomposition import RandomizedPCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.grid_search import GridSearchCV
from scipy import stats

import time


try:
    data = pd.read_csv("first_test_index_20180131.csv")
    print data
    #data.drop(['Region', 'Channel'], axis = 1, inplace = True)
    #print "dataset has {} samples with {} features each.".format(*data_origin.shape)
except:
    print "Dataset could not be loaded. Is the dataset missing?"

data = data.set_index('id', drop=True, append=False, inplace=False, verify_integrity=False)


all_peaks = {}
count = 0

#d = open('/Users/suyangluojia/Desktop/LEARN/天池/天文数据挖掘/peaks.txt', 'a')

for i in data.index:
    f = open('/Users/suyangluojia/Desktop/LEARN/天池/天文数据挖掘/first_test_data_20180131/%s.txt'%i, 'r')
    d = open('/Users/suyangluojia/Desktop/LEARN/天池/天文数据挖掘/peaks.txt', 'a')
    waves_str = f.read()
    waves_s = waves_str.split(',')
    waves_float = pd.Series(map(float,waves_s))
    #waves_int = pd.Series(map(ggg,waves_s)).value_counts()
    
    
    peaks = {}
    kernel = stats.gaussian_kde(waves_float)
    
    if int(min(waves_float))> -10000:
        wave_min = int(min(waves_float))
    else: 
        wave_min = -10000
        
    if int(max(waves_float))< 10000:
        wave_max = int(max(waves_float))
    else: 
        wave_max = 10000
        
    x = range(wave_min,wave_max)
    for p in x:
        if (kernel(p-1)<kernel(p))&(kernel(p+1)<kernel(p)):
            peaks[p] = kernel(p)[0]
    peaks = pd.Series(peaks).sort_values(ascending = False)
    all_peaks[i] = peaks
    d.write(str(i)+";")
    d.write(str(peaks)+'\n')
    
    f.close()
    d.close()
    count +=1
    print count,i
    print int(min(waves_float)),int(max(waves_float))

d.close()