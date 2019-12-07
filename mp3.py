#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 02:45:07 2019

@author: asukawatanabe
"""
import numpy as np

def coeff(x):
        X = x[0,:]
        Y = x[1,:]
        print(X)
        print(Y)
        if len(X)>=11:
                L = 10
        else:
                L = len(X)-1
        nm = np.zeros((L,1))
        print(nm)
        
        for i in range(1,L):
                fit = np.polyfit(X,Y,i)
                val = np.polyval(fit,X)
                nm[i-1,0] = np.linalg.norm(Y-val)
                I = nm.argmin()
                coeff = np.polyfit(X,Y,I+1)
                print(coeff)
                print('Best Fit Coefficient: \n',coeff)
coeff(np.array([(-3,-2,-1,0,1,2,3,4,5,6,7,8),(41,4,0,-7,-29,-52,-41,60,8,9,65,76)]))