import datasets
import similarity

print(datasets.loadAnalogyDataset("data/analogy"))


print(similarity.cosinDistance([1,1],[1,0])) # it should be equal to cos(pi/4)=0.70710
