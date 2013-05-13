from PySide import QtGui
from PySide import QtCore
from PySide.QtGui import QMainWindow
from PySide.QtGui import QAction
from utils import myjson
from pagemanager import PageManager
from dialogs.opendialog import OpenDialog
from kglobals import _PATH


class KMainWindow(QMainWindow):
    def __init__(self, title):
        super(KMainWindow, self).__init__()
        self.setWindowTitle(title)
        self.path = _PATH
        self._setPaths()

        self.actiondict = {
            "open": self.on_open, "new": self.on_new, "database": self.on_database,
            "exit": QtGui.qApp.quit, "back": self.on_back, "next": self.on_next}

        self.statusBar()
        self.PageManager = PageManager()
        self._config()

    def _setPaths(self):
        self.menuConfigPath = self.path + "\\view\\menu_actions.json"
        self.toolConfigPath = self.path + "\\view\\toolbar_actions.json"

    def sizeHint(self):
        return QtCore.QSize(800, 600)

    def _config(self):
        self.menuconfigdata = myjson.GetData(self.menuConfigPath)
        self._makeMenuBar()
        self.setCentralWidget(self.PageManager)
        self.toolbarconfigdata = myjson.GetData(self.toolConfigPath)
        self._makeToolBar()

    def _makeMenuBar(self):
        self.menubar = self.menuBar()
        self.menulist = []
        for menu in self.menuconfigdata:
            mymenu = self.menubar.addMenu(menu)
            self.menulist.append(mymenu)
            actions = self.menuconfigdata[menu]
            actionlist = self._parseactions(actions)
            for item in actionlist:
                action = item[0]
                name = item[1]
                if action == "Separator":
                    mymenu.addSeparator()
                else:
                    if name in self.actiondict:
                        mymenu.addAction(action)
                        method = self.actiondict[name]
                        action.triggered.connect(method)
                    else:
                        mymenu.addAction(action)

    def _makeToolBar(self):
        self.toolbar = QtGui.QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbarlist = []
        toollist = self._parseactions(self.toolbarconfigdata)
        for tool in toollist:
            action = tool[0]
            name = tool[1]
            if name == "Separator":
                self.toolbar.addSeparator()
            else:
                if name in self.actiondict:
                    self.toolbar.addAction(action)
                    method = self.actiondict[name]
                    action.triggered.connect(method)
                else:
                    self.toolbar.addAction(action)

    def _sortbyposition(self, uslist):
        slist = sorted(uslist)
        flist = []
        for item in slist:
            flist.append((item[1], item[2]))
        return flist

    def _parseactions(self, actions):
        actionlist = []
        for act in actions:
            atts = actions[act]
            if act == "Separator":
                newaction = "Separator"
            else:
                try:
                    newaction = QAction(QtGui.QIcon(atts["icon"]), atts["text"], self)
                except:
                    newaction = QAction(atts["text"], self)
                try:
                    newaction.setShortcut(atts["shortcut"])
                except:
                    pass
                try:
                    newaction.setStatusTip(atts["statustip"])
                except:
                    pass
            actionlist.append((atts["pos"], newaction, act))
        actionlist = self._sortbyposition(actionlist)
        return actionlist

    def on_open(self):
        self.PageManager.ThisPage("Blank")
        self.diag = OpenDialog(self)
        self.diag.show()

    def on_new(self):
        self.PageManager.ThisPage("FormPage")

    def on_database(self):
        self.PageManager.ThisPage("Blank")

    def on_refresh(self):
        self.PageManager.PageRefresh()

    def on_back(self):
        self.PageManager.LastPage()

    def on_next(self):
        self.PageManager.NextPage()
