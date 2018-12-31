import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from collections import Counter


my_dict = {}

def write_in_file(path1,my_list) :
    with open(path1, 'w' , encoding='utf-8') as f:
        f.write(my_list)


def save_in_file(my_list,name):
    set_my_list = list(set(my_list))
    all_my_list = ""
    for i in range(len(set_my_list)):
        if name=="concepts":
            all_my_list += str(i) + ":" + set_my_list[i] + "\n"
            my_dict.update([(str(set_my_list[i]), str(i))])
        else:
            all_my_list += set_my_list[i] + "\n"

    write_in_file("./files/"+name+'.txt', all_my_list)


fname = "./files/concept-categorization-dataset.csv"
text_file = open(fname, "r", encoding='utf-8')
lines = text_file.readlines()

concepts = []
member = []
vocabulary = []

for item in lines:
    cnp = item.split(",")[0]
    mbr = item.split(",")[1]
    concepts.append(cnp.strip())
    member.append(mbr.strip())

vocabulary=member+list(set(concepts))

save_in_file(concepts , "concepts")

all_member=""
for i in range(len(member)):
    all_member+=member[i]+"\n"
write_in_file("./files/" + "members" + '.txt', all_member)

all_vocab=""
for i in range(len(member)):
    all_vocab+=vocabulary[i]+"\n"
write_in_file("./files/" + "vocabulary" + '.txt', all_member)

res=""
for item in lines:
    cnp = item.split(",")[0]
    mbr = item.split(",")[1]
    res +=  my_dict[str(cnp.strip())]+","+mbr.strip()+"\n"
write_in_file("./files/" + "members_labeled" + '.txt', res)


def write_in_file(path1,my_list) :
    with open(path1, 'w' , encoding='utf-8') as f:
        f.write(my_list)

fname = "./files/members_labeled.txt"
text_file = open(fname, "r", encoding='utf-8')
lines = text_file.readlines()

##########################
#just for test :)
#we must use real word embeddings vectore here

# test_array = np.random.rand(3102,100)  #vocab size : 3102 , word2vec dim : 100
test_array = np.random.rand(3102,10)
X = pd.DataFrame(data=test_array)

##########################

kmeans=KMeans(n_clusters=93)
kmeansoutput=kmeans.fit_predict(X)
result = list(kmeansoutput)


members=[]
out=[]
count = 0
for item in lines:
    ln = item.split("\n")[0]

    word = ln.split(",")[1]
    label = ln.split(",")[0]

    tmp=["_"+str(label), str(word) ,result[count]]
    out.append(tmp)
    count+=1

out.sort(key=lambda c: c[2])

result_str="cluster number,word,label \n"
for i in range(len(out)):
    result_str += str(out[i][0])+ "," +str(out[i][1])+ "," +str(out[i][2])+"\n"
write_in_file("./files/" + "k_means" + '.txt', result_str)

dict_label_of_cluster = {}
for i in range(93):
  cluster = []
  for j in range(len(out)):
      if out[j][2]==i:
          cluster.append(out[j][0].split("_")[1])
  mf = Counter(cluster)
  mf_list = mf.most_common(1)
  label_of_cluster = mf_list[0][0]
  dict_label_of_cluster.update([(str(i), str(label_of_cluster))])

# print(dict_label_of_cluster)

correct=0

final_result_str="predicted label,word,real label \n"
for i in range(len(out)):
    final_result_str+= str(out[i][0])+ "," + str(out[i][1]) + str(dict_label_of_cluster[str(out[i][2])])+"\n"
    if str(out[i][0]).split("_")[1]== str(dict_label_of_cluster[str(out[i][2])]):
        correct+=1


write_in_file("./files/" + "final_output" + '.txt', final_result_str)
print("accuracy : ",correct/len(out))











