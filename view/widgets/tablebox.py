from PySide import QtGui
from PySide.QtGui import QTableWidget, QAbstractItemView


class TableBox(QTableWidget):
    def __init__(self, mylist, headerlist, editcallback, *args):
        super(TableBox, self).__init__()
        self.mylist = mylist
        self.headerlist = headerlist
        self.itemDoubleClicked.connect(editcallback)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemlist = []
        self.config()
        self.headers()
        self.build()

    def config(self):
        self.rows = len(self.mylist)
        self.cols = len(self.headerlist)
        self.setRowCount(self.rows)
        self.setColumnCount(self.cols)

    def headers(self):
        columtitles = []
        for col in self.headerlist:
            columtitles.append(col["title"])
        self.setHorizontalHeaderLabels(columtitles)

    def build(self):
        r = 0
        for row in self.mylist:
            item = {}
            item["row"] = r
            item["id"] = row["id"]
            c = 0
            for col in self.headerlist:
                item[col["column"]] = QtGui.QTableWidgetItem(str(row[col["column"]]))
                self.setItem(r, c, item[col["column"]])
                self.itemlist.append(item)
                if c < self.cols:
                    c += 1
                else:
                    c = 1
            r += 1

    def Update(self, mylist):
        self.mylist = mylist
        self.clearContents()
        del self.itemlist
        self.itemlist = []
        self.config()
        self.build()

    def Get(self):
        selection = self.currentRow()
        for item in self.itemlist:
            if selection == item["row"]:
                return item["id"]
            else:
                pass
        raise(KeyError, "Nothing Selected")

    def DeleteCurrent(self):
        selection = self.currentRow()
        self.removeRow(selection)
        for item in self.itemlist:
            if selection == item["row"]:
                del item
