
"""
    auther Mohamad M. Jafari

    This file contains a CLASS for loading and useing embedding models!

    Essential materials for dealing with [word2vec, gensim] models is implemented!

    There are some extra facilities to perform bunch of other operation on models,
     like reordering, changeing format and etc.
    
"""



import numpy as np
import pickle
import gensim
from numpy import dot
from numpy.linalg import norm
from random import choice
from string import ascii_lowercase
import io
class W2V():
    def __init__(self, vocabulary, vectors):
        self.vocabulary = vocabulary # list of vocab 
        self.vectors = np.asarray(vectors) # numpy array, each row contains one word vector 
                                           # (corresponding to vocab list)
        self._wordDict={vocabulary[i]:vectors[i] for i in range(0,len(vocabulary))}

    #    magic method for reach vector corresponding to word
    def __getitem__(self, index):
        return self.vectors[index,:]
    #   magic method of containing special word
    def __contains__(self, word):
        return word in self.vocabulary
    
    #    delition word
    def __delitem__(self, word):
        index = self.vocabulary.index(word)
        del self.vocabulary[index]
        self.vectors = np.delete(self.vectors, index, 0)
        
        #   length
    def __len__(self):
        return len(self.vocabulary)
    #   iterator
    def __iter__(self):
        for w in self.vocabulary:
            yield w, self[vocabulary.index(w)]


    def getVec(self,word):
        return self.wordDict[word]
    @property
    def words(self):
        return self.vocabulary   
    @property
    def wordDict(self):
        return self._wordDict   
    @property
    def shape(self):
        return self.vectors.shape

    def normalize_words(self, ord=2, inplace=False):
        if ord == 2:
            ord = None  # numpy uses this flag to indicate l2.
        vectors = self.vectors.T / np.linalg.norm(self.vectors, ord, axis=1)
        if inplace:
            self.vectors = vectors.T
            return self
        return W2V(vectors=vectors.T, vocabulary=self.vocabulary)
        
    def nearest_neighbors(self, word, k=1):
        if isinstance(word, str):
            assert word in self, "invalid word!"
            v = self.vocabulary.index(word)
            print(v)
        else:
            v = word
        dist = lambda v1, v2 : dot(v1, v2)/(norm(v1)*norm(v2))
        vectors = self.vectors
        distances = [dist(vectors[v,:], vectors[x,:]) for x in range(0, len(vectors))]
        return(sorted(distances, reverse=True)[1:1+k])
    @staticmethod
    def from_text(fname, encoding=False):
        words = []
        vectors = []
        if encoding:
            with open(fname, 'r', encoding="utf-8") as fin:
                for line in fin.readlines():
                    line = line.split(" ")
                    word, vector = line[0], [float(x) for x in line[1:]]
                    words.append(word)
                    vectors.append(vector)
            return W2V(vocabulary=words, vectors=vectors)
        else:    
            with open(fname, 'r') as fin:
                for line in fin:
                    line = line.split(" ")
                    try:
                        if(len(line)>0):
                            word, vector = line[0], [float(x) for x in line[1:]]
                    except:
                        print("error in loading model in modles.py by reading this ",line)
                        print("exited by error")
                        exit(0)
                    # word, vector = line[0], [float(x) for x in line[1:]]
                    words.append(word)
                    vectors.append(vector)
            return W2V(vocabulary=words, vectors=vectors)

    @staticmethod
    def fasttext_from_text(fname):
        words = []
        vectors = []
        fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
        n, d = map(int, fin.readline().split())
        data = {}
        for line in fin:
            tokens = line.rstrip().split(' ')
            words.append(tokens[0])
            vectors.append([float(t) for t in tokens[1:]])
            
        return W2V(vocabulary=words, vectors=vectors)
    @staticmethod
    def from_bin(fname):
    	model = gensim.models.KeyedVectors.load_word2vec_format(fname, binary=True)
#        to implement
    @staticmethod
    def to_word2vec(w, fname, binary=False):
        with open(fname, 'wb') as fout:
            header = "%s %s\n" % w.vectors.shape
            fout.write(header.encode("utf-8"))
            for word, vector in zip(w.vocabulary.words, w.vectors):
                if binary:
                    line = word.encode("utf-8") + b" " + vector.astype("float32").tostring()
                    fout.write(line)
                else:
                    line = "%s %s\n" % (word, ' '.join("%.15f" % val for val in vector))
                    fout.write(line.encode("utf-8"))

    @staticmethod
    def from_W2V(fname):
        with open(fname, 'rb') as fin:
            wtov = pickle.load(fin)
        vec, voc = wtov["vectors"], wtov["vocabulary"]
        return W2V(vocabulary=voc, vectors=vec)

    def save(self, fname):
        vec = self.vectors
        voc = self.vocabulary
        model = {"vectors":vec, "vocabulary":voc}
        with open(fname, 'wb') as fout:
            pickle.dump(model, fout, protocol=pickle.HIGHEST_PROTOCOL)

glove50dt = "glove.6B.50d.txt"
wikifab = "wiki.fa.bin"
googb = "GoogleNews-vectors-negative300.bin"

# w2vt = W2V.from_text(glove50dt, encoding=True)
# w2vt.save("test")
# w2vt = W2V.from_W2V("test")

#w2vb = W2V.from_bin(googb)
# print(w2vt.vocabulary[0])
# print(w2vt.vectors[0])
if __name__ == "__main__":
    vocab_size = 100
    embedding_dim = 300
    # create our simple test case!
    vocabulary = [''.join(choice(ascii_lowercase) for i in range(10))\
                  for j in range(0, vocab_size)]
    vectors = np.random.random((vocab_size, embedding_dim))
    # test our methods!
    my_w2v = W2V(vocabulary, vectors)
    my_w2v.save("model")
    my_w2v = W2V.from_W2V("model")
#    print(my_w2v[vocabulary.index(vocabulary[10])])
#    print(my_w2v.shape)
#    print(my_w2v.words)
    del my_w2v[vocabulary[10]]
    print(my_w2v.shape)
#    print(len(my_w2v))
#    for word, vector in my_w2v:
#        print(word, vector)
    tmp = my_w2v.vectors
    my_w2v.normalize_words(ord=2, inplace=True)
#    print(my_w2v.vectors==tmp)
    print(len(my_w2v.nearest_neighbors(vocabulary[3], k=10)))
    
