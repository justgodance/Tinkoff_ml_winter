#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse
import numpy


# In[45]:


def levenshtein(word1, word2):
    len1 = len(word1) + 1
    len2 = len(word2) + 1
    distances = numpy.zeros((len1, len2)) # создадим массивы дистанций
    for item1 in range(len1): #реализуем матрицу дистанций
        distances[item1][0] = item1
    for item2 in range(len2):
        distances[0][item2] = item2
    a = 0
    b = 0
    c = 0
    for item1 in range(1, len1): #заполняем матрицу дистанций
        for item2 in range(1, len2):
            if (word1[item1-1] == word2[item2-1]):
                distances[item1][item2] = distances[item1 - 1][item2 - 1]
            else:
                a = distances[item1][item2 - 1]
                b = distances[item1 - 1][item2]
                c = distances[item1 - 1][item2 - 1]
                if (a <= b and a <= c):
                    distances[item1][item2] = a + 1
                elif (b <= a and b <= c):
                    distances[item1][item2] = b + 1
                else:
                    distances[item1][item2] = c + 1 
    return distances[len1-1][len2-1] #наше искомое будет в самом краю матрицы


# In[46]:


def compare(word1,word2):
    length = max(len(word1), len(word2))
    return (1 - levenshtein(word1, word2) / length) * 100


# In[48]:


parser = argparse.ArgumentParser()
parser.add_argument('file1')
parser.add_argument('file2')
args = parser.parse_args()
with open(args.file1, 'r') as f:
    lines = f.readlines()
files = []
for line in lines:
    words = line.split()
    files += words
for i in range(1, len(files), 2):
    with open(files[i], 'r', encoding="utf-8") as f:
        text1 = f.read()
    with open(files[i - 1], 'r', encoding="utf-8") as f:
        text2 = f.read()
    with open(args.file2, 'a', encoding="utf-8") as f:
        f.write(str(compare(text1, text2)))
        f.write('\n')


# In[ ]:





# In[ ]:





# In[ ]:




