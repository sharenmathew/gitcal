from flask import Flask,request,render_template


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
        result= number1 +number2

    if operation=="subtraction":
        result=  number1 -number2

    if operation=="multipy":
        result= number1 * number2

    else:
        result= number1/number2

    return operation

print(__name__)
if __name__=="__main__":
    app.run(debug=True)