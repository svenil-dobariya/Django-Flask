from flask import Flask, render_template , request, jsonify
                                                          
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

@app.route('/calculator', methods = ['GET'])
def calculator():
    return render_template('calculator.html')

@app.route('/api/calculator', methods=['POST'])
def api_calculator():
    data = request.get_json()
    num1 = float(data.get('num1'))
    num2 = float(data.get('num2'))
    operation = data.get('operation')
    
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Error: Division by zero'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'})
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

app.run()