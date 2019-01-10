# Analogy results for gensim skipgram model

trained on : wikipedia corpus

for now, we trained these three model:

Model1: 
VectorSize 100
WindowSize 3
MinCount 3 
Alpha 0.025

Model2: 
VectorSize 100
WindowSize 3
MinCount 3 
Alpha 0.012

Model3: 
VectorSize 200
WindowSize 3
MinCount 3 
Alpha 0.012


Model4: 
VectorSize 200
WindowSize 3
MinCount 3 
Alpha 0.025

Model5: 
VectorSize 300
WindowSize 3
MinCount 3 
Alpha 0.012

i think in this test, model 1 is better than the others, but all of them, have bad results! (maybe there is bug in test code or size of windowSize for example, we are training different model and check the effect of this parameter)

result of these five model over analogy_test, are in <model_name>.csv files.
