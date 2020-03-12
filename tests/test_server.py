import os
import sys

# setting working directory to the location of the test
curr_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(curr_dir)
sys.path.append("../")

import tempfile
import pytest
import server
import json

@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        ctx = server.app.app_context()
        ctx.push()
        yield client
        ctx.pop()
        
    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])

def post(client, request):
    return client.post("/", data=json.dumps(request))
    
## Testing add function
def test_testing_add_function(client):
    a = post(client, {"func": "add", "args": [1,2]})
    assert a.json["status"] == 200

## Testing add function
def test_expects_func_argument(client):
    a = post(client, {"args": [1,2]})
    assert a.json["status"] == 422, str(a.json["status"])

