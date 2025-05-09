import importlib

drivers = ["sqlite3"]

for driver in drivers:
    importlib.import_module(driver)
