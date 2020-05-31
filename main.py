# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:22:11 2020

@author: U0047365
"""
import os
import pandas as pd
from datetime import datetime, timedelta, date
import numpy as np
import aa01 as a1
import aa02 as a2
import aa03 as a3
import aa04 as a4
import importlib as load
load.reload(a1)
load.reload(a2)
load.reload(a3)
load.reload(a4)
os.chdir("N:/506/5060/99 Sonstiges/Einarbeitung Sardor/Kopie.2019_LGD_Validierung/_Python") 
#%%
############################################## 

import1= 'MigrationenTool TRO v_2019(1)_eng.xlsx' # Datei auswählen

###############################################

#%%
print("Loading  the required datasets...")
df=pd.read_excel(import1,'Daten aufbereitet',encoding='utf-8', index=True)
print("Loading is completed.")
#%%
a=datetime(2002,8,1)
b=datetime(2018,7,31)    # last considered date (2020,3,31)

t_endedates,t_begin,AnzHist= a4.timeframes(a,b)

    
#%%
'''A dataframe which has columns rating_grade, valid from and to. In iteration 
     values in the order of i[0 ,1,2 ] will correspond respective columns od dataframe ''' 
   
dataframe=pd.DataFrame(df,columns=['valid_from','valid_to','rating_grade','rating_grade_pre'])
'''
 t_begin and t_enddates are parametrizable variables. 
 here the dates : 31.07.2018 and 31.07.2018 were 
 chosen fro  end date and begin date
  one can make a loop through enddates and begin dates 
  in t  and save i th rating reports in separte dicts   
'''
AnzHist=13
sortedshort1={}
shorted21={}
shorted22={}
smort={}   
for i in range (0,AnzHist):
    #shorted21[i]=dataframe[(dataframe.valid_from<=t_endedates[i+1])]
    shorted21[i]=dataframe[(dataframe.valid_to>t_endedates[i+1])\
                &(dataframe.valid_from<=t_endedates[i+1])]
    
    smort[i]= dataframe[(dataframe.valid_to>t_endedates[i+1])\
            &(dataframe.valid_from<=t_endedates[i+1])\
            &(dataframe.rating_grade<22)]
 
    shorted22[i]=dataframe[(dataframe.valid_from<=t_endedates[i+1])]    
    
#    shorted22[i]=dataframe[(dataframe.valid_to>t_begin[i+1])
#                &(dataframe.valid_from<=t_endedates[i+1])]
    print(t_endedates[i+1],t_begin[i+1])
    
    

 #%%
# from aa01
    
countt=a1.rating_counter(shorted21)

plot=a1.plot_barchart(countt,t_endedates)

val1=a1.reporting_0(countt)

val2=a1.reporting_1(countt,t_endedates)          

val3,val4=a1.reporting_2(countt,smort, t_endedates,AnzHist) 

#%%

# from aa02
val5=a2.matrix_tabelle(shorted22,AnzHist,t_endedates,t_begin)[0] 

val6,val7=a2.cum_matrix(val5,AnzHist)
    
val8,val9=a2.rating_change(shorted22,AnzHist,t_endedates,t_begin)



#for i in range (0, AnzHist):
#    print(sum(val6[i].iloc[25:26,0:26].sum()))    
    
#%%
val10=a3.summary_tabelle(val6,val7,val8,val9)    
va11=a3.expired_ratings(shorted21)
    
           
    #%%

    
    


