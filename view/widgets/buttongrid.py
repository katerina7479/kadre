from PySide.QtGui import QGridLayout


class ButtonGrid(QGridLayout):
    def __init__(self, *args):
        super(ButtonGrid, self).__init__()
        self.setContentsMargins(20, 20, 20, 20)
        self.setSpacing(10)
        self.maxcols = 2
        self.r = 0
        self.c = 0
        self.buttonlist = []

    def addButton(self, btn):
        self.buttonlist.append(btn)
        self.addWidget(btn, self.r, self.c)
        if self.c < self.maxcols:
            self.c += 1
        else:
            self.c = 0
            self.r += 1

    def clearall(self):
        for btn in self.buttonlist:
            btn.setParent(None)
        del self.buttonlist
        self.buttonlist = []
        self.r = 0
        self.c = 0
