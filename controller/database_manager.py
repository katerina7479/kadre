import sqlite3
from kglobals import _PATH


class DatabaseManager():
    def __init__(self, path=None):
        if path is None:
            self.SetPath(False)
        else:
            self.path = path

    def SetPath(self, mytest):
        if mytest is True:
            self.path = _PATH + "\\data\\database\\test.sqlite3"
        elif mytest is False:
            self.path = _PATH + "\\data\\database\\project.sqlite3"
        else:
            print "Path is %s" % _PATH
            raise Exception("Cannot initialize database")

    def _CreateConnection(self):
        self.connection = sqlite3.connect(self.path)
        self.c = self.connection.cursor()

    def Save(self):
        self.connection.commit()

    def _CloseConnection(self):
        self.connection.close()
        self.connection = None
        self.c = None

    def CreateTables(self, tabledata):
        self._CreateConnection()
        for tablename, atts in tabledata.iteritems():
            start = "CREATE TABLE %s (id INTEGER PRIMARY KEY, " % tablename
            temp = []
            for item in atts:
                mytype = atts[item].upper()
                temp.append("%s %s" % (item, mytype))
            tempstr = ", ".join(temp)
            command = start + tempstr + (");")
            print command
            self.c.execute(command)
        self.Save()
        self._CloseConnection()

    def GetTableList(self):
        self._CreateConnection()
        cursor = self.c.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tableslist = cursor.fetchall()
        self._CloseConnection()
        return tableslist

    def GetColumns(self, tablename):
        self._CreateConnection()
        command = "PRAGMA table_info( %s );" % tablename
        cursor = self.c.execute(command)
        columns = cursor.fetchall()
        self._CloseConnection()
        colnames = []
        for col in columns:
            colnames.append(col[1])
        return colnames

    def Delete(self, tablename, myid):
        self._CreateConnection()
        command = "DELETE FROM %s WHERE id == ?;" % tablename
        self.c.execute(command, (myid,))
        self.Save()
        self._CloseConnection()
        pass

    def Update(self, tablename, row, dic):
        self._CreateConnection()
        for key, value in dic.iteritems():
            command = "UPDATE %s SET %s = ? WHERE id = ?;" % (tablename, key)
            self.c.execute(command, (value, row))
        self.Save()
        self._CloseConnection()

    def Add(self, tablename, dic):
        key = dic.keys()[0]
        command = "INSERT INTO %s (%s) VALUES (?);" % (tablename, key)
        value = dic[key]
        command2 = "SELECT last_insert_rowid();"
        self._CreateConnection()
        cursor = self.c.execute(command, (value,))
        cursor = self.c.execute(command2)
        myid = cursor.fetchone()
        self.Save()
        self._CloseConnection()
        self.Update(tablename, myid[0], dic)
        return myid[0]

    def _QueryTableAll(self, tablename):
        columns = self.GetColumns(tablename)
        values = self._QueryByColsAll(tablename, columns)
        answerlist = []
        for row in values:
            answerdict = {}
            answerlist.append(answerdict)
            i = 0
            for col in columns:
                answerdict[col] = row[i]
                i += 1
        return answerlist

    def _QueryTableRow(self, tablename, row):
        columns = self.GetColumns(tablename)
        answerdict = {}
        self._CreateConnection()
        for col in columns:
            command = "SELECT %s FROM %s WHERE id == ?;" % (col, tablename)
            cursor = self.c.execute(command, (row,))
            answer = cursor.fetchone()
            answerdict[col] = answer[0]
        self._CloseConnection()
        return answerdict

    def _QueryByColsAll(self, tablename, colist):
        collumns = ', '.join(colist)
        command = "SELECT %s FROM %s;" % (collumns, tablename)
        self._CreateConnection()
        cursor = self.c.execute(command)
        answerlist = cursor.fetchall()
        self._CloseConnection()
        return answerlist

    def _QueryColsWhere(self, tablename, colist, wheretup):
        collumns = ', '.join(colist)
        command = "SELECT %s FROM %s WHERE %s = ?;" % (collumns, tablename, wheretup[0])
        self._CreateConnection()
        cursor = self.c.execute(command, (wheretup[1],))
        answerlist = cursor.fetchall()
        self._CloseConnection()
        return answerlist

    def _QueryWhere(self, tablename, wheretup):
        command = "SELECT id FROM %s WHERE %s = ?;" % (tablename, wheretup[0])
        self._CreateConnection()
        cursor = self.c.execute(command, (wheretup[1],))
        rows = cursor.fetchall()
        self._CloseConnection()
        anslist = []
        for row in rows:
            anslist.append(self._QueryTableRow(tablename, row[0]))
        return anslist

    def Query(self, tablename, col=False, cols=False, row=False, wcol=False, wval=False):
        if wcol is not False and wval is not False:
            if cols:
                answers = self._QueryColsWhere(tablename, cols, (wcol, wval))
            elif col:
                answers = self._QueryColsWhere(tablename, [col], (wcol, wval))
            else:
                answers = self._QueryWhere(tablename, (wcol, wval))
        elif row:
            answers = self._QueryTableRow(tablename, row)
        elif cols:
            answers = self._QueryByColsAll(tablename, cols)
        elif col:
            answers = self._QueryByColsAll(tablename, [col])
        else:
            answers = self._QueryTableAll(tablename)
        return answers
