from PySide import QtGui
from pages import Page
from view.widgets.buttongrid import ButtonGrid


class ButtonGridPage(Page):
    # I use this as a "dashboard", to quickly make an initial selection, like opening
    # an existing project.
    def __init__(self, parent, name):
        self.buttonlist = [(0, "FormPage"), (1, "TableBoxPage")]
        super(ButtonGridPage, self).__init__(parent, name)

    def _header(self):
        label = QtGui.QLabel(
            '<font size=16 align="center">My Button Grid Page</font>')
        label.indent = 20
        self.layout.addWidget(label)

    def _center(self):
        self.grid = ButtonGrid()
        self.layout.addLayout(self.grid)
        self._make_buttons()

    def _make_buttons(self):
        for item in self.buttonlist:
            itemid = item[0]
            itemlabel = item[1]

            btn = QtGui.QPushButton(itemlabel, self)
            btn.setMaximumSize(100, 100)
            btn.released.connect(lambda i=itemid: self.on_open_page(i))
            self.grid.addButton(btn)

    def refresh(self):
        self.grid.clearall()
        self._setup()
        self._make_buttons()
        self.show()

    def on_open_page(self, pageid):
        if pageid is 0:
            self.PM.ThisPage("FormPage")
        else:
            self.PM.ThisPage("TableBoxPage")
