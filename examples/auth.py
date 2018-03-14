#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""
from flask import Flask, jsonify
from flask_graylog_bundle.auth import GraylogAuth
from cdumay_error import Error, ErrorSchema

app = Flask(__name__)
app.config.update({
    "GRAYLOG_API_URL": "http://127.0.0.1:12900"
})

auth = GraylogAuth(app)


# or using blueprint:
# from flask.blueprints import Blueprint
# auth_bp = Blueprint('auth', __name__)
# auth = GraylogAuth(auth_bp)
#
# app.register_blueprint(auth_bp)

@app.route('/secret-page')
@auth.login_required
def secret_page():
    return jsonify({
        "message": "hello",
        "username": auth.username
    })


# custom handler for full REST API
@app.errorhandler(Error)
def default_exception(error):
    """docstring for default_exception"""
    return jsonify(ErrorSchema().dump(error)), error.code


if __name__ == '__main__':
    app.run()
