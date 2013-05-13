from PySide import QtGui
from pages import Page
from view.widgets.buttonvbox import ButtonVBox
from view.widgets.tablebox import TableBox


class TableBoxPage(Page):

    def __init__(self, parent, name):
        super(TableBoxPage, self).__init__(parent, name)

    def _setup(self):
        self.headerlabeltext = "This is my TableBoxPage"
        self.ctext = "Subheader 1"
        self.ptext = "Subheader 2"

        self.buttonlist = [
            {"type": "button", "text": "Add",
                "callback": self.on_add},
            {"type": "button", "text": "Edit",
                "callback": self.on_edit},
            {"type": "button", "text": "Delete",
                "callback": self.on_del}]

        # Usually get datalist from the database
        self.datalist = [{"id": 1, "name": "TestName", "desc": "TestDesc", "date": "02MAR13"}]

        self.collist = [{"column": "name", "title": "Name"},
                        {"column": "desc", "title": "Description"},
                        {"column": "date", "title": "Date"}
                        ]

    def _header(self):
        self.hlabel = QtGui.QLabel(
            "<font size=16 align='center'>%s</font>" % self.headerlabeltext)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.hlabel)
        hbox.addStretch(1)

        self.dashcheck = QtGui.QCheckBox()
        self.dashcheck.setChecked(True)
        self.dashcheck.stateChanged.connect(self.on_dash)

        hbox.addWidget(self.dashcheck)
        hbox.addWidget(QtGui.QLabel("My Check Box"))
        self.layout.addLayout(hbox)

        self.clabel = QtGui.QLabel(self.ctext)
        self.plabel = QtGui.QLabel(self.ptext)

        hbox2 = QtGui.QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.clabel)
        hbox2.addStretch(1)
        hbox2.addWidget(self.plabel)
        hbox2.addStretch(1)
        self.layout.addLayout(hbox2)
        self.layout.addStretch(1)

    def _center(self):
        self.layout.addWidget(QtGui.QLabel("TableBox: "))

        hbox = QtGui.QHBoxLayout()
        vbox = ButtonVBox(self.buttonlist)
        hbox.addLayout(vbox)

        self.tablebox = TableBox(self.datalist, self.collist, self.on_edit)
        hbox.addWidget(self.tablebox)

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)

    def _refreshbox(self):
        #self.datalist = from the database
        #self.tablebox.Update(self.datalist)
        pass

    def _footer(self):
        self.layout.addStretch(1)

    def refresh(self):
        self._setup()
        self._refreshbox()
        self.show()

    def on_add(self):
        # Do Stuff to add to database, and refresh (like make a dialog popup)
        self._refreshbox()

    def on_edit(self):
        myid = self.tablebox.Get()
        print myid  # Dialog for editing
        self._refreshbox()

    def on_del(self):
        myid = self.tablebox.Get()
        print "Deleting %s" % myid  # Delete from database
        # self.tablebox.DeleteCurrent()
        self._refreshbox()

    def on_dash(self):
        self.dashboard = self.dashcheck.isChecked()
        print self.dashboard
