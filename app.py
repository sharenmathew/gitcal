from flask import Flask,request,render_template,jsonify
import json


app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to flask"

@app.route("/cal", methods=["GET"] )
def math_operator():
    operation= request.json["operation"]
    number1 =request.json["number1"]
    number2 =request.json["number2"]

    if operation=="add":
        result= int(number1) +int(number2)

    if operation=="subtraction":
        result=  int(number1) -int(number2)

    if operation=="multipy":
        result= int(number1) * int(number2)

    else:
        result= int(number1)/int(number2)

    return jsonify(result)

print(__name__)
if __name__=="__main__":
    app.run(debug=True)