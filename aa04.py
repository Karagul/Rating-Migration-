# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:31:54 2020

@author: U0047365
"""



from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta


maxDate=b
minDate=a

minimum={}
maximum={}
for i in range(0,AnzHist):
    minimum[i]=[min(maxDate,i) for i in shorted21[i].valid_to]
    maximum[i]=[max(minDate,i) for i in shorted21[i].valid_from]
    
    
max(0.00001,str(minimum[1][1]-maximum[1][1])))

exists_indays={}
for i in range(0,AnzHist-11):
    print(minimum[i][1])
    exists_indays[i]=[max(0.00001, s-p) for s,p in minimum[i][1] - maximum[i][1]]

for k, i in enumerate( range(0,len(minimum))):
    print(k,minimum[i] - maximum[i])
    relativedelta(days=d)
    exists_days.append(max(0.00001, minimum[i] - maximum[i]))

ratingHist.Verweildauern(letztesRating) = ratingHist.Verweildauern(letztesRating) + aufenthaltInTagen

dates=[i for i in rrule(MONTHLY,bymonthday=1,\
            dtstart=a,until=b)]
    

























#%%
def timeframes(a,b):
    int_laenge=1
    from dateutil.rrule import rrule, MONTHLY
    from dateutil.relativedelta import relativedelta
    dates=[i for i in rrule(MONTHLY,bymonthday=1,\
            dtstart=a,until=b)]
    
    AnzHist = min(len(dates), 12 * 20)
    
    t_begin=[]
    t_ende=[]
    q=0
    p=0
    for i in range(0,AnzHist):
        q=(AnzHist-i)*int_laenge+1
        t_ende.append(a+relativedelta(months=q))
        
        p=(AnzHist-(i+1))*int_laenge+1
        t_begin.append(a+relativedelta(months=p))
    t_endedates=[]
    for i in t_ende:    
        d=-1
        t_endedates.append(i+relativedelta(days=d))
    t_endedates[0]=b
    print("The timeframe in months: " +str(AnzHist))
    return t_endedates,t_begin, AnzHist




def cluster(rating):
    if rating>=0 and rating<=11:
        clus=1
    elif rating>=12 and rating<=15:
        clus=2
        
    elif rating>=16 and rating<=21:
        clus=3
        
    elif rating>=22 and rating<=24:
        clus=4
    else:
        pass
    return clus      
        
def pad (A, length):
    import numpy as np
    arr=np.zeros(length)
    arr[:len(A)]
    return arr
#%%
    
if __name__=='__main__':
    timeframes()
    cluster()   
print("Completed.")    
    