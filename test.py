# Sets _TESTING to be used in the kglobals
# to keep testing database and project database separate
# simply call main.py to run, and test.py to test

_TESTING = False


if __name__ == '__main__':
    import unittest
    _TESTING = True
    # (Imported but unused is ok, because unittest main runs all the imported modules.
    # import all the test objects here, to run them
    from tests.tanktest import TankTest
    from tests.dmtest import DMTest
    unittest.main()
