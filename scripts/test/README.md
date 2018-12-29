# Test scripts for evaluating embedding models

## analogy test

one of the methods for evaluating each embedding model is analogy test. each analogy question contains  a complete pair of related words and an incomplete pair which you should complete it . for example : (Iran,Tehran) and (England,?) . if an embedding model is representative it should answer such a question. 

analogy questions are under two main categories : semantic and syntactic . and each category divided into many categories.in our  analogy test set under data/analogy directory you can find questions in CVS format which first columns is dedicated for category. like the one in below:

syntactic-pastverb, می رفت,رفت,می خورد,خورد

for solving analogy questions first of all we should get corresponding vector of each word in question like : v1,v2 and v3 .then we find nearest word-vector to v3+v2-v1.


for evaluating method we find k nearest vectors to v3+v2-v1 and we check existence of reference answer(answer in analogy test)in those k words. 

you can run test by : `python3 -m scripts.test.analogy_test -m batch -t 100 -i data/model/sample.vec`

options discriptions can be find by : `python3 -m scripts.test.analogy_test -h`

for now similarity.getKnear() implement finding k nearest vectors based on cosine , euclidean  and pair direction distances . but it is not a efficient method because it compute distance of each word in vocabulary by vector d(which for each question equal to v3+v2-v1).

similarity.getKnearBatch() implement finding k nearest vectors just based on cosine distance. the method is expected to be fast because of using matrix multiplication to compute distances. but it is not efficient in memory usage since it should load all of the model (with size of 1-4G). the problem seems be solved in https://github.com/kudkudak/word-embeddings-benchmarks/blob/master/web/analogy.py. they solve the problem by defining each batch as small subset of model like 300 vector in each batch and they find nearest vector in each batch to (v3+v2-v1) and they report that.so if we want k nearest vector we can divide our model to len(model.vectors)/k batches and find the nearest vector in each batch.
