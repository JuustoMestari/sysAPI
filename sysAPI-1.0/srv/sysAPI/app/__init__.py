from flask import Flask, render_template, url_for, request
from functools import wraps
from crossdomain import crossdomain
from cmd_ls import *
from cmd_cat import *
from helpers import isauth
from httpError import httperror

app = Flask(__name__)

#add whitelist/blacklist verification?


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isauth(request):
            return httperror('Authentication', 'Authentication Failed!', 403)
        return f(*args, **kwargs)
    return decorated


@app.route("/ls", defaults={'fullpath': ''}, methods=['GET', 'OPTIONS'])
@app.route("/ls/", defaults={'fullpath': ''}, methods=['GET', 'OPTIONS'])
@app.route("/ls/<path:fullpath>", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
@requires_auth
def main_cmd_ls(fullpath):
    return cmd_ls(fullpath)


@app.route("/cat/<path:fullpath>", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
@requires_auth
def main_cmd_cat(fullpath):
    return cmd_cat(fullpath)

@app.route("/test", methods=['GET', 'OPTIONS'])
@crossdomain(origin='*')
@requires_auth
def test():
    return "Authentication works !"

#mainCSS=url_for('static', filename='bootstrap.min.css')
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/help")
def help():
    return render_template('help.html', apiURI=request.url_root)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0",port=8888)