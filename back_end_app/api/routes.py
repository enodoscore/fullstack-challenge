import flask
from back_end_app import app
from flask import request, jsonify
import re
from ..db.database import Database

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def build_response_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PATCH")
    return response

@app.route('/api/v1/properties/search', methods=['GET', 'OPTIONS'])
def search():
    query_parameters = request.args
    query = query_parameters.get('search') or ""
    conn = Database().connect()
    conn.row_factory = dict_factory
    cur = conn.cursor()
    found_properties = cur.execute("select a.*, properties.description, properties.id, properties.selected \
                              from addresses a \
                              INNER JOIN properties \
                              ON a.properties_id=properties.id WHERE \
                              LOWER(a.full_address) LIKE ?",
                              ("%{}%".format(query.lower()),)).fetchall()
    response = flask.jsonify(found_properties)
    return build_response_headers(response)

@app.route('/api/v1/properties/<int:id>/update', methods=['PATCH', 'OPTIONS'])
def update(id):

    query_parameters = request.args
    value = query_parameters.get('info')
    database = Database().connect()
    database.row_factory = dict_factory
    cursor = database.cursor()
    prop = cursor.execute("SELECT id FROM properties where id = ?", (id,)).fetchone()
    if prop is None:
        response = flask.jsonify({})
        return build_response_headers(response)
    else:
        cursor.execute("UPDATE properties SET selected = ? WHERE id = ?", (value, id))
        database.commit()
        response = flask.jsonify({})
        return build_response_headers(response)
