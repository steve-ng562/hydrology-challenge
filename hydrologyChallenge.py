import pandas as pd
import math

URL = 'http://rapid-hub.org/data/angles_UCI_CS.csv'


def process(url):
    data = pd.read_csv(url, skipinitialspace=True)
    angles = data.loc[:, "angle_degrees"].tolist()
    cosine = []
    for s in angles:
        cosine.append(round(math.cos(math.radians(s)), 4))
    cos = pd.Series(cosine)
    data['cos'] = cos.values
    print(data)
    return data

process(URL)
