import cPickle as pickle
from sqlite3 import Binary


def unPickle(mybinary):
    data = pickle.loads(str(mybinary))
    return data


def getPickle(data):
    mypickle = pickle.dumps(data, protocol=2)
    mybinary = Binary(mypickle)
    return mybinary
