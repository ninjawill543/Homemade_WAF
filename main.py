from flask import Flask, render_template, request
import logging

app = Flask(__name__)
logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        file = request.form['file']
        app.logger.info(f"Username: {username} ; Password: {password} ; File: {file}")
    return "Data received"

if __name__ == "__main__":
    app.run(debug=True)
