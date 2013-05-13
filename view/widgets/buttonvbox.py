from PySide import QtGui
from PySide.QtGui import QVBoxLayout


class ButtonVBox(QVBoxLayout):
    def __init__(self, buttonlist, *args):
        super(ButtonVBox, self).__init__()
        self.buttonlist = buttonlist
        self.build()

    def build(self):
        for item in self.buttonlist:
            item["widget"] = QtGui.QPushButton(item["text"])
            item["widget"].released.connect(item["callback"])
            self.addWidget(item["widget"])
            self.addStretch(0.1)
        self.addStretch(1)
