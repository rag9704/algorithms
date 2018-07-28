import numpy as np
from math import sqrt
import warnings
import pandas as pd
from collections import Counter
import random 


def k_nearest_neighbors(data,predict,k=3):
    if len(data) >= k:
        warnings.warn('K is set to value less ')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance =np.linalg.norm(np.array(features)-np.array(predict))#check it out
            distances.append([euclidean_distance , group])

    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result
df = pd.read_csv(r"C:\Users\Rag9704\Desktop\breast-cancer-wisconsin.data.txt")
df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)

full_data = df.astype(float).values.tolist()#converting to float/int

print(full_data[:10])
