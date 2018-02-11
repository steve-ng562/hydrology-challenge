from hydrology import hydrologyChallenge


def test():  # compare test data to validation data
    data = hydrologyChallenge.process("http://rapid-hub.org/data/angles_UCI_CS.csv")
    data2 = hydrologyChallenge.process("http://rapid-hub.org/data/angles_UCI_CS_out.csv")
    assert data.loc[:, "angle_degrees"].tolist() == data.loc2[:, "station_id"].tolist()
    assert data.loc[:, "station_id"].tolist() == data.loc2[:, "station_id"].tolist()




