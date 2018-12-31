import pandas as pd
import numpy as np
from scipy.stats import spearmanr, pearsonr



def load_data(dataset_path, has_header=False):
    if has_header:
        dataset = pd.read_csv(dataset_path, header=0)
    else:
        dataset = pd.read_csv(dataset_path, header=None)
    return dataset


def words_similarity(wordslist1, wordslist2, model, method='C'):
    """
    :param wordslist1: numpy array of words
    :param wordslist2: numpy array of words
    :param model: object of model instance of LoadModel
    :param method: 'C' for cosine_similarity and 'E' for Euclidean_distance , default is 'C'
    :return: similarity rate between words in wordslist1 and wordslist2
    """
    similarity_of_model = []
    model = model.normalize_words()  # use normalize_words() from LoadModel package of Mehdi Jafari
    if method == 'C':
        for w1, w2 in zip(wordslist1, wordslist2):
            wv1 = model.get_vector(w1)  # get word vector w1 from model
            wv2 = model.get_vector(w2)  # get word vector w2 from model
            cos_sim = np.dot(wv1, wv2) / (np.linalg.norm(wv1) * np.linalg.norm(wv2))
            similarity_of_model.append(cos_sim)

    elif method == 'E':
        for w1, w2 in zip(wordslist1, wordslist2):
            wv1 = model.get_vector(w1)  # get word vector w1 from model
            wv2 = model.get_vector(w2)  # get word vector w2 from model
            dist = np.linalg.norm(wv1 - wv2)
            similarity_of_model.append(dist)

    else:
        raise ValueError("method not correct")

    return similarity_of_model



def correlation_coefficient(sim_dataset_path, model, sim_columns=[], has_header=False, method='s'):
    """
    :param sim_dataset_path:(type:string) dataset csv file path
    :param model:(type:object) object of model instance of LoadModel
    :param sim_columns:(type:list of integer) list of index of columns, index should started of 3 (exp:[3,4,7])
            default is empty list means that get all columns of similarities
    :param has_header:(type:Boolean) default is False , if dataset has header, set has_header to True
    :param method:(type:char) Correlation coefficient method, if 's':Spearman and 'p':Pearson

    :return:(list of integer) Spearman or Pearson correlation coefficient respect to sim_columns
    """
    dataset = load_data(sim_dataset_path, has_header)

    num_of_sim_columns = dataset.shape[1]
    list_of_words1 = dataset.iloc[:, 0]
    list_of_words2 = dataset.iloc[:, 1]

    sim_of_model = words_similarity(list_of_words1, list_of_words2, model)

    if not sim_columns:     # if sim_columns is empty
        sim_columns = list(range(3, num_of_sim_columns + 1))
    else:
        if(max(sim_columns) > num_of_sim_columns):
            raise ValueError("maximum index of columns is", num_of_sim_columns)
        elif(min(sim_columns) < 3):
            raise ValueError("minimum index of columns is", 3)


    corr_coe_rates = []
    if (method == 's') :    # spearman correlation coefficient
        for i in sim_columns:
            sim_of_dataset = dataset.iloc[:, i - 1]
            spearman = spearmanr(np.array(sim_of_model), np.array(sim_of_dataset))
            corr_coe_rates.append(spearman[0])
    elif(method == 'p') :    # pearson correlation coefficient
        for i in sim_columns:
            sim_of_dataset = dataset.iloc[:, i - 1]
            pearson = pearsonr(np.array(sim_of_model), np.array(sim_of_dataset))
            corr_coe_rates.append(pearson[0])
    else:
        raise ValueError("method not correct")

    return corr_coe_rates

