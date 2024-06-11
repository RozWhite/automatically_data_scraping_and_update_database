import pandas as pd 
import hashlib 
from datetime import datetime
import time 
from extract_Info_from_Urls import database, docs
from get_Trevisto_Urls import urls
from urllib.request import urlopen, Request 
import html2text
time=str(datetime.today().strftime('%Y_%m_%d'))
#print(urls)



#### read prev data 
df_pre = pd.read_csv("html_data/trevisto_monitoring_pre.csv",sep = ';')

#### read current data and store it as a csv file   #########
texts=[]
titles=[]
hashes=[]
#urls1=[]
for i in range(len(docs)):
    text=docs[i].page_content
    texts.append(text)
    currentHash = hashlib.sha224(text.encode('utf-8')).hexdigest()
    hashes.append(currentHash)
    title=docs[i].metadata['title'].replace("\r\n" , "")
    titles.append(title)
   #url=docs[i].metadata['source']
    #urls1.append(url)

#print(urls1)   
dict = {'url': urls ,'title':titles, f'text_{time}': texts, f'hash_{time}': hashes}
df_cur = pd.DataFrame(dict)
df_cur =df_cur.drop_duplicates(['title'], keep='last').reset_index(drop=True)
df_cur.to_csv('html_data/trevisto_monitoring_pre.csv',index=False,sep=";")


#### compare prev data with current
df_all =df_pre.merge(df_cur, how='outer', on='title')
name=list(df_all.columns)
df_all['all_matching'] = df_all.apply(lambda x: x[name[-4]] == x[name[-1]], axis = 1)
false=df_all.loc[df_all['all_matching'] == False]['url_x']
text=""
for l in range(len(false)):
    text += f"{false.values[l]}\n"
# print(false)
# print(text)
if not df_all['all_matching'].all():
        print (' We have False value !!')
        f = open(f"html_data/newData_{time}.txt", "w")
        f.write("This url(s) has been changed since last time:  \n" + text)# 'r' for reading and 'w' for writing
        #f.write("There is a new File:  " + f.name)    # Write inside file 
        f.close()
        database()

else:
    print(' all values are True!')
    f = open(f"html_data/allTrue_{time}.txt", "w")   # 'r' for reading and 'w' for writing
    f.write("There is a new File:  " + f.name)    # Write inside file 
    f.close()