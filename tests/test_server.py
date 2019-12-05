import os
import sys

# setting working directory to the location of the test
curr_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(curr_dir)
sys.path.append("../")

import tempfile
import pytest
import server

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

def test_methods(client):
    import json
    url = "/json/"
    post_dict_test1 = {"func": "add", "args": [1,2]}

    post_dict = post_dict_test1
    post_json = json.dumps(post_dict)
    
    a = client.post(url, data=post_json)
    