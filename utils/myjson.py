import json


def GetData(path):
    jsonfile = open(path)
    data = json.load(jsonfile)
    jsonfile.close()
    return data
