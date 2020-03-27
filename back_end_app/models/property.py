class Property:
  def __init__(self, sheet):
    self.sheet = sheet
  
  
  def extract(self, row):
    description = self.sheet.cell(row, 7).value
    rec_type = self.sheet.cell(row, 4).value
    pin = self.sheet.cell(row, 5).value
    ovacls = self.sheet.cell(row, 6).value
    estimated_market_value = self.sheet.cell(row, 11).value
    location = self.sheet.cell(row, 21).value
    tax_code = self.sheet.cell(row, 22).value
    neighborhood = self.sheet.cell(row, 23).value
    res_type = self.sheet.cell(row, 30).value
    building_use = self.sheet.cell(row, 31).value
    selected = 0

    return (description, rec_type, pin, ovacls, estimated_market_value,
                       location, tax_code, neighborhood, res_type, building_use, selected)