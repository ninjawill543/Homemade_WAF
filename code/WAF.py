from flask import Flask,request,redirect,Response,abort
import requests
import datetime 

app = Flask(__name__)
SITE_NAME = "http://localhost:6969"

@app.before_request 
def before_request_callback():
    pls = True
    if (pls != True):
        abort(400, 'no good')
    
    # Maybe rather than writing to logs, we check in real time and then abort if not good
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()};{request.remote_addr};{request.method};{request.path};{request.values};{request.mimetype};{request.headers.get('User-Agent')};{request.headers.get('Accept')};{request.headers.get('Content-Type')};{request.headers.get('Content-Length')}\n")

@app.route("/",methods=['GET','POST'])
def index():
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

@app.route("/xss", methods=['GET','POST'])
def xss():
    # input_data = request.form['input']
    # return f"XSS Input: {input_data}"
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}/xss")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}/xss",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

@app.route("/delete_comment", methods=['POST'])
def delete_comment():
    global SITE_NAME
    if request.method=="POST":
        resp = requests.post(f"{SITE_NAME}/delete_comment",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

@app.route("/sql", methods=['GET','POST'])
def sql():
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}/sql")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}/sql",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    # username = request.form['username']
    # password = request.form['password']
    # return f"Username: {username}, Password: {password}"


@app.route("/image", methods=['GET','POST'])
def image():
    global SITE_NAME
    if request.method=="GET":
        resp = requests.get(f"{SITE_NAME}/image")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method=="POST":
        resp = requests.post(f"{SITE_NAME}/image",data=request.form)
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    # file_data = request.form['file']
    # return f"File: {file_data}"

# @app.route("/<path:path>",methods=["GET","POST"])
# def proxy(path):
#     global SITE_NAME
#     if request.method=="GET": 
#         resp = requests.get(f"{SITE_NAME}/{path}")
#         excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
#         headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
#         response = Response(resp.content, resp.status_code, headers)
#         return response
#     elif request.method=="POST":
#         resp = requests.post(f"{SITE_NAME}/{path}",data=request.form)
#         excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
#         headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
#         response = Response(resp.content, resp.status_code, headers)
#         return response



if __name__ == "__main__":
    app.run(debug = True,port=5000)
