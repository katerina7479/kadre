from kglobals import _PATH
from database_creator import DatabaseCreator
from database_manager import DatabaseManager


class TestDatabaseCreator(DatabaseCreator):
    def __init__(self):
        self.databasePath = _PATH + "\\data\\database\\test.sqlite3"
        self.table_path = _PATH + "\\data\\tables.json"
        self.table_init_path = _PATH + "\\data\\test_db_init.json"
        self.DM = DatabaseManager(self.databasePath)
