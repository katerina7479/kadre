from PySide.QtGui import QComboBox


class Combo(QComboBox):
    def __init__(self, *args):
        super(Combo, self).__init__()

    def addlist(self, combolist):
        for item in combolist:
            self.insertItem(item[0], item[1])

    def setList(self, newlist):
        self.clearall()
        self.addlist(newlist)

    def clearall(self):
        self.clear()
