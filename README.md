# flask-graylog

Graylog extension for Flask

## Quickstart

First, install flask-graylog using [pip](https://pip.pypa.io/en/stable/):

    $ pip install flask-graylog

## Auth extension

To enable Graylog auth, add a `GraylogAuth` instance to your code:

```python
    from flask import current_app as app
    from flask_graylog.auth import GraylogAuth
    
    app.config.update({
       "GRAYLOG_URL": "http://127.0.0.1:12900"
    })
    
    auth = GraylogAuth(app)
    
```

You can take a look at [examples/auth.py](examples/auth.py) for more 
complete example. Flask's 
[application factories](http://flask.pocoo.org/docs/patterns/appfactories/) 
and [blueprints](http://flask.pocoo.org/docs/blueprints/) can be used too.

It provides a login decorator `login_required`. To use it just wrap a view function:

```python
    @app.route('/secret-page')
    @auth.login_required
    def secret_page():
        return jsonify({
            "message": "hello",
            "username": auth.username
        })
```

Additionnal info can be accessed using `g.user` (see: Graylog REST API result of GET /users/{username})

**NOTE:** Graylog tokens are supported, take a look at the Graylog REST API documentation.

## API client

To use query Graylog API, add a `GraylogAPIServer` instance to your code:

```python
    from flask import Flask
    from flask_graylog.server import GraylogAPIServer
    
    app = Flask(__name__)
    app.config.update({
        "GRAYLOG_URL": "http://127.0.0.1:12900",
        "GRAYLOG_USERNAME": "admin",
        "GRAYLOG_PASSWORD": "admin"
    })
    
    api = GraylogAPIServer(app)
    
```

You can take a look at [examples/api.py](examples/api.py) for a complete example.

## License

Apache License 2.0