import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")
    
from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import flask

import numpy as np
import traceback
from request_handler import execute
from errors import BaseError, Forbidden, Unauthorized, BadRequest, ServerError
from time import time as time_system
from datetime import datetime

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TRAP_HTTP_EXCEPTIONS=True,
    TRAP_BAD_REQUEST_ERRORS=True
)

@app.route('/')
def route_home():
    return "Home"

@app.route('/json/', methods=['POST'])
def route_json():

    try:
        # post request formatted
        post_request = request.get_json(force=True)
        return flask.jsonify(status = 200, 
                             output = execute(post_request))
                             
    # saving throw information for server use, then rethrowing the same error
    except Exception as e:
        # is exception in the group of exceptions
        try:
            except_info = str(datetime.now()), str(time_system()), e.status, traceback.format_exc()
        except:
            except_info = str(datetime.now()), str(time_system()), -1, traceback.format_exc()
        try:
            raise e
        except BadRequest as e:
            return flask.jsonify(status = e.status, 
                                 output = e.msg)
        except:
            e = ServerError()
            return flask.jsonify(status = e.status, 
                                 output = e.msg)
        finally:
            print("-"*40)
            print(*except_info)
            print("-"*40)