#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
from flask import Flask
from flask_graylog_bundle.server import GraylogAPIServer
from cdumay_rest_client.exceptions import HTTPException, HTTPExceptionValidator

app = Flask(__name__)
app.config.update({
    "GRAYLOG_URL": "http://127.0.0.1:12900",
    "GRAYLOG_USERNAME": "admin",
    "GRAYLOG_PASSWORD": "admin"
})

api = GraylogAPIServer(app)

# or using blueprint:
# from flask.blueprints import Blueprint
# api_bp = Blueprint('auth', __name__)
# api = GraylogAPIServer(api)
#
# app.register_blueprint(api_bp)

if __name__ == '__main__':
    try:
        print(api.client.do_request(
            method="GET",
            path="/users/user1"
        ))
    except HTTPException as exc:
        print(HTTPExceptionValidator().dump(exc).data)
