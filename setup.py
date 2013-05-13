from kglobals import DC, TDC


def run():
    DC.CreateDatabase()
    DC.InitializeDatabase()

    TDC.CreateDatabase()
    TDC.InitializeDatabase()


if __name__ == "__main__":
    run()
