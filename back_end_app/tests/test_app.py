import os
import tempfile
import pytest
from ..app import app
import json


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_get_route(client):
    res = client.get('/api/v1/properties/search?')
    assert res.status_code == 200

def test_get_route_results(client):
    res = client.get('/api/v1/properties/search?Chicago')
    data = json.loads(res.get_data(as_text=True))
    res.assertEqual(data['dummy'], "dummy-value")
