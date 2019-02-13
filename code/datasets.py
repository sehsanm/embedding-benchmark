


from os import listdir
from os.path import isfile, join

def loadAnalogyDataset(path):

    allfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    datasets=[]
    for f in allfiles:
        with open (f, "r") as myfile:
            lines = myfile.read().splitlines()
        dataset={"name":f.split("/")[-1],'rows':[]}
        cat = None
        for l in lines:
            cols =  l.split(",")
            if(len(cols)!=5):
                raise Exception("analogy test set corrupted")
            dataset["rows"].append({'words':cols[1:],'category':cols[0]})
        datasets.append(dataset)

    return datasets