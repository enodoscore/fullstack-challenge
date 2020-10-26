"""
Initialize a sqlite3 to store property data for use with the property search app.
"""
import argparse
import logging
import os
import sqlite3
import warnings
# ignore Pandas spaces warning.
warnings.simplefilter(action='ignore', category=UserWarning)
import pandas

from utils import get_real_path, DB_FILEPATH, TABLENAME


EXCEL_FILEPATH='Enodo_Skills_Assessment_Data_File.xlsx'


def create_db():
    """Create db for property data and return connection to it."""
    real_path = get_real_path(DB_FILEPATH)
    make_dir(real_path)
    logging.warning(f'Creating database at "{real_path}" for property data.')
    return sqlite3.connect(real_path)


def make_dir(real_path):
    dir = os.path.split(real_path)[0]
    if not os.path.exists(dir):
        os.mkdir(dir)


def add_selected_column(db_conn):
    """Add 'selected' column."""
    cur = db_conn.cursor()
    cur.execute(f'ALTER TABLE {TABLENAME} ADD COLUMN SELECTED INTEGER')
    logging.warning(f'Added SELECTED column to {TABLENAME} table.')
    return None


def drop_db():
    db_file = get_real_path(DB_FILEPATH)
    try:
        os.remove(db_file)
    except:
        pass


def extract_cli_args():
    """Parse and return the command line args."""
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--force", help="Force DB creation.", action="store_true")
    return p.parse_args()


def get_create_table_sql(header_cols):
    return (
        f"CREATE TABLE {TABLENAME} "
    )


def get_source_data():
    return pandas.read_excel(get_real_path(EXCEL_FILEPATH))


def have_db():
    return os.path.isfile(get_real_path(DB_FILEPATH))


def load_data_to_table(data, db_conn):
    data.to_sql(name=TABLENAME, con=db_conn)
    logging.warning(f'Loaded source data to {TABLENAME} table.')
    return None


def prepare_db(force=False):
    """Get data, create the db, the table, then load the data."""
    df = get_source_data()

    if force:
        drop_db()

    if have_db():
        logging.warning('Skipping create. DB exists and force not enabled.')
    else:
        db_conn = create_db()
        load_data_to_table(df, db_conn)
        add_selected_column(db_conn)
        db_conn.close()


if __name__ == '__main__':
    args = extract_cli_args()
    if not os.environ.get('APP_ROOT'):
        raise Exception('APP_ROOT environment variable must contain the root of the project.')
    prepare_db(args.force)
