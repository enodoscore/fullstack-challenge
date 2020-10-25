from flask import (
    Blueprint,
    g,
    jsonify,
    request,
    session,
)

from .db import get_cursor, TABLENAME


bp = Blueprint('data', __name__, url_prefix='/data')


@bp.route('/get_autocomplete_values/<string:q>')
def get_autocomplete_values(q):
    cur = get_cursor(g)
    cur.execute(
        f'SELECT class_description, "Full Address" '
        f'FROM {TABLENAME} '
        f'WHERE (selected = 0 or selected is null) '
        f'AND (lower(class_description) like ? or lower("Full Address") like ?)',
        (f'%{q}%', f'%{q}%')
    )
    return jsonify(properties=cur.fetchall())


@bp.route('/set_selected/<int:prop_index>')
def set_selected(prop_index):
    """Set prop_index to selected."""
    cur = get_cursor(g)
    cur.execute(
        f'UPDATE {TABLENAME} SET selected = 1 WHERE "index" = {prop_index}'
    )
    cur.connection.commit()
    return {}


@bp.route('/unset_selected/<int:prop_index>')
def unset_selected(prop_index):
    """Unset selected for prop_index."""
    cur = get_cursor(g)
    cur.execute(
        f'UPDATE {TABLENAME} SET selected = 0 WHERE "index" = {prop_index}'
    )
    cur.connection.commit()
    return {}


@bp.route('/selected_properties')
def selected_properties():
    """Return only the selected properties."""
    cur = get_cursor(g)
    cur.execute(
        f'SELECT "index", class_description, "Full Address" FROM {TABLENAME} WHERE selected = 1'
    )
    return jsonify(properties=cur.fetchall())
