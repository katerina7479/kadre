# I decided to store global items here.
# If an object needs the path to the main directory, to make absolute paths
# I can get it here.
# Also, a single DatabaseManager, and Creator.
# Also, the order of the imports is important, so don't try to
# neaten them up.


import os
from test import _TESTING

_PATH = os.path.dirname(os.path.abspath(__file__))

from controller.database_manager import DatabaseManager
DM = DatabaseManager()

from controller.database_creator import DatabaseCreator
DC = DatabaseCreator(DM)

from controller.test_db_creator import TestDatabaseCreator
TDC = TestDatabaseCreator()
