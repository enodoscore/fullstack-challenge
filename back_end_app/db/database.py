import sqlite3
import os

class Database:
  DATA_BASE_PATH_NAME = 'enodotest.db'

  def __init__(self):
    self.path = os.path.abspath(os.path.dirname(__file__))

  def connect(self):
    database_path = os.path.join(self.path, self.DATA_BASE_PATH_NAME)
    return sqlite3.connect(database_path)
  