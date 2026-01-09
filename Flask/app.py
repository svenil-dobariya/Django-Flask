from flask import Flask, render_template , request
                                                          
app = Flask(__name__)

@app.route('/')
def Home():
    return "<h1>hello World</h1>"
                                                                         
# @app.route('/login/<username>')
# def login(username):
#     return f"<h1>hello {username}</h1>"
                                                              
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    data = {
        'name' : ['nilesh','harshit','harsh','ankit'],
        'age' : [18,20,24,22,45],
    }
    return render_template('about.html', data=data)

@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return f"<h1>Email: {email}, Password: {password}</h1>"
    return render_template('login.html')

@app.route('/calculator', methods = ['GET','POST'])
def calculator():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        return f"<h1>Result: {result}</h1>"
    return render_template('calculator.html')

app.run()