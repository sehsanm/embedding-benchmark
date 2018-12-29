import os
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from model import LoadModel

class similarity_util():
    def __init__(self, data_model_path=None, model=None):    # need to default path or default model
        self.load_model(data_model_path, model)
        self._speramn_score = None   # is tuple (correlation, p_value)

    def load_model(self,data_model_path=None,model=None):
        if(model):
            self._model = model
            return self._model
        elif(data_model_path):
            ext = os.path.splitext(data_model_path)[1]   # ext is .bin or .txt (file of words or sentences) or .pkl or pckl or .model and etc. which?
            self._model = LoadModel.from_bin(data_model_path)
            return self._model
        else:
            raise ValueError("assign value to data_model_path or model")

    def load_data(self):
        if(self._has_header):
            self._dataset = pd.read_csv(self.sim_dataset_path, header=0)
        else:
            self._dataset = pd.read_csv(self.sim_dataset_path)


    def words_similarity(self, word1, word2, method="C"):
        """
        :param word1:
        :param word2:
        :param method: can be "C" : cosine_similarity or "E": Euclidean_distance , default is "c"
        :return: similarity
        """
        wv1 = self._model.get_vector(word1)     # get word vector w1 from model
        wv2 = self._model.get_vector(word2)     # get word vector w2 from model
        n_wv1 = np.array(self.normalize(wv1))     # normalize word vector 1 between(0,1)
        n_wv2 = np.array(self.normalize(wv2))     # normalize word vector 2 between(0,1)

        if(method == "C"):
            cos_sim = np.dot(n_wv1, n_wv2) / (np.linalg.norm(n_wv1) * np.linalg.norm(n_wv2))
            return cos_sim
        elif(method == "E"):
            dist = np.linalg.norm(n_wv1 - n_wv2)
            return dist
        else:
            raise ValueError("Method not correct")

    def spearman_score(self, sim_dataset_path, sim_col1=3, sim_col2=4, has_header=None):
        """
        spearman correlation between two similarity
        """
        self.sim_dataset_path = sim_dataset_path
        self._has_header = has_header
        self.load_data()

        list_of_word1 = self._dataset.iloc[:, 0]
        list_of_word2 = self._dataset.iloc[:, 1]
        sim1 = self._dataset.iloc[:, sim_col1-1]
        sim1 = self.normalize(sim1, min_value=0, max_value=5)

        if(sim_col2):
            sim2 = self._dataset.iloc[:, sim_col2-1]
            sim2 = self.normalize(sim2, min_value=0, max_value=5)
        else:
            sim2 = []
            for w1, w2 in zip(list_of_word1, list_of_word2):
                sim2.append(self.words_similarity(w1,w2))
            sim2 = self.normalize(sim2, min_value=-1, max_value=1)


        self._speramn_score = spearmanr(sim1, sim2)
        # print("Spearman's rank correlation coefficient : ", self._speramn_score[0])
        # print("Spearman's p_value : ", self._speramn_score[0])

        '''
        
        """ add new column to similarity dataset from model """
        dataset_with_sim_model = self._dataset.assign(sim_model=pd.Series(np.array(sim_from_model)).values)
        """ save to file """
        full_path = os.path.splitext(self._path)[0]
        # filename = full_path.split('/')[-1]
        # source = full_path.split(filename)[0]
        dataset_with_sim_model.to_csv(full_path+"_sim_model.csv", sep=',', encoding='utf-8')
        return "new similarity dataset with new column (similarity from model) created in "+full_path+"_sim_model.csv"
        
        '''


    def get_spearman_score(self):
        return self._speramn_score

    def normalize(self, vector, min_value=None, max_value=None):
        if (min_value is None) or (max_value is None):
            min_value = min(vector)
            max_value = max(vector)
        normal_vector = []
        for i in vector:
            normal_vector.append((i - min_value) / (max_value - min_value))
        return normal_vector
