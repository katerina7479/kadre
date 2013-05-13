from PySide.QtGui import QVBoxLayout


class Vbox(QVBoxLayout):
    def __init__(self, *args):
        super(Vbox, self).__init__()

    def clear(self):
        children = self.children()
        for child in children:
            child.setParent(None)
