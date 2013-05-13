from PySide import QtGui
from PySide.QtGui import QHBoxLayout

from popup import Popup
from view.widgets.buttonvbox import ButtonVBox
from view.widgets.listbox import ListBox


class OpenDialog(Popup):

    def __init__(self, parent):
        self.parent = parent
        super(OpenDialog, self).__init__()
        self.title = "Open Dialog"
        self.resize(400, 200)

    def _refresh(self):
        self._setup()

    def _setup(self):
        self.choicelist = [(0, "Choose Me!"), (1, "No, Me!")]
        self.buttonlist = [{"type": "button", "text": "Open", "callback": self.on_open}]

    def _header(self):
        label = QtGui.QLabel("Select Item to Open: ")
        self.layout.addWidget(label)

    def _center(self):
        self.hbox = QHBoxLayout()
        self.layout.addLayout(self.hbox)

        vbox = ButtonVBox(self.buttonlist)
        self.hbox.addLayout(vbox)

        self.listbox = ListBox(self.choicelist, self.on_open)
        self.hbox.addWidget(self.listbox)

    def _footer(self):
        hbox2 = QHBoxLayout()
        self.layout.addLayout(hbox2)

        cancelbut = QtGui.QPushButton("Close")
        cancelbut.released.connect(self.close)
        hbox2.addStretch(1)
        hbox2.addWidget(cancelbut)

    def on_open(self):
        myid = self.listbox.getId()
        print self.choicelist[myid]
        self.parent.PageManager.ThisPage("ButtonGridPage")
        self.close()
