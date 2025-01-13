#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter  

@app.route('/count/<int:parameter>')
def count(parameter):
    try:
        numbers = "\n".join(str(i) for i in range(parameter))
        return numbers + "\n"  
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    try:
        # Perform the math operation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == 'div' and num2 != 0:
            result = num1 / num2
        elif operator == '%' and num2 != 0:
            result = num1 % num2
        else:
            return "Invalid operation or division by zero.", 400
        
        return str(result), 200
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(port=5555, debug=True)
