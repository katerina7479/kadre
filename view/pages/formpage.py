from PySide import QtGui
from pages import Page

from view.widgets.form import Form


class FormPage(Page):

    def __init__(self, parent, name):
        super(FormPage, self).__init__(parent, name)

    def _setup(self):
        self.combolist = [(1, "Test1"), (2, "Test2")]  # Can be from database

        self.formlist = [
            {"column": "name", "label": "Name: ",
                "type": "textenter", "value": "Name"},
            {"column": "number", "label": "Number: ",
             "type": "textenter", "value": "XXX"},
            {"column": "question", "label": "Question?: ",
             "type": "checkbox", "value": True},
            {"column": "test_id", "label": "Select Test: ", "type":
             "combobox", "list": self.combolist, "value": 1}]

    def _header(self):
        label = QtGui.QLabel('<font size=16 align="center">My Form Page</font>')
        label.indent = 20
        self.layout.addWidget(label)

    def _center(self):
        self.form = Form(self.formlist)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(0.5)
        hbox.addLayout(self.form)
        hbox.addStretch(0.5)

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)  # Adds some space between the form and the footer buttons

    def _footer(self):
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        okbut = QtGui.QPushButton("Ok", self)
        okbut.released.connect(self.on_ok)
        hbox.addWidget(okbut)

        clearbut = QtGui.QPushButton("Cancel", self)
        clearbut.released.connect(self.on_clear)
        hbox.addWidget(clearbut)

        hbox.addStretch(1)  # Moves boxes to the center, delete to right justify

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)

    def refresh(self):
        self._setup()
        self.form.UpdateComboLists([self.combolist])
        self.layout.update()

    def on_clear(self):
        self.form.clearForm()

    def on_ok(self):
        formdata = self.form.getData()
        print formdata

        self.PM.ThisPage("ButtonGridPage")
