from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route("/")
def Signup():
	return render_template("home.html")

@app.route("/home")
def home():
	return render_template("homepage.html")

@app.route("/abitur")
def streams():
	return render_template("streams.html")

@app.route("/subjects")
def subjects():
	return render_template("subjects.html")

@app.route("/topics")
def topics():
	return render_template("topics.html")



if __name__ == '__main__':
    app.run(debug=True)	


