# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:21:25 2020

@author: U0047365


 Function rating_counter --
 Dataframe variable should be  given after sorting and 
 filtering    operations from main file.
 The Variable is a dict containing pd.Dataframe type data in values) 
  count the number of ratings in each class   
 """
#    #Verlauf Tabellenblatt B9:B32  

def rating_counter(dataframe):         
    vert_3=dict()
    for key,j in dataframe.items():
        
        vert_3[key]={}
        for k in j.rating_grade:
            
            for i in range (0,25):
                
                if i==k:
                    vert_3[key][i]=j[(j.rating_grade==k)].count()[1]
                    break
               
                else:
                    pass
        
    return vert_3
    
#%%

def plot_barchart(dicted_data,enddates):
    """
    as t_endedates the  list of datetime.datetime type 
    of variables shoud be given 
    as dicted_data the output of rating_counter
    function should be passed
    Bar chart compares rating levels in given time frames
    in reporting worksheet range is 31.07.2017 - 31.07.2018
    """
    # Report Tabellenblatt Barchart   plot
    import matplotlib.pyplot as plt
    import numpy as np
    
    t_endedates=enddates
    vert_3=dicted_data
    fig, ax=plt.subplots(figsize=(19,6))
    labels=["AAAA","AAA", "AA+","AA","AA-","A+","A", "A-", "2",\
             "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",\
             "13", "14", "15", "16", "17", "18"]
    x=np.arange(len(labels))
    year=12 # interval in  months 
    rect1=ax.bar(x, list(vert_3[0+year].values()),width=-0.35,\
             color='pink', edgecolor='white')
    rect2=ax.bar(x, list(vert_3[0].values()),width=+0.35,\
                color='red',edgecolor='white')
    
    ax.set_ylabel ('Nuber of ratings')
    ax.set_title('All modules')
    
    ax.set_xticks(x) #x+0.35/2
    ax.set_xticklabels((labels),fontsize=13)
    
    ax.legend((rect1[0],rect2[0]),\
        (str(t_endedates[year+1].date()),str(t_endedates[0].date())),\
        loc=2,fontsize=13,frameon=False) # ('31.07.2017','31.07.2018'),
    
    ax.yaxis.grid(color='lightgrey', linewidth=0.8)
    ax.autoscale_view()
    return plt.show()

#%%

def reporting_0(dicted_data):
    '''
    returns to the  rating classes of latest observed timeframe 
    Input variables  are initially calculated 
    from main file and after are passed to this function
    '''
    import pandas as pd 
    vert_3=dicted_data
    
# Report Tabellenblatt G18
    labels=["AAAA","AAA", "AA+","AA","AA-","A+","A", "A-", "2",\
             "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",\
             "13", "14", "15", "16", "17", "18"]
    pd_zu_stufe=[0,0.0001,0.0002,0.0003,0.0004,0.0005,0.0007,
                     0.0009, 0.0011561, 0.00173415, 0.00260123,
                     0.00390184,0.00585277,0.00877915, 0.01316872,
                     0.01975309, 0.029629,0.0444444,0.0666667,
                     0.1, 0.15, 0.2]
    zz=["{:.2%}".format(i) for i  in pd_zu_stufe]                
    for i in range(0,3):
        zz.append('100%') 
    
    n_ratings=vert_3[0]
                    
    
    result0=pd.DataFrame([zz,list( n_ratings.values())], columns=labels)
    result0.index=['1Y-PD','number of ratings (#)']
    
    return result0                  


#%%
   
def reporting_1 (dicted_data, enddates): 
    '''
    returns to a wighted PD  ratios and assigns to nearest
    PD rating class
    as a matter of approximation  0.005 is used. This can be 
    increased or decreased.  
    Input variables  are initially calculated 
    from main file and after are passed to this function
    '''
    
    # Report Tabellenblatt G22
    # reference date
    import pandas as pd    
    vert_3=dicted_data
    t_endedates=enddates
    ratio={}
    pd_zu_stufe=[0,0.0001,0.0002,0.0003,0.0004,0.0005,0.0007,
                     0.0009, 0.0011561, 0.00173415, 0.00260123,
                     0.00390184,0.00585277,0.00877915, 0.01316872,
                     0.01975309, 0.029629,0.0444444,0.0666667,
                     0.1, 0.15, 0.2]
    for key, i in vert_3.items():
        
        ratio[key]=sum ([a*b for a, b in zip(list(i.values())[:22],\
        pd_zu_stufe)])/sum(list(i.values())[:22])
    
    PD_performing=list(ratio.values())
    PD_performing1=["{:.2%}".format(i) for i in PD_performing]

    
    grade=[]
    for k,l in enumerate(pd_zu_stufe):
    
        for j in PD_performing:
            
            if  l+0.005>=j>=l-0.005:
                grade.append(k-6)
    year=12           
    refdate=[t_endedates[i].date() for i in [1,2,4,1+year]]
    
    selection=[0,1,3,12]
    
    lo=[PD_performing1[i] for i in selection]
    co=[grade[i] for i in selection]
    result1=pd.DataFrame([lo, co], columns=refdate)
    result1.index=[' PD (number weighted; performing)','rating grade'] 
    
    return result1
        

#%%
    # Report Tabellenblatt G26
    #number of ratings (total) 
    
def reporting_2(dicted_data,dicted_alives, enddates, AnzHist):
    """
    dicted_data is the same type of variable as output from \
    rating_counter  function
    dicted_alives is  filtered out alive ratings in time frames, 
    dicted_alives is a dict containing dataframes in the leghth 
    of AnzHist.AnzHist should be a intiger
    Function retunrs to two arguments
    Input variables  are initially calculated from main file and
    after are passed to this function
    
    """
    import pandas as pd    
    vert_3=dicted_data
    t_endedates=enddates
    
    table_number=[sum(i.values()) for k, i in vert_3.items()]
    
    perf_num=[sum(list(i.values())[:22]) for k, i in vert_3.items()]
    selection=[0,1,3,12]
    non_perf_num=[a-b for a, b in zip(table_number,perf_num)]
    num_1=[table_number[i] for i in selection]
    
    num_2=[perf_num[i] for i in selection]
    
    num_2_1=["{:.2%}".format(a/b) for a,b in zip(num_2,num_1)]
    
    num_3=[non_perf_num[i] for i in selection]
    num_3_1=["{:.2%}".format(a/b) for a,b in zip(num_3,num_1)]
    
    year=12           
    refdate=[t_endedates[i].date() for i in [1,2,4,1+year]]
    
    result2=pd.DataFrame([num_1, num_2,num_2_1,num_3,num_3_1],\
    columns=refdate)
    result2.index=['number of ratings (total)','number of ratings (performing)',  'in %',\
                    'number of ratings (non-performing)',  'in %',  ] 

    # Report Tabellenblatt G30
    #age of ratings (performing; days)
    smort=dicted_alives 
    for i in range (0,AnzHist):
        for key,j in smort.items():
            if i==key:
                j['xxx']=t_endedates[i+1]-j['valid_from']  
            else:
                pass
    ras=[]
    selection=[0,1,3,12]
    for i in selection:
        for k,j in smort.items():
            if i == k:
                ras.append(j['xxx'].dt.days.sum())
    
    result3=[p/q for p,q in zip(ras,num_2)] 
    age=[round(i) for i in result3]
    result001=pd.DataFrame(age,columns=['age of ratings( performing days)'])
    result01=result001.T 
    
    return  result2, result01


if __name__=="__main__":
    rating_counter()
    plot_barchart()
    reporting_0()
    reporting_1()
    reporting_2()
    
print("Completed.")