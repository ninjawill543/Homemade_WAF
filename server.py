from flask import Flask,request,redirect,Response, render_template
import requests

app = Flask(__name__)
# logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/xss")
def xss():
    return render_template("xss_test.html")

@app.route("/sql")
def sql():
    return render_template("sql_test.html")

@app.route("/image")
def image():
    return render_template("image_test.html")

@app.route("/submit_sql", methods=["POST"])
def submit_sql():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username} Password: {password}")
        # app.logger.info(f"Username: {username} ; Password: {password};")
    return redirect("/", code=302)

@app.route("/submit_xss", methods=["POST"])
def submit_xss():
    if request.method == "POST":
        input = request.form['input']
        print(f"Input: {input}")
        # app.logger.info(f"XSS input: {input};")
    return redirect("/", code=302)

@app.route("/submit_image", methods=["POST"])
def submit_image():
    if request.method == "POST":
        file = request.form['file']
        print(f"File: {file}")
        # app.logger.info(f"File: {file};")
    return redirect("/", code=302)

if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0') Enable this to open for everyone
    app.run(debug=True, port=6969)
