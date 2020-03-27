import re
import xlrd
import sqlite3
import os
from models.property import Property
from models.address import Address

DATA_IMPORT_FILE_PATH = './data/Enodo_Skills_Assessment_Data_File.xlsx'
SHEET_NAME = 'Sheet1'
DATA_BASE_PATH_NAME = './db/enodotest.db'

my_path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(my_path, DATA_IMPORT_FILE_PATH)

book = xlrd.open_workbook(data_path, on_demand = True)
sheet = book.sheet_by_name(SHEET_NAME)

database_path = os.path.join(my_path, DATA_BASE_PATH_NAME)
database = sqlite3.connect(database_path)
cursor = database.cursor()

PROPERTIES_QUERY = """INSERT INTO properties (description, rec_type, pin, ovacls, estimated_market_value, location, tax_code, neighborhood, res_type, building_use, selected) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
ADDRESSES_QUERY = """INSERT INTO addresses (full_address, house_number, direction, street, suffix, apt, city, zip, longitude, latitude, properties_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

for r in range(1, sheet.nrows):
    # extract property values
    property_values = Property(sheet)
    cursor.execute(PROPERTIES_QUERY, property_values.extract(r))
    # extract address values
    address_values = Address(sheet)
    cursor.execute(ADDRESSES_QUERY, address_values.extract(r, cursor))

cursor.close()
database.commit()
database.close()
print("")
print("Data successfully imported")
rows = str(sheet.nrows)
print(rows + " were just imported into Enodo DB")
