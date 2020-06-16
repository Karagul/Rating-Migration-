# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:31:54 2020

#@author: U0047365
"""


def migrated_alives(output_cum_matrix,output_rating_change,AnzHist):
    '''
    output_cum_matrix takes first output of cum_matrix aa2.py function,i.e.
    cum_matrix()[0].
    output_rating_change takes first output of rating_change aa2.py 
    function,i.e. rating_change()[0]
    Returns to  migrations-excluding-defaults in all timeframes and 
    in [last month ,last 3 months, 12 months] 

    '''
    import pandas as pd
    
    # create a Sprungweitenmatrix with no defaulted
    
    s1=pd.DataFrame(columns=range(0,25),index=range(0,25)) 
    for i in s1.index:
        if i==0:
            s1.loc[i]=range(0,25)
        else:
            s1.loc[i]=s1.iloc[0,:]-i
    
    matrix_ohne_D=s1.iloc[0:22,0:22]
    helper_val8= [4 ,3 ,2, 1,0, -1,-2,-3,-4]
    val7=output_cum_matrix
    val8=output_rating_change

    result_12=[]
    for i in range(0,AnzHist):
            
        attrib=pd.DataFrame(val7[i].iloc[0:22,0:22])
        
        lig=pd.DataFrame(attrib.values*matrix_ohne_D.values)
        lig['summe']=[ sum(lig.loc[i]) for i in range(len(lig))]
        
        attrib['summe']=[ sum(i) for s, i in attrib.iterrows()]
        
        result_12.append(sum(lig['summe'])/sum(attrib['summe']))
    
    result_13=[]
    result_14=[]
    for i in range(1,AnzHist):   
         
        attrib2=val8[i].iloc[1:10,:]
        lig2=[t*r for t, r in zip(attrib2['re-rating (excl.defaults)'],\
        helper_val8)]    
        result_13.append(sum(lig2)/attrib2['re-rating (excl.defaults)'].sum())
    
        result_14.append(val8[i].iloc[0:5,:].sum()/val8[i].iloc[6:11,:].sum())
     
    selection=[1,3,11] #[last month ,last 3 months, 12 months]  
    
    result_122=[result_12[i]  if result_12[i] is not None else '-' for i in selection]
    result_133=[result_13[i-1]  if result_13[i] is not'nan' else '-' for i in selection]
    result_144=[result_14[i-1][0]  if result_14[i][0] is not'nan' else '-' for i in selection]

    return result_122,result_133, result_144


#%%%
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
        
        
# draft For default rate scaled to 1Y analysis 
        
#    selection=[1,3,11] #[last month ,last 3 months, 12 months] 
#    result_15=[]
#    for i in selection:
#        attrib=pd.DataFrame(val7[i].iloc[0:22,0:22])
#        
#        lig=pd.DataFrame(attrib.values*matrix_ohne_D.values)
#        lig['summe']=[ sum(lig.loc[i]) for i in range(len(lig))]
#        
#        attrib['summe']=[ sum(i) for s, i in attrib.iterrows()]
#        
#        result_13.append(sum(lig['summe'])/sum(attrib['summe']))
#%%
    
if __name__=='__main__':
    migrated_alives()
    timeframes()
    cluster()   
print("Completed.")    
    
