import pandas as pd
import math

url = 'http://rapid-hub.org/data/angles_UCI_CS.csv'
data = pd.read_csv(url, skipinitialspace=True)
angles = data.loc[:, "angle_degrees"].tolist()
cosine = []
for s in angles:
    cosine.append(round(math.cos(math.radians(s)), 4))


def return_cosine():
    return cosine


cos = pd.Series(cosine)
data['cos'] = cos.values
print(data)


