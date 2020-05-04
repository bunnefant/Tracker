import plotly.graph_objects as go
from matplotlib import pyplot as plt
import time
import numpy as np
import datetime as dt
from scipy import stats
from sklearn.metrics import r2_score
from scipy import stats
from sklearn.metrics import r2_score

def linearRegressor(dftemp, metric):
    #Getting R-squared of a linear regression for time and another metric
    timeListTs = dftemp['time'].tolist()
    timeListInt = []
    i = 0
    for ts in timeListTs:
        timeListInt.append(i)
        i=i+1
    closeList = dftemp[metric].tolist()
    #print(timeListTs)
    #print(closeList)
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(timeListInt, closeList)
    trendpoly = np.poly1d(trend)
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.show()
    #print(str(slope)+" "+str(intercept)+" "+str(r_value)+" "+str(std_err))
    return r_value**2

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
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(timeListInt, closeList)
    trendpoly = np.poly1d(trend)
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.show()
    print(str(slope)+" "+str(intercept)+" "+str(r_value)+" "+str(std_err))
    return r_value**2

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
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
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
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, 2)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.show()
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
    plt.plot(timeListInt, trendpoly(timeListInt))
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
    plt.plot(timeListInt, closeList, 'o')
    trend = np.polyfit(timeListInt, closeList, n)
    trendpoly = np.poly1d(trend)
    r2_value = r2_score(closeList, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.plot(timeListInt, trendpoly(timeListInt))
    plt.show()
    return r2_value
