from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
# from databases import *

app = Flask(__name__)

app.secret_key = "MY_SUPER_SECRET_KEY"



# @app.route("/home",methods=['GET', 'POST'])

# def Signup():

# def anna():
#     if request.method == 'GET':
#         return render_template('home.html')
#     else:
       
#         email = request.form['email']
#         password = request.form["psw"]

#         save_to_database(email,password)        
#         return render_template('homepage.html',
            
#             email= e,
#             password= p

#             )
@app.route('/', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
    	email = request.form['email']
    	password = request.form['password']
    	add_user(email, password)
    	return render_template('homepage.html')
    else:
    	return render_template('home.html')


@app.route('/login', methods= ['GET','POST'])
def login():
	if request.method == 'POST':
		user = queryAllUsers(request.form['email'], request.form["password"])
		if user != None:
			login_session['name'] = user.username
			login_session['logged_in'] = True
			return render_template('homepage.html')
		else:
			return render_template("home.html")
	else:
		return render_template("home.html")

@app.route('/logged-in')
def logged_in():
    return render_template('homepage.html')


@app.route("/home")
def home():return render_template("homepage.html")

@app.route("/abitur")
def streams():
 
   return render_template("streams.html")

@app.route("/lessons")
def lessons():
    return render_template("lessons.html")

# @app.route("/tips")
# def tips():
#     return render_template("tips.html")



if __name__ == '__main__':
	
    app.run(debug=True)


