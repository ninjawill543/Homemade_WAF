from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        data = request.form['input_data']
        print("Input Data:", data)
    return "Data Received"

if __name__ == "__main__":
    app.run(debug=True)

