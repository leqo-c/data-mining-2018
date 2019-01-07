#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:25:12 2018

@author: leorsu
"""

import numpy as np
from sklearn.cluster import DBSCAN

def dbscan_search(df, min_pts):

    xx = np.linspace(0.01, 1.00, 200)
    yy = list()
    for eps in xx:
        dbscan = DBSCAN(eps, min_samples=min_pts, metric='euclidean')
        dbscan.fit(df)
        labels = dbscan.labels_
        # yy = size of noise cluster
        yy.append(float(len([1 for i in labels if i == -1])) / len(df.values))
    
    my_eps = min( [ xx[i] for i in range(len(xx)) if yy[i]<=0.01 ] )
    
    return xx,yy,my_eps
