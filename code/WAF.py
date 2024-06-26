from flask import Flask, request, Response
import requests
import ssl
from werkzeug.middleware.proxy_fix import ProxyFix
import os
from checks.sql import sql_check
import datetime
import checks.bot as bot

Protection = True # Change this to false to view the website with no protection

app = Flask(__name__)

if not os.path.exists("../logs"):
    os.makedirs("../logs")

if not os.path.exists("../uploads"):
    os.makedirs("../uploads")

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

SITE_NAME = "http://localhost:6969"

CSP_POLICY = "default-src 'none'; script-src 'none'; object-src 'none'; base-uri 'none'; connect-src 'self'; img-src 'self'; style-src 'self'; frame-ancestors 'self'; form-action 'self'; upgrade-insecure-requests; require-trusted-types-for 'script'"

BREAK = "~*~"
LOGS = BREAK.join(("{time}", "{addr}", "{method}", "{path}", "{values}", "{mimetype}", "{headers1}", "{headers2}", "{headers3}", "{headers4}\n"))
CHECK_LIMIT = 1 
BAN_LIMIT = 2

@app.before_request 
def before_request_callback():
    if Protection:
        if (request.path == "/sql"):
            sql_check(request.values.get('user'), request.values.get('passw'), request.path, request.method)
        
        with open("../logs/logs.txt", "a") as f:
            f.write(LOGS.format(time=datetime.datetime.now(), addr=request.remote_addr, method=request.method, path=request.path, values=request.values, mimetype=request.mimetype, headers1=request.headers.get('User-Agent'), headers2=request.headers.get('Accept'), headers3=request.headers.get('Content-Type'), headers4=request.headers.get('Content-Length')))

        bot.blacklist(request.remote_addr, CHECK_LIMIT, BAN_LIMIT)
        if bot.check_blacklist(request.remote_addr) == 2:
            return 'hackers gonna hack', 401
        

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        resp = requests.get(SITE_NAME)
    elif request.method == "POST":
        resp = requests.post(SITE_NAME, data=request.form)
    
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    if Protection:
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
    if Protection:
        headers.append(('Content-Security-Policy', CSP_POLICY))
    response = Response(resp.content, resp.status_code, headers)
    return response
    

if __name__ == "__main__":
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('../certs/certificate.crt', '../certs/private.key')
    
    app.run(debug=True, port=8443, ssl_context=context)
