import hydrologyChallenge


def test():  # compare test data to validation data
    data = hydrologyChallenge.process("http://rapid-hub.org/data/angles_UCI_CS.csv")
    data2 = hydrologyChallenge.process("http://rapid-hub.org/data/angles_UCI_CS_out.csv")
    assert data2.loc[:, "angle_degrees"].tolist() == data.loc[:, "angle_degrees"].tolist()
    assert data2.loc[:, "station_id"].tolist() == data.loc[:, "station_id"].tolist()




