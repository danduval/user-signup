from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def signup_form():

    error_1 = request.args.get("error_1")
    if error_1 == None:
        error_1 = ""

    error_2 = request.args.get("error_2")
    if error_2 == None:
        error_2 = ""

    error_3 = request.args.get("error_3")
    if error_3 == None:
        error_3 = ""

    error_4 = request.args.get("error_4")
    if error_4 == None:
        error_4 = ""

    username = request.args.get("username")
    if username == None:
        username = ''

    return render_template('user-signup.html', error_1=error_1, error_2=error_2, error_3=error_3, error_4=error_4, username=username)

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    password = request.form["password"]
    verification = request.form["verification"]
    email = request.form["email"]

    error_1 = ''
    error_2 = ''
    error_3 = ''
    error_4 = ''

# TO DO: make sure no fields were left empty (except email):

#        return redirect("/?error=") 

# TO DO: validate username: must contain between 3 and 20 characters and no spaces

    if len(username) < 3 or len(username) > 20 or " " in username:
        error_1 = "please enter a valid username"

# TO DO: make sure password and verification match:

    if password != verification:
        error_2 = "password and verification don't match"

# TO DO: make sure no fields were left empty (except email):

    empty = False
    if username == '' or username == None or password == '' or password == None or verification == '' or verification == None:
        empty = True
        error_3 = "please don't submit an empty form, silly"

# TO DO: validate email: must have between 3 and 20 characters, one @, one period, and no spaces

    if len(email) > 0:
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            error_4 = "please submit a valid email address"

# if there was an error, redirect back to the signup form, with error messages displayed

    if error_1 != "" or error_2 != "" or error_3 != "" or error_4 != "":
        return redirect("/?error_1=" + error_1 + "&error_2=" + error_2 + "&error_3=" + error_3 + "&error_4=" + error_4 + "&username=" + username)   

# if there is no error, proceed to the Welcome page.

    if error_1 == "" and error_2 == "" and error_3 == "" and error_4 == "" and empty == False:
        return render_template("welcome.html", name=username)



app.run()