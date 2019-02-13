import tf_glove
from hazm import *
import re

def process_text(text):
    normalize=Normalizer()
    text=normalize.normalize(text)

    text = text.replace(',', ' ')
    text=text.replace("\u220c","")
    text=text.replace("\u200c","")
    text=text.replace("-","")
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text=text.replace("«"," ")
    text=text.replace("»"," ")
    # Convert text string to a list of words

    token=WordTokenizer()
    t=token.tokenize(text)

    text=t
    return text

def load_data(path):
    data=[]
    token_set = set()

    with open(path,"r",encoding="UTF-8") as f:
        text=f.readlines()
        for line in text:
            l=process_text(line)
            data.append(l)
            for term in l:
                token_set.add(term)

    return data, token_set

def build_model(corpus):
    model = tf_glove.GloVeModel(embedding_size=300, context_size=10)
    model.fit_to_corpus(corpus)
    model.train(num_epochs=100)
    model.generate_tsne()

    return model

data, token_set = load_data("testSet.txt")
model =build_model(data)

writer=open("glove_vector.txt","w",encoding="UTF-8")

for t in token_set :
    p=model.embedding_for(t)
    writer.write(t+":"+str(p)+"\n")