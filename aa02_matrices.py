# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:22:48 2020

@author: U0047365
"""
def matrix_tabelle(dataframe,AnzHist,enddates,begindates):
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
    import aa05_matrix_bilder as f0
    
    # Teile Tabellenblatt B6:AD3000
    
    refresh.reload(f0)

    shorted22={}
    t_begin=begindates
    t_endedates=enddates  
    for i in range (0,AnzHist):     
        shorted22[i]=dataframe[(dataframe.valid_from<=t_endedates[i+1])]    
        
    vert_4=dict()
    
    global vert_44
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
def cum_matrix(output_from_matrix_tabelle,AnzHist):
    
    """
    Uses first  argument of matrix_tabelle(),i.e matrix_tabelle()[0] 
    to compound the sum of rating amount in the matrix. 
    AnzHist is integer  defines the length of analysis.
    Retunrs to tw0 dicted arguments, the second arguments consists of matrices
    with [1 month 3 month and 1 year] timeframe.

    """
    import pandas as pd
    vert_5=output_from_matrix_tabelle
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
               c=last.add(i) # cummulates previous result 
               vert_6[s]=c
               last=c      
               
    result4={} 
    selection2=[1,3,11]  #  choose the results
    for key ,i in vert_6.items():
        if key in selection2 :
            result4[key]=i # 1 month, 3 months and 1 year 
        
    return vert_6, result4
    

  
#%%    
  
def rating_change (AnzHist):
    """
    Uses the  module function_0.py
    Creates results of migrated ratings withing given timeframes 
    Retuns to two dicted arguments, the second argument is cummulative mugrated
    ratings 
    the outputs are used for further calculations
    
    """
      
    # rating's change current rating vs. previous rating 
    import pandas as pd
    import aa05_matrix_bilder as f0
    import importlib as load
    load.reload(f0)

    
    
    vert_55=dict()      
    last=pd.DataFrame(0,columns=['re-rating (excl.defaults)'],index=range(0,11))
    last.index=[\
            '<=-5','-4 ','-3 ','-2','-1','0', '1','2','3','4','>=5']
    global vert_44
    for k, i in  vert_44.items():
        if isinstance (i,pd.DataFrame) is False:
            print("-- The  type of variable must be pd.DataFrame --")
            return 
        
        elif i.empty==True:
            enter1=pd.DataFrame(0,columns=['re-rating (excl.defaults)'],\
            index=range(0,11))
            enter1.index=[\
            '<=-5','-4 ','-3 ','-2','-1','0', '1','2','3','4','>=5']
            vert_55[k]=enter1

        else:
            enter=i.iloc[:,2:4]
            s=f0.abwechslung(enter,include_5_notch=True) 
            
            summy=last.add(s)
            vert_55[k]=summy
            last+=s 
  
   
   # for set up the tablle 
    ordered={}  
    smm={}
    smend={}
    ress={}
    migrated_perf={}
    for i in range(1,AnzHist):
        ordered[i]=vert_55[i-1].iloc[6:10,:]
        smm[i]=vert_55[i].iloc[0:6,:]
        smend[i]=vert_55[i].iloc[10:11,:]
    
        ress[i]=pd.concat([smm[i],ordered[i],smend[i]])  
        migrated_perf[i]=ress[i]['re-rating (excl.defaults)'].sum()\
        -ress[i].iloc[5,:]            

    result6=[]    
    selection3=[1,3,11]   # last, 3 months  and one year range 
    for k,i in enumerate(selection3):
        result6.append(migrated_perf[i][0])
    
    return ress,migrated_perf


if __name__=='__main__':
    matrix_tabelle()
    cum_matrix()
    rating_change()
    

    
print("Completed.")    
    
    
    
    
