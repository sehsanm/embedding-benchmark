import models as models
import random
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np


class concept_categorization:
    def __init__(self):
        self.member = []

    def add_member(self, member_list):
        self.member.append(member_list)

    def get_score(self):
        correct = 0
        for i in range(len(self.member)):
            if self.member[i][0]=="_"+self.member[i][2]:
                correct+=1
        return (correct/len(self.member))*100

def get_word2vec(model , word):
    vec = list(model.getVec(word))
    return vec

def k_means(input_vectors , K):
    kmeans = KMeans(n_clusters=K)
    kmeansoutput = kmeans.fit_predict(input_vectors)
    output_list = list(kmeansoutput)
    return output_list

def write_in_file(path,data) :
    with open(path, 'w' , encoding='utf-8') as f:
        f.write(data)

def preprocessing(input_file,input_model):

    word_embeddings = {}
    concept_categorization={}
    members = []
    concept_counter=-1
    concept_number={}

    data = open(input_file, "r", encoding='utf-8')
    lines = data.readlines()
    unique_concepts = []
    result=[]

    for item in lines:

        item=item.split("\n")[0]
        cnp = item.split(",")[0]
        mbr = item.split(",")[1]
        members.append(mbr.strip())

        if cnp not in unique_concepts:
            current_members=[]
            unique_concepts.append(cnp)
            concept_counter+=1
            concept_number.update([(cnp, str(concept_counter))])

            current_members.append(mbr)
            concept_categorization.update([(str(cnp), current_members)])

            mach = [mbr, concept_counter]
            result.append(mach)


        else:
            current_members.append(mbr)
            concept_categorization.update([(str(cnp), current_members)])
            mach = [mbr, concept_counter]
            result.append(mach)

    vectors = []

    concept_number_str=""
    for key in concept_number.keys():
        concept_number_str+=str(key) + " : " +str(concept_number[key])+"\n"
    write_in_file("concept_coding.csv" , concept_number_str)

    # model = models.W2V.from_W2V(input_model)
    model = models.W2V.fasttext_from_text(input_model)
    for item in members:
        current_vector =get_word2vec(model , str(item))
        word_embeddings.update([(str(item), current_vector)])
        vectors.append(list(current_vector))

    return vectors,concept_categorization,result,concept_number

def calculate_score(result,k_means_output, K):
    #result[i][0] --> word
    # result[i][1] --> real label
    out=[]
    for i in range(len(k_means_output)):
        mach= [result[i][1]] #label
        mach.append(result[i][0]) #word
        mach.append(k_means_output[i]) #predicated label

        out.append(mach)
    out.sort(key=lambda c: c[2])

    out_str="predicated_label , word , real_label \n"
    for o in range(len(out)):
        out_str+=str(out[o])+"\n"
    write_in_file("k_means_out.csv" , out_str)

    dict_label_of_cluster = {}
    for i in range(K):
        cluster = []
        for j in range(len(out)):
            if out[j][2] == i:
                cluster.append(out[j][0])
        mf = Counter(cluster)
        mf_list = mf.most_common(1)
        label_of_cluster = mf_list[0][0]
        dict_label_of_cluster.update([(str(i), str(label_of_cluster))])

    final_result_str = "voting label , k-means label , word , real label \n"
    final_result=[]

    for i in range(len(out)):
        final_result_str += "_"+str(out[i][0]) + "," + str(out[i][1]) + ","+str(out[i][2])+",*"+str(dict_label_of_cluster[str(out[i][2])]) + "*\n"
        tmp = ["_"+str(out[i][0])]
        tmp.append(out[i][1])
        tmp.append(dict_label_of_cluster[str(out[i][2])])
        final_result.append(tmp)

    score_dict={}
    for i in range(K):
        concept_cat = concept_categorization()
        for j in range(len(final_result)):
            if str(final_result[j][0])== "_"+str(i):
                concept_cat.add_member(final_result[j])
        score = concept_cat.get_score()
        score_dict.update([(str(i), str(score))])



    write_in_file("output" + '.csv', final_result_str)

    return score_dict

def print_result(score_dict, concept_number):
    eval_str=""
    for i in range(len(score_dict)):
        concept = [k for k,v in concept_number.items() if v == str(i)]
        print("concept : " + str(concept) +"\t score : " + str(score_dict[str(i)]))
        eval_str+="concept : " + str(concept) +"\t score : " + str(score_dict[str(i)])+"\n"
    write_in_file("eval.csv" , eval_str)


def main(input_file,inputModel):

    print("Test Scrip For Concept Categorization")

    vectors, concept_categorization, result, concept_number = preprocessing(input_file,inputModel)

    k_means_output = k_means(vectors , len(concept_categorization))

    score_dict = calculate_score(result,k_means_output,len(concept_categorization))

    print_result(score_dict, concept_number)




if __name__ == '__main__':
    input_file="./data/categories/concept-categorization-dataset.csv"
    input_model="./data/models/model.vec"
    main(input_file,input_model)



