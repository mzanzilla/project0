from flask import Flask, render_template # Import the class `Flask` from the `flask` module

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    return render_template("index.html")
@app.route("/cardio")
def cardio():
    return render_template("cardio.html")

@app.route("/low_carb_diet")
def low_carb_diet():
    return render_template("low_carb_diet.html")

@app.route("/rpg")
def rpg():
    return render_template("rpg.html")
