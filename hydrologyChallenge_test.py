from hydrology import hydrologyChallenge
import math
# import validation data
station_id = [0,1,2,3]
angle_degrees = [90,60,30,0]
cosine = []

for s in angle_degrees:  # calculate the cosine of validation data
    cosine.append(round(math.cos(math.radians(s)),4))


def test():  # compare test data to validation data
    data = hydrologyChallenge.process("http://rapid-hub.org/data/angles_UCI_CS.csv")
    assert data.loc[:, "cos"].tolist() == cosine




