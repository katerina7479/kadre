from PySide.QtGui import QWidget
from view.widgets.vbox import Vbox


class Page(QWidget):

    def __init__(self, pagemanager, name):
        super(Page, self).__init__()
        self.PM = pagemanager
        self.name = name
        self.resize(0, 0)
        self._setup()
        self._build()

    def _setup(self):
        pass

    def _build(self):
        self.layout = Vbox()
        self._header()
        self._center()
        self._footer()
        self.setLayout(self.layout)
        #self.show() ***Don't do this on the initial build. Do on the refresh, or it will blink.

    def _header(self):
        pass

    def _center(self):
        pass

    def _footer(self):
        self.layout.addStretch(1)

    def refresh(self):
        self.show()
