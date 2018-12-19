# Compute Spearman’s rank correlation coefficient between this score and the human judgments
# by Aamin Abbasi

import pandas as pd
import numpy as np
from scipy.stats import spearmanr

# get dataset name
filename = 'SemanticSimilarityDataset.csv.xlsx'
f_extns = filename.split(".")

# if similarity dataset format is '.xlsx' with four columns (word1, word2, similarity, human_judgment)
if(f_extns[-1] == 'xlsx'):
    WS = pd.read_excel(filename)
    WS_np = np.array(WS)
    similarity_rate = []
    human_judgment = []
    for row  in WS_np:
        similarity_rate.append(row[2])
        human_judgment.append(row[3])

# if similarity dataset format is '.CSV' or '.txt'
else:
    similarity_dataset = np.genfromtxt(filename, delimiter=',')
    similarity_rate = similarity_dataset[:,2].tolist()
    human_judgment = similarity_dataset[:,3].tolist()


corr, p_value = spearmanr(similarity_rate, human_judgment)
print("Spearman's rank correlation coefficient : ",corr)
print("Spearman's p_value : ",p_value)
