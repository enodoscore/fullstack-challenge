class Address:
  def __init__(self, sheet):
    self.sheet = sheet
  
  def extract(self, row, cursor):
    full_address = self.sheet.cell(row, 0).value
    house_number = self.sheet.cell(row, 24).value
    direction = self.sheet.cell(row, 25).value
    street = self.sheet.cell(row, 26).value
    suffix = self.sheet.cell(row, 27).value
    apt = self.sheet.cell(row, 28).value
    city = self.sheet.cell(row, 29).value
    zip = self.sheet.cell(row, 3).value
    longitude = self.sheet.cell(row, 1).value
    latitude = self.sheet.cell(row, 2).value
    properties_id = cursor.lastrowid

    return (full_address, house_number, direction, street, suffix,
                      apt, city, zip, longitude, latitude, properties_id)