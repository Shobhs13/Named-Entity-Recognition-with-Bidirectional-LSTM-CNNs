import pandas as pd
import numpy as np

def read_dataset() :
    df = pd.read_csv('dataset/main_dataset.csv', encoding = "ISO-8859-1")
    df = df[:100000]
    df.head()
    df.isnull().sum()
    df = df.fillna(method='ffill')

    df['Sentence #'].nunique(), df.Word.nunique(), df.Tag.nunique()
    df1=df.groupby('Tag').size().reset_index(name='counts')

    class SentenceGetter(object):
        def __init__(self, data):
            self.n_sent = 1
            self.data = data
            self.empty = False
            agg_func = lambda s: [(w, p, t) for w, p, t in zip(s['Word'].values.tolist(), 
                                                            s['POS'].values.tolist(), 
                                                            s['Tag'].values.tolist())]
            self.grouped = self.data.groupby('Sentence #').apply(agg_func)
            self.sentences = [s for s in self.grouped]

        def get_next(self):
            try: 
                s = self.grouped['Sentence: {}'.format(self.n_sent)]
                self.n_sent += 1
                return s 
            except:
                return None

    getter = SentenceGetter(df)
    sentences = getter.sentences

    gsentence = []
    
    for sentence in sentences :
        arr = []
        for i in sentence:
            arr.append([i[0], i[2]])
        gsentence.append(arr)

    df = pd.read_csv('dataset/covid_dataset.csv', encoding = "ISO-8859-1")
    df.head()
    df.isnull().sum()
    df = df.fillna(method='ffill')

    list1 = df.values.tolist()
    list1 = list1[:30000]
    # print(len(list1))
    for i in list1:
        gsentence.append([i])
    df = pd.read_csv('dataset/accident_dataset.csv', encoding = "ISO-8859-1")
    df.head()
    df.isnull().sum()
    df = df.fillna(method='ffill')

    list1 = df.values.tolist()
    list1 = list1[:30000]
    # print(len(list1))
    for i in list1:
        gsentence.append([i])

    return gsentence

def test_dataset() :

    gsentence = []
    df = pd.read_csv('dataset/covid_dataset.csv', encoding = "ISO-8859-1")
    df.head()
    df.isnull().sum()
    df = df.fillna(method='ffill')

    list1 = df.values.tolist()
    list1 = list1[30000:]
    # print(len(list1))
    for i in list1:
        gsentence.append([i])
    df = pd.read_csv('dataset/accident_dataset.csv', encoding = "ISO-8859-1")
    df.head()
    df.isnull().sum()
    df = df.fillna(method='ffill')

    list1 = df.values.tolist()
    list1 = list1[30000:]
    # print(len(list1))
    for i in list1:
        gsentence.append([i])

    return gsentence

# read_dataset()
print(read_dataset())