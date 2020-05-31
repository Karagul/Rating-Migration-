# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:22:48 2020

@author: U0047365
"""


#os.chdir("N:/506/5060/99 Sonstiges/Einarbeitung Sardor/Kopie.2019_LGD_Validierung/_Python/python_tool_Data.migration/Methoden Ratingreporting") 
def matrix_tabelle(dict_data_valid_from,AnzHist,enddates,begindates):
    """
    Creates matrix of previous ratings and current rating
    uses the module function_0, the location of this module should be
    explicitly defined in the main or in directory manager. 
    length of output variable depends on the AnzHist. 
    Returns to two arguments , the outputs is used for
    further funtions as input 
    """
    import importlib as refresh
    import pandas as pd    
    import function_0 as f0
    
    # Teile Tabellenblatt B6:AD3000
    
    refresh.reload(f0)
    shorted22=dict_data_valid_from
    t_begin=begindates
    t_endedates=enddates
    vert_4=dict()
    vert_44={}
    for i in range(0,AnzHist):
        
        rating=shorted22[i]
        vert_4[i]=rating[(rating.valid_from >= t_begin[i+1])\
        &(rating.valid_from <=t_endedates[i+1])]
        
        vert_44[i]=rating[(rating.valid_from >= t_begin[i+1])\
        &(rating.valid_from <=t_endedates[i+1])&(rating.rating_grade<22)\
        &(rating.rating_grade_pre<22)]
    
    vert_5=dict()
    
    for k, i in vert_4.items():
        if isinstance (i,pd.DataFrame) is False:
            print("-- The  type of variable must be pd.DataFrame --")
            break #return 
        
        elif i.empty==True:
            
            vert_5[k]=pd.DataFrame(0,index=range(0,28),\
            columns=range(0,28))
        else:
            #vprev=pd.DataFrame()
            enter=i.iloc[:,2:4] # chooses colums: rating_grade and rating_grade_pre
            vert_5[k]=f0.migmatrix(enter,include_25th_class=True)
            
    names=['0','1','2','3','4','5','6','7','8','9',\
            '10','11','12','13','14','15','16','17',\
            '18','19','20','21','22','23','24','25',\
            'unrated', 'Sum'] 
    for i in vert_5.values():
        i.columns=names
        i.index=names   
    
    return vert_5,vert_44


    
#%%
def cum_matrix(outout_from_matrix_tabelle,AnzHist):
    
    """
    Uses first (means 0) argument of matrix_tabelle() to compound the sum of 
    rating amount in the matrix. 
    AnzHist is integer  defines the length of analysis.
    Retunrs to tw0 dicted arguments, the second arguments consists of matrices
    with 1 month 3 month and 1 year timeframe.
    
    """
    import pandas as pd
    vert_5=outout_from_matrix_tabelle
         #sum each matrix
    names=['0','1','2','3','4','5','6','7','8','9',\
            '10','11','12','13','14','15','16','17',\
            '18','19','20','21','22','23','24','25',\
            'unrated', 'Sum']     
    vert_6={}
    last=pd.DataFrame(0,index=range(0,28),columns=range(0,28))
    last.columns=names
    last.index=names
    for k, i in vert_5.items():  
       for s in range(0,AnzHist):
           if s==k:
               c=last.add(i)
               vert_6[s]=c
               last=c      
               
    result4={} 
    selection2=[0,1,3,11]  #  choose the results
    for key ,i in vert_6.items():
        if key in selection2 :
            result4[key]=i # result4  1 month, 3 months and 1 year 
        
    return vert_6, result4
    

  
#%%    
  
def rating_change (dict_data_valid_from,AnzHist,enddates,begindates):
    """
    Uses the  module  (function_0.py) and function matrix_tabelle()
    Creates results of migrated ratings withing given timeframes 
    Retuns to two dicted arguments, the second argument is cummulative mugrated
    ratings 
    the outputs are used for further calculations
    
    """
      
    # rating's change current rating vs. previous rating 
    import pandas as pd
    import function_0 as f0
    vert_44=matrix_tabelle(dict_data_valid_from,AnzHist,\
    enddates,begindates)[1]
    
    vert_55=dict()      
    last=pd.DataFrame(0,columns=['Anzahl'],index=range(0,11))
    last.index=[\
        'Verschlechterung um mind. 5 Klassen','Verschlechterung um mind. 4 Klassen',\
        'Verschlechterung um mind. 3 Klassen','Verschlechterung um mind. 2 Klassen',\
        'Verschlechterung um mind. 1 Klasse','Gleichheit', \
        'Verbesserung um 1 Klasse','Verbesserung um 2 Klassen',\
        'Verbesserung um 3 Klassen','Verbesserung um 4 Klassen','Verbesserung um 5 Klassen']
    for k, i in  vert_44.items():
        if isinstance (i,pd.DataFrame) is False:
            print("-- The  type of variable must be pd.DataFrame --")
            return 
        
        elif i.empty==True:
            enter1=pd.DataFrame(0,columns=['Anzahl'],index=range(0,11))
            enter1.index=[\
        'Verschlechterung um mind. 5 Klassen','Verschlechterung um mind. 4 Klassen',\
        'Verschlechterung um mind. 3 Klassen','Verschlechterung um mind. 2 Klassen',\
        'Verschlechterung um mind. 1 Klasse','Gleichheit', \
        'Verbesserung um 1 Klasse','Verbesserung um 2 Klassen',\
        'Verbesserung um 3 Klassen','Verbesserung um 4 Klassen','Verbesserung um 5 Klassen']
            vert_55[k]=enter1

        else:
            enter=i.iloc[:,2:4]
            s=f0.abwechslung(enter,include_5_notch=True) 
            
            summy=last.add(s)
            vert_55[k]=summy
            last+=s 

        # last, 3 months  and one year range
    result5={}       
    selection2=[0,1,3,11]    
    for i in selection2:
        result5[i]=vert_55[i]
        
    migrated_perf={}
    for  i in range(0,AnzHist-1):
        migrated_perf[i]=((vert_55[i+1]['Anzahl']\
        [:6].sum()+vert_55[i]['Anzahl'][6:10].sum()\
        +vert_55[i+1].loc['Verbesserung um 5 Klassen'])\
        -vert_55[i+1].loc['Gleichheit'])
        
    result6={}       
    selection3=[0,1,3,10]   # last, 3 months  and one year range 
    for k,i in enumerate(selection3):
        result6[k]=migrated_perf[i]
    
    
    return vert_55, result6

#%%


if __name__=='__main__':
    matrix_tabelle()
    cum_matrix()
    rating_change()
    

    
print("Completed.")    
    
    
    
    