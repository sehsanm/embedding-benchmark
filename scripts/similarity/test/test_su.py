import SimilarityUtil as su
import LoadModel 

my_w2v = LoadModel.W2V.from_W2V("mymodel")    # mymodel file is a word2vec file placed inside this directory
result = su.correlation_coefficient("sim_test.csv", my_w2v, [3,4])  # sim_test.csv placed inside this directory
print(res)
# The result should be [-1.0, 0.8660254037844387]
