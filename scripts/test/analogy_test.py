from code.models import models
from code import datasets
from  code.analogy import similarity
from code.analogy.helpers import write_result_to_file
import numpy as np
import sys
from optparse import OptionParser

def print_inplace(txt):
	sys.stdout.write("\r"+txt)
	sys.stdout.flush()


parser = OptionParser()
parser.add_option("-t", "--thereshold",type="int", dest="thereshold",
                  help="thereshold for checking nearest vecotrs to answers",
                  default=None)

parser.add_option("-m", "--method",type="string", dest="method",
                  help="method of solving analogy problem can be one of these item : batch , pair , euclidean",
                  default="batch")

parser.add_option("-i", "--inputmodel",type="string", dest="inputModel",
                  help="path to input model",
                  default=False)

(options,args) = parser.parse_args()
if not options.thereshold:   
    parser.error('thereshold must be specified')
if not options.inputModel: 
    parser.error('path to input model must be specified')
if  options.method not in ["pair","batch","euclidean"]: 
    parser.error('method can be one of "pair","batch","euclidean"')

print_inplace("loading analogy dataset...")
analog_datasets=datasets.loadAnalogyDataset('data/analogy')
print_inplace("analogy dataset loaded.")
#load model
print_inplace("loading embedding model ...")
# model = models.W2V.from_text('data/models/sample.vec')
model = models.W2V.fasttext_from_text(options.inputModel)
print_inplace("embedding model loaded.\n")


for dataset in analog_datasets:
	totals={}
	corrects={}
	if(options.method=='batch'):
		X=[r["words"] for r in dataset['rows']]
		X=np.array(X)
		result=similarity.getKNearBatch(X,model,"Cosine",options.thereshold,50)
		result=np.array(result)
		# for i,row in enumerate(dataset["rows"]):
		rows=dataset['rows']
		for i,row in enumerate(result):
			row=rows[i]
			if row["category"] not in totals:
				totals[row["category"]]=0
				corrects[row["category"]]=0
			totals[row["category"]] = totals[row["category"]] + 1
			if(row["words"][3] in result[i,:]):
				corrects[row["category"]]+=1
		write_result_to_file(dataset["name"] , totals , corrects,"results/analogy/"+dataset["name"])
	else:
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
			words=similarity.getKNear(r1,r2,r3,model,options.thereshold ,'Euclidean' if options.method=="euclidean" else "PairDirection")
			if row["category"] not in totals:
				totals[row["category"]]=0
				corrects[row["category"]]=0
			totals[row["category"]] = totals[row["category"]] + 1
			if row["words"][3] in words:
				corrects[row["category"]] = corrects[row["category"]] + 1
		write_result_to_file(dataset["name"] , totals , corrects,"results/analogy/"+dataset["name"])
