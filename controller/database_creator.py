import os
from utils import myjson
from kglobals import _PATH


class DatabaseCreator():
    def __init__(self, DM):
        self.databasePath = _PATH + "\\data\\database\\project.sqlite3"
        self.table_path = _PATH + "\\data\\tables.json"
        self.table_init_path = _PATH + "\\data\\db_init.json"
        self.DM = DM

    def CreateDatabase(self):
        try:
            self._DeleteDatabase()
        except:
            pass
        self.tabledata = myjson.GetData(self.table_path)
        self.DM.CreateTables(self.tabledata)

    def InitializeDatabase(self):
        self.initdata = myjson.GetData(self.table_init_path)
        self._AddData()

    def _AddData(self):
        for tablename in self.initdata:
            test = self.initdata[tablename]
            if type(test) == list:
                for dic in test:
                    self.DM.Add(tablename, dic)
            elif type(test) == dict:
                self.DM.Add(tablename, test)

    def _DeleteDatabase(self):
        try:
            os.remove(self.databasePath)
        except OSError:
            print "Did not remove database"
