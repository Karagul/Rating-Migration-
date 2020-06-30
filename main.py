# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:22:11 2020

@author: Sardor Mirzaev
"""
import os
# directory where datas are located 
os.chdir("N:Einarbeitung Sardor/Kopie.2019_LGD_Validierung/_Python")

import pandas as pd
from datetime import datetime, timedelta, date
import numpy as np
import aa01_start as a1
import aa02_matrices as a2
import aa03_summaries as a3
import aa04_helper as a4
import importlib as load


#%%
############################################## 

import1= 'MigrationenTool TRO v_2019(1)_eng.xlsx' # Choose data 
###############################################

#%%
print("Loading  the required datasets...")
df=pd.read_excel(import1,'Daten aufbereitet',encoding='utf-8', index=True)
print("Loading is completed.")
 #%%
a=datetime(2002,8,1)     # first considered date 
b=datetime(2018,7,31)    # last considered date 

t_endedates,t_begin,AnzHist= a4.timeframes(a,b)

    
#%%
'''A dataframe which has columns rating_grade, valid from and to. In iteration 
     values in the order of i[0 ,1,2 ] will correspond respective columns of 
     dataframe ''' 
      
dataframe=pd.DataFrame(df,columns=['valid_from','valid_to','rating_grade','rating_grade_pre'])

AnzHist=13 # for simplicity 13 timeframes (months) instead 192, were taken 

 #%%
# from aa01
load.reload(a1)
# Verlauf  A8:N31- counts the total ratings in ratingsclasses, 
# counts the total sum of ratings AA129 AA170, AA217

countt,countt_2 = a1.rating_counter(dataframe,13,t_endedates) 
# in VBA summation function is incorrectly implemented 

# Report L22: AF30 - plots the destibutuion of ratings in two timeframes  
plot_report_page1=a1.plot_barchart(countt,t_endedates)


# Report G18:AF20
rating_dist=a1.rating_grade_report(countt)

# Report G22:K24
amount_perf=a1.ref_date_report(countt,t_endedates)          


# Report G26:K28, # Report G30:K30
total_perfm_nonperfm,age_ratings=a1.total_perfm_nonperfm(countt,dataframe, t_endedates,AnzHist)  

#%%
load.reload(a2)
# from aa02
# Teile A6:AD2000
matrices_nested=a2.matrix_tabelle(dataframe,AnzHist,t_endedates,t_begin)[0] 
#val5
# Cummulative sum of matrices , Report G8, G139,G189 matrix 
cum_all,for_report=a2.cum_matrix(matrices_nested,AnzHist)


#Report  K132:U134, H130, 
all_up_down,hilf_wert=a2.rating_change(AnzHist)

    
#%%
    
# from aa03
#Reprot G33:U36
load.reload(a3)
#Reprot G33:U36 if in_first_page=True)
changes,changes_percent=\
a3.summary_tabelle(cum_all,for_report,all_up_down,hilf_wert,in_first_page=True)

#Reprot H129:U130 if for_report=True) returns to nested dataframes 
#in last, 3 months  and one year range
changes_each ,changes_each_percent=a3.summary_tabelle(cum_all,\
for_report,all_up_down,hilf_wert,in_first_page= False)

#Report W33:Y36
expired_ratings=a3.expired_ratings()
for k,i in expired_ratings.iterrows():
    print(i) # returns to each expired ratings in last ( W130 ), 3 months  and one year range 
     
#%%
##from aa04
load.reload(a4)

#Report  T39:Z42  
# returns to each expired ratings in last month, last 3 months  and one year range

exclude_def,exclude_def_4,down_up_grades =a4.migrated_alives(cum_all,all_up_down,AnzHist)










