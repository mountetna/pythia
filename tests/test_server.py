import os
import sys
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
    """Start with a blank database."""
    import json
    url = "/json/"
    post_dict_test1 = {"func": "add", "args": [1,2]}

    post_dict = post_dict_test1
    post_json = json.dumps(post_dict)
    
    a = client.post(url, data=post_json)
    