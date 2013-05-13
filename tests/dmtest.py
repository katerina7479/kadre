import unittest
from kglobals import DM


class DMTest(unittest.TestCase):

    ClassIsSetup = False
    ClassIsTornDown = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Running Database Manager Tests"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        unittest.TestCase.setUp(self)
        # you want to have persistent things to test
        self.__class__.DM = DM
        # (you can call this later with self.myclass)

    def testTableList(self):
        result = self.DM.GetTableList()
        self.assertEqual(result[0][0], "Tank")

    def testColumns(self):
        result = self.DM.GetColumns("Tank")
        self.assertEqual(result[0], "id")

    def testAddUpdateDelete(self):
        self.myid = self.DM.Add("Tank", {"tag": "TestTank"})
        self.DM.Update("Tank", self.myid, {"maxvolume": 500})
        result = self.DM.Query("Tank", row=self.myid)
        self.assertEqual(result["maxvolume"], 500)
        self.DM.Delete("Tank", self.myid)

    def testQueryAll(self):
        result = self.DM.Query("Tank")
        self.assertEqual(result[0]["tag"], "TNK-XXX")

    def testQueryRow(self):
        result = self.DM.Query("Tank", row=1)
        self.assertEqual(result["maxvolume"], 2000)

    def testQueryWhere(self):
        result = self.DM.Query("Tank", wcol="tag", wval="TNK-XXX")
        self.assertEqual(result[0]["id"], 1)
