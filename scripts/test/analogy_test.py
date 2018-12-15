from code.models import models
from code import datasets
import code.helpers
from  code.analogy import similarity
from code.helpers import write_result_to_file
#set thershold
thershold=50
#load dataset
analog_datasets=datasets.loadAnalogyDataset('data/analogy')
#load model
model = models.loadmodel('data/models/model_khafan.bin')
for dataset in analog_datasets:
	totals={}
	corrects=[]
	for row in dataset["rows"]:
		r1= model.getVec(row["words"][0])
		r2= model.getVec(row["words"][1])
		r3=model.getVec(row["words"][2])
		words=similarity.getKNear(r1,r2,r3,model,thershold , 'Cosine')
		totals[row["category"]] = totals["category"] + 1
		if row["words"][3] in words:
			corrects[row["category"]] = corrects[row["category"]] + 1
	write_result_to_file(dataset["name"] , totals , corrects,"results/analogy/"+dataset["name"])
