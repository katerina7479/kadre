import unittest
from model.tank import Tank


class TankTest(unittest.TestCase):
    # First define a class variable that determines
    # if setUp was ever run
    ClassIsSetup = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Running Object Tests"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        unittest.TestCase.setUp(self)
        # you want to have persistent things to test
        self.__class__.testclass = Tank("XXX", 1200)
        # (you can call this later with self.myclass)

    def testTag(self):
        result = self.testclass.tag
        self.assertEqual(result, "TNK-XXX")

    def testMaxVol(self):
        result = self.testclass.maxvolume
        self.assertEqual(result, 1200)

    def testMinVol(self):
        result = self.testclass.minvolume
        self.assertEqual(result, 120)
