from flask import Flask, render_template, url_for, request
from math import sin, cos, tan, sqrt, exp, log, acosh, asinh, atanh, asin, acos

app = Flask(__name__)

@app.route("/")
def main():
    return render_template ("index.html")

@app.route("/basic-calculator")
def basic():
    return render_template ("basic-calculator.html")

@app.route("/advanced-calculator")
def advanced():
    return render_template ("advanced-calculator.html")

@app.route("/basic-result", methods=["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "addition was perfomed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "subtraction was perfomed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "multiplication was perfomed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "division was perfomed successfully"
    else:
        note = "There is an error, please try again!"
        color = "alert-danger"
        return render_template("basic-calculator.html", note=note, color=color)
    return render_template("basic-calculator.html", result = result, note=note, color=color)

@app.route("/advanced-result", methods=["post"])
def advanced_calculate():
    number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    note = ""
    color = "alert-success"
    try:
        if operation == "sin":
            result = sin(number)
            note = "sin has been calculated"
        elif operation == "cos":
            result = cos(number)
            note = "cos has been calculated"
        elif operation == "tan":
            result = tan(number)
            note = "tan has been calculated"
        elif operation == "sqrt":
            result = sqrt(number)
            note = "square root has been calculated"
        elif operation == "exp":
            result = exp(number)
            note = "square root has been calculated"
        elif operation == "log":
            result = log(number)
            note = "square root has been calculated"
        elif operation == "acosh":
            result = acosh(number)
            note = "square root has been calculated"
        elif operation == "asinh":
            result = asinh(number)
            note = "square root has been calculated"
        elif operation == "atanh":
            result = atanh(number)
            note = "square root has been calculated"
        elif operation == "asin":
            result = asin(number)
            note = "square root has been calculated"
        elif operation == "acos":
            result = acos(number)
            note = "square root has been calculated"
        else:
            note = "There is an error, please try again!"
            color = "alert-danger"
            return render_template("advanced-calculator.html", note=note, color=color)
    except ValueError:
        return render_template("advanced-calculator.html", result = 0, note="Error!", color="alert-danger")
    return render_template("advanced-calculator.html", result = result, note=note, color=color)

if __name__ == "__main__":
    app.run(debug = True)