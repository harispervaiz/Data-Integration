from __future__ import division
import pandas as pd
import numpy as np

import re


im= pd.read_csv("./imdb.csv");
rt= pd.read_csv("./rotten_tomatoes.csv");
print('The imdb shape: %d x %d' % im.shape)
print('The rt shape: %d x %d' % im.shape)


# In[3]:

#Split words in the n-grams
def ngrams(string, n=2):
    string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]

#Not used...
def split_ngram(string,n=2):
        """Normalize string and split in n-grams constaing n characters."""
        string_ = string.lower()
        string = [string_[i:i+n] for i in range(0, len(string_), n)]
        return string
    

def dice_coefficient(a, b,n=2):
    """dice coefficient 2nt/na + nb."""
    
    #For comparing strings 
    if isinstance(a,str) & isinstance(b,str):
        a = split_ngram(a,n)
        b = split_ngram(b,n)
        
    #For comparing lists  
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return overlap * 2.0/(len(a_bigrams) + len(b_bigrams))


# 
# ## General Truth


#Ibmd : RottenTomatoes
GT = {
      "Name":"Name",
      "ReleaseDate":"Release Date",
      "RatingValue":"RatingValue",
      "Director":"Director",
      "Creator":"Creator",
      "YearRange":"Year",
      "Genre":"Genre",
      "Duration":"Duration",
      "Cast":"Cast",
      "Description":"Description"
     }


# In[ ]:




# ## Label Based Mapping
# 
# **get_mapping** is the main function of the algortihm. It takes two data tables (padans DataFrame) and a treshold value for the N-Grams computed using Dice Score.

# In[15]:

def get_mapping(table_a,table_b,treshold=0.5,n=2):
    #print("Treshold: {}, {}-grams".format(treshold,n))
    A =[ str(a) for a in table_a.columns]
    B =[ str(b) for b in table_b.columns]
    #HardCoded skiping IDs
    A.remove('Id')
    B.remove('Id')
    #List of arrays containg header label and it's Ngram represatantion,
    rt_cl = [[ngrams(cl,n),cl]for cl in A]
    im_cl = [[ngrams(cl,n),cl] for cl in B]
    df = pd.DataFrame(columns=["tab_a_entry","tab_b_entry","coeff"])
    for r,r_ in rt_cl:
        for i,i_ in im_cl:
            dc = dice_coefficient(r,i)
            print([r_, i_, dc])

            if (dc >= treshold ) or (r_ in i_):
                df = df.append(pd.Series([r_,i_,dc],index=["tab_a_entry","tab_b_entry","coeff"]),ignore_index=True)
    # tresh = df.loc[df['coeff'] >= treshold];
    #print(tresh)
    print(df.to_csv())
    df = df.groupby(['tab_a_entry'], sort=True)['tab_a_entry','tab_b_entry','coeff'].max()
    return dict(zip(df["tab_b_entry"],df['tab_a_entry']))



def compute_recall(mapping):
    total_found =len(mapping.items())
    #print("Recall {}".format(float(total_found/len(GT.items()))))
    return float(total_found/len(GT.items()))
                 
def compute_precision(mapping):
    precision = set(mapping.items()) & set(GT.items())
    true_matches = len(precision)
    total_found =len(mapping.items())
    #print("Precision {}".format(float(true_matches/total_found)))
    return float(true_matches/total_found)

test_mapping = get_mapping(rt,im,0.7)

compute_precision(test_mapping)
compute_recall(test_mapping)


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def what_is_missing_or_wrong(mapping):
    missing = list()
    for x in GT.items():
        try:
            mapping= removekey(mapping,x[0])
        except KeyError as e:
            #print("Missing : "+x[0])
            missing.append(x)
                        
    #print("Wrong:",[pair[0] for pair in mapping])        
    return {"Missing":missing, "FalsePositives":mapping}






# In[13]:

def test_algo(tableA,tableB,to_csv=False):
    treshold_test_axis = np.arange(0.001, 1, .03);
    ngram_test_axis = np.arange(1,5)

    df = pd.DataFrame(columns=["treshold","ngrams","precision","recall","total_matches","uniqie_matches"])
    for t in treshold_test_axis:
        for n in ngram_test_axis:
            #(t,n)
            mp =get_mapping(tableA,tableB,t,n)
            prec =compute_precision(mp)
            recall= compute_recall(mp)
            unique = set(mp.items())
            df = df.append(pd.Series([t,n,prec,recall,len(mp.items()),len(unique)],index=["treshold","ngrams","precision","recall","total_matches","uniqie_matches"]),ignore_index=True)
    df['precision_normalised']=(df['precision'] - df['precision'].mean()) / (df['precision'].max() - df['precision'].min())
    df['recall_normalised']=  (df['recall'] - df['recall'].mean()) / (df['recall'].max() - df['recall'].min())
    if to_csv:
        df.to_csv('test.csv')
    return df


# In[14]:

#test_ = test_algo(rt,im,True)


# In[ ]:

print(what_is_missing_or_wrong(test_mapping))



# In[218]:




# In[219]:

#test_.to_csv("test.csv")


# In[ ]:



