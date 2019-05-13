#!/usr/bin/env python
# coding: utf-8

# 

# In[33]:


import csv
import pandas as pd
import networkx as nx
from collections import defaultdict


# In[34]:


def sign_out_degree(G, e_sign):
    outdegree = defaultdict(int)
    for u,v in ((u,v) for u,v,d in G.out_edges(data=True) if d['sign']==e_sign):
        outdegree[u]+=1
    return outdegree


# In[35]:


def sign_in_degree(G, e_sign):
    indegree = defaultdict(int)
    for u,v in ((u,v) for u,v,d in G.in_edges(data=True) if d['sign']==e_sign):
        indegree[v] +=1
    return indegree


# In[36]:


def total_out_degree(G):
    outdegree = defaultdict(int)
    for i, j in G.out_degree():
        outdegree[i] = j
    return outdegree

def total_in_degree(G):
    indegree = defaultdict(int)
    for i, j in G.in_degree():
        indegree[i] = j
    return indegree


# In[27]:


data = []
in_txt = csv.reader(open("data/epinions.txt", "r"), delimiter = '\t')
for row in in_txt:
        data.append(tuple(row))
   
df1 = pd.DataFrame(data, columns = ['u', 'v','sign']) 
G_epinions = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign', create_using=nx.DiGraph())
G_Und_epinions = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign')

pos_out = sign_out_degree(G_epinions, '1')
neg_out = sign_out_degree(G_epinions, '-1')

pos_in = sign_in_degree(G_epinions, '1')
neg_in = sign_in_degree(G_epinions, '-1')

total_out = total_out_degree(G_epinions)
total_in = total_in_degree(G_epinions)

ds = [total_out, total_in, pos_in, neg_in, pos_out,neg_out]
my_dict = {}

for k in total_out.keys():
  my_dict[k] = tuple(my_dict[k] for my_dict in ds)

with open('nodes_features_epinions.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in my_dict.items():
       writer.writerow([key, value])


# In[28]:


data = []
in_txt = csv.reader(open("data/slashdot.txt", "r"), delimiter = '\t')
for row in in_txt:
        data.append(tuple(row))
   
df1 = pd.DataFrame(data, columns = ['u', 'v','sign']) 
G_slashdot = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign', create_using=nx.DiGraph())
G_Und_slashdot = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign')

pos_out = sign_out_degree(G_slashdot, '1')
neg_out = sign_out_degree(G_slashdot, '-1')

pos_in = sign_in_degree(G_slashdot, '1')
neg_in = sign_in_degree(G_slashdot, '-1')

total_out = total_out_degree(G_slashdot)
total_in = total_in_degree(G_slashdot)

ds = [total_out, total_in, pos_in, neg_in, pos_out,neg_out]
my_dict = {}

for k in total_out.keys():
  my_dict[k] = tuple(my_dict[k] for my_dict in ds)

with open('nodes_features_slashdot.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in my_dict.items():
       writer.writerow([key, value])


# In[30]:


data = []
in_txt = csv.reader(open("data/wiki-utf.txt", "r"), delimiter = '\t')

v = ""

for row in in_txt:
    if(len(row)!=0 and row[0]=='U'):
        v = row[1]
        
    if(len(row)!=0 and row[0]=='V'):
        newuple = (row[2],v,row[1])
        data.append(newuple)
        
df1 = pd.DataFrame(data, columns = ['u', 'v','sign']) 

G_old_wiki = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign', create_using=nx.DiGraph())
G_Und_old_wiki = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign')

pos_out = sign_out_degree(G_old_wiki, '1')
neg_out = sign_out_degree(G_old_wiki, '-1')

pos_in = sign_in_degree(G_old_wiki, '1')
neg_in = sign_in_degree(G_old_wiki, '-1')

total_out = total_out_degree(G_old_wiki)
total_in = total_in_degree(G_old_wiki)

ds = [total_out, total_in, pos_in, neg_in, pos_out,neg_out]
my_dict = {}

for k in total_out.keys():
  my_dict[k] = tuple(my_dict[k] for my_dict in ds)

with open('nodes_features_oldwiki.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in my_dict.items():
       writer.writerow([key, value])


# In[39]:


data = []
in_txt = csv.reader(open("newwiki_edgelist.csv", "r"))
for row in in_txt:
        data.append(tuple(row))
   
df1 = pd.DataFrame(data, columns = ['u', 'v','sign']) 

G_new_wiki = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign', create_using=nx.DiGraph())
G_Und_new_wiki = nx.from_pandas_edgelist(df1, 'u', 'v', 'sign')

pos_out = sign_out_degree(G_new_wiki, '1')
neg_out = sign_out_degree(G_new_wiki, '-1')

pos_in = sign_in_degree(G_new_wiki, '1')
neg_in = sign_in_degree(G_new_wiki, '-1')

total_out = total_out_degree(G_new_wiki)
total_in = total_in_degree(G_new_wiki)

ds = [total_out, total_in, pos_in, neg_in, pos_out,neg_out]
my_dict = {}

for k in total_out.keys():
  my_dict[k] = tuple(my_dict[k] for my_dict in ds)

with open('nodes_features_newwiki.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in my_dict.items():
       writer.writerow([key, value])


# In[14]:


def embeddedness(G):
    embeddedness = []
    for u,v in G.edges():
        embeddedness.append([u,v,str(len(list(nx.common_neighbors(G,u,v))))])
    return embeddedness


# In[ ]:


embedded = embeddedness(G_Und_epinions)

with open("edges_features_epinions.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["u", "v", "embeddedness"])
    writer.writerows(embedded)


# In[40]:


embedded = embeddedness(G_Und_slashdot)

with open("edges_features_slashdot.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["u", "v", "embeddedness"])
    writer.writerows(embedded)


# In[41]:


embedded = embeddedness(G_Und_old_wiki)

with open("edges_features_old_wiki.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["u", "v", "embeddedness"])
    writer.writerows(embedded)


# In[42]:


embedded = embeddedness(G_Und_new_wiki)

with open("edges_features_new_wiki.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["u", "v", "embeddedness"])
    writer.writerows(embedded)


# In[ ]:



