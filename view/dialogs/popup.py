from PySide.QtGui import QWidget
from view.widgets.vbox import Vbox


class Popup(QWidget):
    def __init__(self):
        super(Popup, self).__init__()
        self.resize(600, 600)
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

    def _header(self):
        pass

    def _center(self):
        pass

    def _footer(self):
        pass
