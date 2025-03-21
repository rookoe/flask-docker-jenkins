from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    if num1 is None or num2 is None:
        return 'Both num1 and num2 are required.', 400
    return str(num1 + num2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
