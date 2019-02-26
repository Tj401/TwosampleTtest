# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
#import statsmodels.api as sm
#import pylab
import scipy.stats as stats
#from scipy import stats
from matplotlib import pyplot
#import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.gofplots import qqplot
#from tkinter.filedialog import askopenfilename
#twosample = pd.ExcelFile(askopenfilename())
twosample = pd.ExcelFile('C:/Users/kdandebo/Desktop/Models/DS training/Yogesh data sets/Promotion.xlsx')
twosample = twosample.parse("Sheet1")
print(twosample.columns)
twosample = twosample[twosample.columns[3:5]]
twosample = twosample.rename(columns={'Interest Rate Waiver ($ spent)': 'IDAY', 'Standard Promotion ($ spent)': 'XMAS'})
print(twosample.head(5))
twosample = twosample.dropna()
conv_arr= twosample.values
#split matrix into 3 columns each into 1d array
arr1 = np.delete(conv_arr,[1,2],axis=1) 
arr2 = np.delete(conv_arr,[0,2],axis=1) 

#converting into 1D array
IDAY = arr1.ravel()
XMAS = arr2.ravel()


#Normality test - Finding whether the data lies in the ND or not

qqplot(twosample['IDAY'], line='s')
qqplot(twosample['XMAS'], line='s')
pyplot.show()

#checking whether they actually follow the ND or not by checkng the P value
print(stats.shapiro(IDAY))
print(stats.shapiro(XMAS))
#as p-value> 0.05, so Ha is applicable - both the data follow ND

#varinace test
#print(var.test(twosample['IDAY'],twosample['XMAS']))
#F = Var(IDAY) / Var(XMAS)
#scipy.stats.f.cdf(F, len(IDAY)-1, len(XMAS)-1)
#f_test = f_regression(arr1, arr2)
#print(f_test)

#compare means using two sample ttest

print(stats.ttest_ind(IDAY,XMAS))
#because p <0.05 we go with Ha as means are not equal, now checking which mean is greater

