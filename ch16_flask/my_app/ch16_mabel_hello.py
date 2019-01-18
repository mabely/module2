from flask import Flask, render_template, request
app = Flask("MyApp")

# function to test 
@app.route("/") #Tells Flask to serve function below to the URL. @ is a decorator. Tells server to 'get' the page
def hello():
    return "<h1 style='font-size:200; margin:50px;'background-color: pink;'>// Hello world</h1>"

# inline styling
@app.route("/contact-us")
def border():
    return "<h1 style='font-size:170; margin:50px;'>// <span style='background-color: pink;'>Contact</span> us</h1>"

# function to test invoking index.html which shows 'Hello' + name given into URL path. css is linked to html page
@app.route("/<name>") 
def hello_you(name):
    return render_template("index.html", name=name.title())

@app.route("/signup", methods=["POST"])
def signup():
    # Tells it to request from the form .form is html element
    form_data = request.form
    email = form_data["email"]
    result="All good"
    print(form_data["email"])
    # does not take more than one return
    # locals() returns lots of keyword arguments. locals means local var, from Flask. W/o it doesn't print email
    return render_template("signup.html", title="Form confirmation", **locals())

app.run(debug=True)

