from flask import Flask, request, Response
import requests
import ssl
from werkzeug.middleware.proxy_fix import ProxyFix
import os
from checks.sql import sql_check
from checks.image import image_check
import datetime

app = Flask(__name__)

if not os.path.exists("../logs"):
    os.makedirs("../logs")

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

SITE_NAME = "http://localhost:6969"

CSP_POLICY = "default-src 'none'; script-src 'none'; object-src 'none'; base-uri 'none'; connect-src 'self'; img-src 'self'; style-src 'self'; frame-ancestors 'self'; form-action 'self'; upgrade-insecure-requests; require-trusted-types-for 'script'"

@app.before_request 
def before_request_callback():
    if (request.path == "/sql"):
        sql_check(request.values.get('user'), request.values.get('passw'), request.path, request.method)

    if (request.path == "/image"):
        image_check(request.files['file'], request.method)
    
    with open("../logs/logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()};{request.remote_addr};{request.method};{request.path};{request.values};{request.mimetype};{request.headers.get('User-Agent')};{request.headers.get('Accept')};{request.headers.get('Content-Type')};{request.headers.get('Content-Length')}\n")

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        resp = requests.get(SITE_NAME)
    elif request.method == "POST":
        resp = requests.post(SITE_NAME, data=request.form)
    
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    headers.append(('Content-Security-Policy', CSP_POLICY))
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route("/<path:path>", methods=["GET", "POST"])
def proxy(path):
    if request.method == "GET":
        resp = requests.get(f"{SITE_NAME}/{path}")
    elif request.method == "POST":
        if 'file' in request.files:
            file = request.files['file']
            files = {'file': (file.filename, file.stream, file.mimetype)}
            resp = requests.post(f"{SITE_NAME}/{path}", data=request.form, files=files)
        else:  
            resp = requests.post(f"{SITE_NAME}/{path}", data=request.form)
    
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    headers.append(('Content-Security-Policy', CSP_POLICY))
    response = Response(resp.content, resp.status_code, headers)
    return response
    

if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('../certs/certificate.crt', '../certs/private.key')
    
    app.run(debug=True, port=443, ssl_context=context)
