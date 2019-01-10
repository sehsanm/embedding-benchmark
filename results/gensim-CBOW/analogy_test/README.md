# Analogy results for gensim SBOW model

trained on : wikipedia corpus

for now, we trained these three model:

Model1: 
VectorSize 200
WindowSize 3
MinCount 3 
Alpha 0.012

Model2: 
VectorSize 200
WindowSize 3
MinCount 3 
Alpha 0.025

Model3: 
VectorSize 300
WindowSize 3
MinCount 3 
Alpha 0.012

i think in this test, model 3 may be better than the others(a bit!), but all of them, have bad results! (maybe there is bug in test code or size of windowSize for example, we are training different model and check the effect of this parameter)

result of these three model over analogy_test, are in <model_name>.csv files.
