import numpy as np
from math import sqrt
def _cosinDistance(v1,v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))

def _euclideanDistance(v1,v2):
    return np.linalg.norm(v1-v2)

# def PAIRDIRECTION():

def getKNear(r1,r2,r3,model,thershold,method):
    distances=[]
    if(method=="Cosine"):
        for vector,word in model.vectors():
            distances.append({'word':word,"distance":_cosinDistance(r3+r2-r1,vector)})
    elif(method=="Euclidean"):
        for vector,word in model.vectors():
            distances.append({'word':word,"distance":_euclideanDistance(r3+r2-r1,vector)})
    elif method=="PairDirection":
        for vector,word in model.vectors():
            distances.append({'word':word,"distance":_cosinDistance(r2-r1,vector-r3)})
    else:
        raise Exception("bad argument for getKNear function, method parameter can be one of these : Cosine,Euclidean,PairDirection")

        
    distances.sort(key=lambda d:d["distance"])
    result=[]
    for i in range(1,thershold):
        result.append(distances[len(distances)-i])
    return result