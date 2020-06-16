# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:23:54 2020

@author: U0047365
"""

def summary_tabelle(val6,val7,val8,val9,in_first_page):
    """
    This function should be executed after input variables habe been  defined 
    from modules "aa01.py","aa02.py".
    Creates a table for reporting 
    """
    
    import pandas as pd 
    selection2=[1,3,11]  

    
    result4= val7
    result5= val8
    result6=val9
    vert_6=val6
    
    #  in Numbers 
    approved=[result4[i].loc['Sum'].sum() for i in selection2]
    unchanged=[result5[i].loc['0'] for i in selection2]
    
    samp_proz={}
    for i in selection2:
        samp_proz[i]=(result5[i].loc['0']/result4[i].loc['Sum'].sum())
    
    proved=list(approved)
    proz={}     
    for key,i in samp_proz.items():
        proz[key]=i.fillna('-')
            
    proz2={}     
    for key,i in result6.items():
        proz2[key]=i.fillna('-')
        
    xas=[]
    for k,i in proz2.items():
        if k in selection2:
            xas.append(i[0])
    
    perf_proz=['-'  if xas[i] ==0 else xas[i]/proved[i] for i in range(3)]

     
    unch=[i[0] for i in unchanged]
    mig_within=xas

    
    # migrated to default  
    
    to_def=[]
    to_rec=[]    
    conf_def=[]  
    new_ratings=[]  
    for k, i in vert_6.items():
        to_def.append(sum(i.iloc[:23,23:26].sum()))
        to_rec.append(sum(i.iloc[22:25,:22].sum()))
        conf_def.append(sum(i.iloc[22:25,22:25].sum()))
        new_ratings.append(sum(i.iloc[25:26,0:26].sum()))
        # print(i.iloc[0:26,27].sum())
        #default_rate_1Y.append(sum(i.iloc[0:23,23:26].sum())/x)
        #print(sum(i.iloc[0:26,25].sum()))   
      
   
    
    #  in Percentages 

    unchanged_prozent=["{:.2%}".format(i[0]) if i[0]!='-' else '-'\
    for  key, i in proz.items()]
        
    migrated_perf_proz=["{:.2%}".format(i) if type(i)!=str else '-'  \
    for i in perf_proz]
   
    mig_to_def=[]
    mig_to_rec=[]
    for i in [1,3,12]:
        mig_to_def.append(to_def[i])
        mig_to_rec.append(to_rec[i])
    
    global  new_ratings_proz  #allows to call this variable in another funciton
    
    new_ratings_proz=[new_ratings[i]for i in selection2]     

    
        
    mig_to_def_proz=["{:.2%}".format(i/proved[k]) if i!=0 else \
    '-' for k,i in enumerate(mig_to_def)]
          
    mig_to_rec_proz=["{:.2%}".format(i/proved[k]) if i!=0 else \
    '-' for k,i in enumerate(mig_to_rec)]
    
    conf_def_proz=[conf_def[i] for i in selection2]
    mig_conf_def_proz=["{:.2%}".format(i/proved[k]) if i!=0 else \
    '-' for k,i in enumerate(conf_def_proz)]
    
    mig_new_ratings_proz=["{:.2%}".format(i/proved[k])if i!=0 else \
    '-' for k,i in enumerate(new_ratings_proz)]


    result10=pd.DataFrame(list(zip(proved,unch,mig_within, mig_to_def,\
    mig_to_rec, conf_def_proz,new_ratings_proz)),\
    columns=['# approved ',\
    '# confirmed (unchanged)','# migrated within performing',\
    '# migrated to default (to non performing)', '# recovered',  \
    '# confirmed as default','# new (no active ratings existed before)'])
        
    result10.index=['last month','last 3 months','last 12 months']
    
    result11=pd.DataFrame(list(zip(unchanged_prozent, migrated_perf_proz,mig_to_def_proz,mig_to_rec_proz,\
     mig_conf_def_proz,mig_new_ratings_proz)),\
     columns=[    '# confirmed (unchanged)','# migrated within performing',\
    '# migrated to default (to non performing)', '# recovered',  \
    '# confirmed as default','# new (no active ratings existed before)'])
    
    result11.index=['last month','last 3 months','last 12 months']
    

    if in_first_page is False: 
        result_t=dict()
        result_t2=dict()
        for i in range(0,len(result11)):
            result_t[i]=pd.DataFrame(result10.iloc[i,:]).T
            result_t2[i]=pd.DataFrame(result11.iloc[i,:]).T
            
        return result_t, result_t2
    else:
        return result10, result11
        
    #%%
def expired_ratings():
    """
    Uses the variable defined in summary_tabelle()
    Returns to the table of expired ratings (no direct followers exist)
    """
    import pandas as pd
    from aa01_start import rating_counter# call variable from aa01 module
    ss={}

    for  k,i in rating_counter.shorted21.items():
        ss[k]=len(i)
    
    sss=[abs(m-n) for m,n in zip(list(ss.values())[:-1],\
        list(ss.values())[1:])]
    
    sum(sss[0:3])
    global  new_ratings_proz
    a=[sss[0],sum(sss[0:3]),sum(sss)+int(new_ratings_proz[-1])]
    result02=pd.DataFrame(a, columns=['expired ratings (no direct followers exist)'])
    result02.index=['last month','last 3 months','last 12 months']
    
    return result02
 #%%
    
    
if __name__=='__main__':
    summary_tabelle()
    expired_ratings()    
print("Completed.")    
       
    
    
