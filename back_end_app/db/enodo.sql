CREATE TABLE properties (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  description TEXT NOT NULL,
  rec_type TEXT NOT NULL,
  pin TEXT NOT NULL,
  ovacls TEXT NOT NULL,
  estimated_market_value REAL NOT NULL,
  location TEXT NOT NULL,
  tax_code REAL NOT NULL,
  neighborhood INTEGER NOT NULL,
  res_type TEXT,
  building_use TEXT,
  selected INTEGER NOT NULL DEFAULT 0, 
  created_at DATETIME NOT NULL DEFAULT current_timestamp,
  updated_at DATETIME NOT NULL DEFAULT current_timestamp,
  CHECK (selected IN (0,1))
);

CREATE TABLE addresses (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  full_address NOT NULL,
	house_number TEXT NOT NULL,
  direction TEXT NOT NULL,
  street TEXT NOT NULL,
  suffix TEXT NOT NULL,
  apt TEXT,
  city TEXT NOT NULL,
  zip INTEGER NOT NULL,
  longitude INTEGER NOT NULL,
  latitude INTEGER NOT NULL,
  properties_id INTEGER,
  created_at DATETIME NOT NULL DEFAULT current_timestamp,
  updated_at DATETIME NOT NULL DEFAULT current_timestamp,
  FOREIGN KEY(properties_id) REFERENCES properties(id)
);

CREATE INDEX idx_properties_id ON properties (id);
CREATE INDEX idx_addresses_id ON addresses (id);
CREATE INDEX idx_addresses_properties_id ON addresses(properties_id);
CREATE INDEX idx_addresses_full_address ON addresses(full_address)