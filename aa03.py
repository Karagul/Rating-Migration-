# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:23:54 2020

@author: U0047365
"""

def summary_tabelle(val6,val7,val8,val9):
    """
    This function should be executed after input variables habe been  defined 
    from modules "aa01.py","aa02.py".
    Creates a table for reporting 
    """
    # Table of summary 
    import pandas as pd 
    selection2=[0,1,3,11]  
    approved=[]
    unchanged=[]
    samp_proz={}
    migrated_perf_proz=[]
    result4= val7
    result5= val8
    result6=val9
    vert_6=val6
    for i in selection2:
        approved.append(result4[i].loc['Sum'].sum())
        unchanged.append(result5[i].loc['Gleichheit'])
        
        samp_proz[i]=(result5[i].loc['Gleichheit']\
                /result4[i].loc['Sum'].sum())
    proved=list(approved)
    proz={}     
    for key,i in samp_proz.items():
        proz[key]=i.fillna(0)
            
    proz2={}     
    for key,i in result6.items():
        proz2[key]=i.fillna(0)
    
    perf_proz={}
    for k,i in proz2.items():
        if i[0]==0: 
            perf_proz[k]=0
        else:
            perf_proz[k]=i[0]/approved[k]
    unch=[i[0] for i in unchanged]
    unchanged_prozent=["{:.2%}".format(i[0])  for i in proz.values()]
    migrated_perf_proz=["{:.2%}".format(i) for i in perf_proz.values()]
    mig_within=[i[0] for i in proz2.values()]
    
    
    # migrated to default 
    
    to_def=[]
    mig_to_def=[]
    to_rec=[]
    mig_to_rec=[]
    mig_to_def_proz=[]
    mig_to_rec_proz=[]
    conf_def=[]  
    new_ratings=[]  
    conf_def_proz=[] 
    summary_tabelle.new_ratings_proz=[] 
    mig_conf_def_proz=[]
    mig_new_ratings_proz=[]
    default_rate_1Y=[]
    for k, i in vert_6.items():
        to_def.append(sum(i.iloc[:23,23:26].sum()))
        to_rec.append(sum(i.iloc[22:25,:22].sum()))
        conf_def.append(sum(i.iloc[22:25,22:25].sum()))
        new_ratings.append(sum(i.iloc[25:26,0:26].sum()))
        #print(i.iloc[0:26,27].sum())
        #default_rate_1Y.append(sum(i.iloc[0:23,23:26].sum())/x)
            
      
        #print(sum(i.iloc[0:26,25].sum()))
    
    for i in [0,1,3,12]:
        mig_to_def.append(to_def[i])
        mig_to_rec.append(to_rec[i])
        
    for i in [0,1,3,11]:
        conf_def_proz.append(conf_def[i])
        summary_tabelle.new_ratings_proz.append(new_ratings[i])
        
        
        
    mig_to_def_proz=["{:.2%}".format(i/proved[k]) for k,i in enumerate(mig_to_def)]    
    mig_to_rec_proz=["{:.2%}".format(i/proved[k]) for k,i in enumerate(mig_to_rec)]
    
    mig_conf_def_proz=["{:.2%}".format(i/proved[k]) for k,i in enumerate(conf_def_proz)]
    mig_new_ratings_proz=["{:.2%}".format(i/proved[k]) for k,i in enumerate(summary_tabelle.new_ratings_proz)]   
    
    result10=pd.DataFrame(list(zip(proved,unch,mig_within, mig_to_def,mig_to_rec, conf_def_proz,summary_tabelle.new_ratings_proz)),columns=['# approved ','# confirmed (unchanged)',\
        '# migrated within performing','# migrated to default (to non performing)',\
        '# recovered',  '# confirmed as default','# new (no active ratings existed before)'])
        
    result10.index=['this month','last month','last 3 months','last 12 months']
    
    result11=result10.iloc[1:,:]
    
    
    return result11
    #%%
def expired_ratings(dataframe):
    """
    Uses the variable defined in summary_tabelle()
    Returns to the table of expired ratings (no direct followers exist)
    """
    import pandas as pd
    ss={}
    # expired ratings (no direct followers exist)
    shorted21=dataframe
    for  k,i in shorted21.items():
        ss[k]=len(i)
        #ss[k]=sum([a for a  in list(i.values())])
    
    sss=[abs(m-n) for m,n in zip(list(ss.values())[:-1],\
        list(ss.values())[1:])]
    
    sum(sss[0:3])
    a=[sss[0],sum(sss[0:3]),sum(sss)+int(summary_tabelle.new_ratings_proz[-1])]
    result02=pd.DataFrame(a, columns=['expired ratings (no direct followers exist)'])
    
    return result02
 #%%
    
    
if __name__=='__main__':
    summary_tabelle()
    expired_ratings()    
print("Completed.")    
    
    
    
    
    
    
    
    
    
    
    
    
    