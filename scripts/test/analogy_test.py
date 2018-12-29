from code.models import models
from code import datasets
from  code.analogy import similarity
from code.analogy.helpers import write_result_to_file
import numpy as np
import sys
def print_inplace(txt):
	sys.stdout.write("\r"+txt)
	sys.stdout.flush()
#set thershold
thershold=100
#load dataset
print_inplace("loading analogy dataset...")
analog_datasets=datasets.loadAnalogyDataset('data/analogy')
print_inplace("analogy dataset loaded.")
#load model
print_inplace("loading embedding model ...")
# model = models.W2V.from_text('data/models/sample.vec')
model = models.W2V.fasttext_from_text('../data/model.vec')
print_inplace("embedding model loaded.\n")


for dataset in analog_datasets:
	totals={}
	corrects={}

	X=[r["words"] for r in dataset['rows']]
	X=np.array(X)
	result=similarity.getKNearBatch(X,model,"Cosine",thershold)
	result=np.array(result)
	for i,row in enumerate(dataset["rows"]):

		if row["category"] not in totals:
			totals[row["category"]]=0
			corrects[row["category"]]=0
		totals[row["category"]] = totals[row["category"]] + 1
		if(row["words"][3] in result[:,i]):
			corrects[row["category"]]+=1
	write_result_to_file(dataset["name"] , totals , corrects,"results/analogy/"+dataset["name"])
	break
	for row in dataset["rows"]:
		r1= np.array(model.getVec(row["words"][0]))
		r2= np.array(model.getVec(row["words"][1]))
		r3=np.array(model.getVec(row["words"][2]))
		_flag=False
		for w in row["words"]:
			if w not in model.words:
				print("warning! the word "+w+" doesn't exist in vocabulary so  we skip asserting this question! ")
				_flag=True
		if(_flag):
			continue
		words=similarity.getKNear(r1,r2,r3,model,thershold , 'Cosine')
		
		if row["category"] not in totals:
			totals[row["category"]]=0
			corrects[row["category"]]=0
		totals[row["category"]] = totals[row["category"]] + 1
		if row["words"][3] in words:
			corrects[row["category"]] = corrects[row["category"]] + 1
	write_result_to_file(dataset["name"] , totals , corrects,"results/analogy/"+dataset["name"])
