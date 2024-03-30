from flask import Flask,request,redirect,Response, render_template
import requests
import sqlite3
import os

conn = sqlite3.connect('supersecure.db') 
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")                   
conn.commit()

conn.close()

app = Flask(__name__)
# logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/xss")
# def xss():
#     return render_template("xss_test.html")

# @app.route("/sql")
# def sql():
#     return render_template("sql_test.html")

# @app.route("/image")
# def image():
#     return render_template("image_test.html")

# @app.route("/submit_sql", methods=["POST"])
# def submit_sql():
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']
#         print(f"Username: {username} Password: {password}")
#         # app.logger.info(f"Username: {username} ; Password: {password};")
#     return redirect("/", code=302)

# @app.route("/submit_xss", methods=["POST"])
# def submit_xss():
#     if request.method == "POST":
#         input = request.form['input']
#         print(f"Input: {input}")
#         # app.logger.info(f"XSS input: {input};")
#     return redirect("/", code=302)

# @app.route("/submit_image", methods=["POST"])
# def submit_image():
#     if request.method == "POST":
#         file = request.form['file']
#         print(f"File: {file}")
#         # app.logger.info(f"File: {file};")
#     return redirect("/", code=302)

@app.route("/image", methods=["GET", "POST"])
def image():
    if request.method == "GET":
        return render_template("image_test.html")
    elif request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.root_path, '../', file.filename))
        return redirect(request.url)


def getcomments():
    conn = sqlite3.connect("supersecure.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM comments")
    results = cursor.fetchall()
    conn.close()
    return results


@app.route("/delete_comment", methods=["POST"])
def delete_comment():
    if request.method == "POST":
        comment = request.form['comment_id']
        con = sqlite3.connect('supersecure.db')
        c = con.cursor() 
        c.execute(f"DELETE FROM comments WHERE id = ?", (comment,))
        con.commit()
        con.close()
    return redirect("/xss", code=302)

@app.route("/xss", methods=["GET", "POST"])
def xss():
    if request.method == "GET":
        comments = getcomments()
        return render_template("xss_test.html", cmnt=comments)
    elif request.method == "POST":
        input_text = request.form['input']
        print(f"Input: {input_text}")
        comment = request.form['input']
        con = sqlite3.connect('supersecure.db')
        c = con.cursor() 
        c.execute("INSERT INTO comments (text) VALUES (?)", (comment,))
        con.commit()
        con.close()
    return redirect("/xss", code=302)



# def getusers():
#   conn = sqlite3.connect("supersecure.db")
#   cursor = conn.cursor()
#   cursor.execute("SELECT username FROM `users`")
#   results = cursor.fetchall()
#   conn.close()
#   return results

@app.route("/sql", methods=["GET", "POST"])
def sql():
    if request.method == "GET":
        # users = getusers()
        return render_template("sql_test.html")
        # users=""
    elif request.method == "POST":
        user = request.form['user']
        passw = request.form['passw']
        con = sqlite3.connect('supersecure.db')
        c = con.cursor() 
        c.executescript("INSERT INTO users (username, password) VALUES ('%s', '%s')" % (user, passw))
        #c.execute("INSERT INTO users (username,password) VALUES (?,?)",(user,passw) ) Secure
        con.commit()
    # return redirect("/", code=302)
    return redirect("/sql", code=302)

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         return render_template("xss_test.html")
#     elif request.method == "POST":
#         input = request.form['input']
#         print(f"Input: {input}")
#     return redirect("/login", code=302)



if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0') Enable this to open for everyone
    app.run(debug=True, port=6969)
