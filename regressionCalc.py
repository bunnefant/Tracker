import plotly.graph_objects as go
from matplotlib import pyplot as plt
from matplotlib import *
import time
import numpy as np
import datetime as dt
from scipy import stats
from sklearn.metrics import r2_score
from scipy import stats
from scipy.signal import argrelextrema

def maxima(regression):
    crit = regression.deriv().r
    criticalValues = crit[crit.imag==0].real
    secDerivTest = regression.deriv(2)(criticalValues)
    xMaxima = criticalValues[secDerivTest<0]
    return xMaxima

def minima(regression):
    crit = regression.deriv().r
    criticalValues = crit[crit.imag==0].real
    secDerivTest = regression.deriv(2)(criticalValues)
    xMinima = criticalValues[secDerivTest>0]
    return xMinima

def linearRegressor(dftemp, metric):
    #Getting R-squared of a linear regression using metric, returns pair of estimated price at current time and r squared
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    i = 0
    for ts in timeListTs:
        timeListInt.append(i)
        i=i+1
    closeList = dftemp[metric].tolist()
    #print(timeListTs)
    #print(closeList)
    #plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(timeListInt, closeList)
    trendStats = (slope, intercept, r2_value)
    r2_value = r_value**2
    trendpoly = np.poly1d(trend)
    print(trendpoly)
    #plt.plot(timeListInt, trendpoly(timeListInt))
    #plt.show()
    #print(str(slope)+" "+str(intercept)+" "+str(r_value)+" "+str(std_err))
    return trendStats

def linearRegressorTime(dftemp, metric, timeInterval):
    #Getting R-squared of a linear regression for time and another metric for last timeInterval minutes
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    z = 0
    closeListUncut = dftemp[metric].tolist()
    closeList = []
    j = len(closeListUncut)
    while(z<timeInterval):
        timeListInt.append(z)
        #print(j-(timeInterval-z))
        closeList.append(closeListUncut[j-(timeInterval-z)])
        z=z+1
    #print(timeListTs)
    print(closeList)
    #plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(timeListInt, closeList)
    r2_value = r_value**2
    trendStats = (slope, intercept, r2_value)
    trendpoly = np.poly1d(trend)
    #plt.plot(timeListInt, trendpoly(timeListInt))
    #plt.show()
    #print(str(slope)+" "+str(intercept)+" "+str(r_value)+" "+str(std_err))
    return trendStats

def quadRegressor(dftemp, metric):
    #Getting R-squared for quadratic regression for time and another metric
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    i = 0
    for ts in timeListTs:
        timeListInt.append(i)
        i=i+1
    closeList = dftemp[metric].tolist()
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 2)
    print(trend)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    print(trendpoly)
    plt.plot(timeListInt, trendpoly(timeListInt))
    print(maxima(trendpoly))
    plt.show()
    return r2_value

def quadRegressorTime(dftemp, metric, timeInterval):
    #Getting R-squared for quadratic regression for time and another metric for last timeInterval minutes
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    z = 0
    closeListUncut = dftemp[metric].tolist()
    closeList = []
    j = len(closeListUncut)
    while(z<timeInterval):
        timeListInt.append(z)
        #print(j-(timeInterval-z))
        closeList.append(closeListUncut[j-(timeInterval-z)])
        z=z+1
    #print(len(closeList))
    #print(len(timeListInt))
    #plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 2)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    #plt.plot(timeListInt, trendpoly(timeListInt))
    #plt.show()
    return r2_value

def nDegreeRegressor(dftemp, metric, n):
    #Getting R-squared for nth degree regression for time and another metric
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    i = 0
    for ts in timeListTs:
        timeListInt.append(i)
        i=i+1
    closeList = dftemp[metric].tolist()
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, n)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    maximum = maxima(trendpoly)
    for i in maximum:
        plt.plot(i, trendpoly(i), 'rs')
    minimum = minima(trendpoly)
    for i in minimum:
        plt.plot(i, trendpoly(i), '^k')
    plt.show()
    return r2_value

def nDegreeRegressorTime(dftemp, metric, n, timeInterval):
    #Getting R-squared for nth degree regression for time and another metric for last timeInterval minutes
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    z = 0
    closeListUncut = dftemp[metric].tolist()
    closeList = []
    j = len(closeListUncut)
    while(z<timeInterval):
        timeListInt.append(z)
        #print(j-(timeInterval-z))
        closeList.append(closeListUncut[j-(timeInterval-z)])
        z=z+1
    #print(len(closeList))
    #print(len(timeListInt))
    #plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, n)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    #plt.plot(timeListInt, trendpoly(timeListInt))
    #plt.plot(timeListInt, trendpoly(timeListInt))
    #plt.show()
    return r2_value
