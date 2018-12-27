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


    def getKNearBatch(X,model,thershold):
        V=model.vectors
        # X: matrice of questions. in each column  is a list of string  words w1,w2,w3.each row is 
        # a single query
        # model:word embedding model instance
        # thershold: for checking how target word is close to our answers 
        # method : Cosine,Euclidean,PairDirection

        # for cosine distance :
        A=np.array()
        B=np.array()
        C=np.array()
        if method=="Cosine":
            for w,i in enumerate(X[0]):
                A[i]=model.getVec(w)
            for w,i in enumerate(X[1]):
                B[i]=model.getVec(w)
            for w,i in enumerate(X[0]):
                C[i]=model.getVec(w)
            D=B-A+C
        
        # now D is a d(embedding dimension)xM(number of questions) matrice.
        # each row of D is a vector representing w2-w1+w3. we want to get cosine distance of each 
        # row by all vectors of vocabulary. the result should be a matrice by M(number of questions)xV(vocabulary size)
        # and then we select K minimum item of each row which make matrice to have MxK dimension.

        # for computing cosine distance first we should normalize all vectors. 
            nD=np.linalg.norm(D, axis=1)
            nV=np.linalg.norm(V, axis=1)
            R=np.multiply(nV,nD.T)
            R=np.sort(R,axis=1)
            return R[:,0:thershold]
        elif method=="PairDirection":
            for w,i in enumerate(X[0]):
                A[i]=model.getVec(w)
            for w,i in enumerate(X[1]):
                B[i]=model.getVec(w)
            for w,i in enumerate(X[0]):
                C[i]=model.getVec(w)
            B_A=B-A

            #we need to  subtract each row of C from each word in vocabulary. so the result 
            #whould be a cube with MxVxd dimension.
            V_C=numpnpy.array()
            for c,i in enumerate(C):
                for v,j in enumerate(V):
                    V_C[i][j]=v-c
            #now we should compute dot-product of B_A by each vector in V_C which give
            #a matice with MxV dimension
            #I have no idea how to compute it!
            return
        # elif method=="Euclidean":
        #     #I have no idea!
        #     return
        else:
            raise Exception("bad argument for getKNearBatch function, method parameter can be one of these : Cosine,Euclidean,PairDirection")


        

