


from os import listdir
from os.path import isfile, join

def loadAnalogyDataset(path):

    allfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    datasets=[]
    print(allfiles)
    for f in allfiles:
        with open (f, "r") as myfile:
            lines = myfile.read().splitlines()
        dataset={"name":f,'rows':[]}
        cat = None
        for l in lines:
            if l.startswith(":"):
                cat =l.lower().split()[1]
            else:
                words =  l.split()
                dataset["rows"].append({'words':words,'category':cat})
        datasets.append(dataset)

    return datasets