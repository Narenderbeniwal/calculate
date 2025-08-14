from flask import Flask, request, jsonify

app = Flask(__name__)

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if not data or 'operation' not in data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Invalid input! Required fields: operation, num1, num2"}), 400

    operation = data['operation'].lower()
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({"error": "num1 and num2 must be numbers"}), 400

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        return jsonify({"error": "Invalid operation! Use add, subtract, multiply, or divide"}), 400

    return jsonify({"operation": operation, "num1": num1, "num2": num2, "result": result})

if __name__ == '__main__':
    app.run(debug=True)
