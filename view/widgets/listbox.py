from PySide.QtGui import QListWidgetItem, QListWidget


class ListBox(QListWidget):
    def __init__(self, mylist, editcallback, *args):
        super(ListBox, self).__init__()
        self.mylist = mylist
        self.doubleClicked.connect(editcallback)
        self.build()

    def build(self):
        self.itemlist = []
        for item in self.mylist:
            itemdict = {"id": item[0], "value": item[1]}
            itemdict["widget"] = QListWidgetItem(itemdict["value"], self)
            self.itemlist.append(itemdict)

    def Update(self, newlist):
        self.clearall()
        self.mylist = newlist
        self.build()

    def clearall(self):
        self.clear()
        del self.itemlist

    def add(self, myid, value):
        self.mylist.append({"id": myid, "value": value, "widget": QListWidgetItem(value, self)})

    def getId(self):
        selection = self.currentItem()
        for item in self.itemlist:
            if selection is item["widget"]:
                myid = item["id"]
        return myid

    def getValue(self):
        selection = self.currentItem()
        for item in self.itemlist:
            if selection is item["widget"]:
                value = item["value"]
        return value
