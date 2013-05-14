# Sets variable to be used in the kglobals' DM
# to keep testing database and project database separate
# simply call main.py to run, and test.py to test

import unittest
from kglobals import DM

DM.SetPath(True)

# (The lines below are "imported but unused", but that's ok
# unittest main runs all the imported modules.
# import all the test objects here, to run them
from tests.tanktest import TankTest
from tests.dmtest import DMTest
unittest.main()
