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



DEFAULT_DB_FILEPATH=os.path.abspath('../../db_data/property.db')
DEFAULT_EXCEL_FILEPATH=os.path.abspath('../../Enodo_Skills_Assessment_Data_File.xlsx')
TABLENAME='property'


def create_db():
    """Create db for property data and return connection to it."""
    logging.warning(f'Creating database at "{DEFAULT_DB_FILEPATH}" for property data.')
    return sqlite3.connect(DEFAULT_DB_FILEPATH)


def add_selected_column(db_conn):
    """Add 'selected' column."""
    cur = db_conn.cursor()
    cur.execute(f'ALTER TABLE {TABLENAME} ADD COLUMN SELECTED INTEGER')
    logging.warning(f'Added SELECTED column to {TABLENAME} table.')
    return None


def drop_db():
    try:
        os.remove(DEFAULT_DB_FILEPATH)
    except Exception:
        logging.error(f'Could not remove file "{DEFAULT_DB_FILEPATH}"!')
        raise


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
    return pandas.read_excel(DEFAULT_EXCEL_FILEPATH)


def have_db():
    return os.path.isfile(DEFAULT_DB_FILEPATH)


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
    prepare_db(args.force)
