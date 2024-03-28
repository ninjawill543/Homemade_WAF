from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        username = request.form['username']
        print("Username:", username)
        password = request.form['password']
        print("Password:", password)
        file = request.form['file']
        print("File:", file)
    return "Data Received"

if __name__ == "__main__":
    app.run(debug=True)

