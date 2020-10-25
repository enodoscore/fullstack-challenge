"""
Utility functions for connecting to the database, getting the correct path, etc...
"""
import logging
import os
import sqlite3

DB_FILEPATH='db_data/property.db'
TABLENAME='property'


def check_db():
    real_path = get_real_path(DB_FILEPATH)
    db_conn = None
    try:
        db_conn = sqlite3.connect(real_path)
        return True
    except Exception as e:
        logging.error(f'{e} {real_path}')
    finally:
        if db_conn:
            db_conn.close()


def get_db_conn():
    real_path = get_real_path(DB_FILEPATH)
    return sqlite3.connect(real_path)


def get_db_path():
    """Return the real db path to other modules."""
    return get_real_path(DB_FILEPATH)


def get_real_path(partial):
    """Append the app base to the path. Raise if app base not set."""
    return os.path.join(os.environ['APP_ROOT'], partial)


def get_db(g):
    """Return cached db connector if exists, else get new one."""
    if 'db' not in g:
        g.db = get_db_conn()
        # g.db.row_factory = sqlite3.Row

    return g.db


def get_cursor(g):
    db_conn = get_db(g)
    return db_conn.cursor()
