import gensim
from scipy.spatial.distance import cosine, euclidean
import  numpy as np
model = gensim.models.Word2Vec.load("w2v_farsi.model")

data=[]
groundTruth=[]
with open("data.csv","r",encoding="UTF-8")as f:
    for line in f:
        row = []
        line=line.split(",")
        row.append(line[1])
        row.append(line[2])
        row.append(line[3])
        groundTruth.append(line[4])
        data.append(row)

j=0
tp=0
for row in data:
    i=0
    for w in row:
        try:
            if i==0:
                A=model.wv[w]
            if i==1:
                B=model.wv[w]
            if i==2:
                C=model.wv[w]
            i+=1
        except:
            if  i==0:
                A=0
            if i==1:
                B=0
            if  i==2:
                C=0
            i+=1
        
    if (A is not 0) and (B is not 0)and(C is not 0):
        mi=np.subtract(B,A)
        s=np.add(mi,C)
        most_similars=model.similar_by_vector(s,topn=10)

        for word in most_similars:
            if (groundTruth[j].strip() is word[0].strip()):
                print('ghj')
                tp+=1

    j+=1


print('accuracy = ', tp/len(data))