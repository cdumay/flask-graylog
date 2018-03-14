#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
from flask import Flask
from flask_graylog_bundle.server import GraylogAPIServer
from cdumay_error import Error, ErrorSchema

app = Flask(__name__)
app.config.update({
    "GRAYLOG_API_URL": "http://127.0.0.1:12900",
    "GRAYLOG_API_USERNAME": "admin",
    "GRAYLOG_API_PASSWORD": "admin"
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
    except Error as exc:
        print(ErrorSchema().dump(exc))
