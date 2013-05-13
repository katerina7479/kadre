import sys

from PySide import QtGui
from view.main_window import KMainWindow


def main():
    # Creates main QTGui App
    app = QtGui.QApplication(sys.argv)
    # Set a style, options include:
    # "cleanlooks", "plastique", "motif",
    # "Windows", "CDE", "WindowsXP", "WindowsVista"
    # Comment out the two lines for the default.
    # May also be able to create your own here.
    # For the complete list do:
    # print QtGui.QStyleFactory.keys()
    style = QtGui.QStyleFactory.create("Cleanlooks")
    app.setStyle(style)

    w = KMainWindow("My Title")
    w.show()

    # Sets the exit button
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
