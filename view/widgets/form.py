from PySide import QtGui
from PySide.QtGui import QFormLayout
from combo import Combo


class Form(QFormLayout):
    def __init__(self, orderlist, *args):
        super(Form, self).__init__()
        self.orderlist = orderlist
        self.HorizontalSpacing = 10
        self._build()

    def _build(self):
        for item in self.orderlist:
            if item["type"] == "textenter":
                item["widget"] = QtGui.QLineEdit(str(item["value"]))
            elif item["type"] == "checkbox":
                item["widget"] = QtGui.QCheckBox()
                item["widget"].setChecked(item["value"])
            elif item["type"] == "combobox":
                item["widget"] = Combo(self)
                item["widget"].addlist(item["list"])
                item["widget"].setCurrentIndex(item["value"]-1)
            elif item["type"] == "button":
                item["widget"] = QtGui.QPushButton(item["text"])
                item["widget"].released.connect(item["callback"])
            else:
                raise(TypeError, "Type %s not yet supported" % item["type"])
            item["labelw"] = QtGui.QLabel(item["label"])
            self.addRow(item["labelw"], item["widget"])

    def Update(self, neworderlist):
        self.clearAll()
        self.orderlist = neworderlist
        self._build()

    def UpdateComboLists(self, combolists):
        i = 0
        for item in self.orderlist:
            if item["type"] == "combobox":
                item["widget"].setList(combolists[i])
                item["widget"].setCurrentIndex(item["value"]-1)
                i += 1

    def getData(self):
        for item in self.orderlist:
            if item["type"] == "textenter":
                item["value"] = item["widget"].text()
            elif item["type"] == "checkbox":
                item["value"] = item["widget"].isChecked()
            elif item["type"] == "combobox":
                comboindex = item["widget"].currentIndex()
                item["value"] = comboindex + 1
        answers = self._parseformdata(self.orderlist)
        return answers

    def clearForm(self):
        for item in self.orderlist:
            if item["type"] == "textenter":
                item["widget"].setText("")
            elif item["type"] == "checkbox":
                item["widget"].setChecked(False)
            elif item["type"] == "combobox":
                item["widget"].setCurrentIndex(-1)

    def _parseformdata(self, formdata):
        answerdict = {}
        for item in formdata:
            try:
                answerdict[item["column"]] = item["value"]
            except KeyError:
                pass
        return answerdict

    def clearAll(self):
        for item in self.orderlist:
            self.removeWidget(item["widget"])
            self.removeWidget(item["labelw"])
            item["widget"].setParent(None)
            item["labelw"].setParent(None)
        del self.orderlist
