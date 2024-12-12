from flask import Flask, request, jsonify, render_template
import calculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = calculator.add(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = calculator.subtract(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = calculator.multiply(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    result = calculator.divide(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/complex_add', methods=['POST'])
def complex_add():
    data = request.get_json()
    result = calculator.complex_add(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/complex_subtract', methods=['POST'])
def complex_subtract():
    data = request.get_json()
    result = calculator.complex_subtract(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/complex_multiply', methods=['POST'])
def complex_multiply():
    data = request.get_json()
    result = calculator.complex_multiply(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/complex_divide', methods=['POST'])
def complex_divide():
    data = request.get_json()
    result = calculator.complex_divide(data['a'], data['b'])
    return jsonify(result=result)

@app.route('/logarithm', methods=['POST'])
def logarithm():
    data = request.get_json()
    result = calculator.logarithm(data['a'], data['base'])
    return jsonify(result=result)

@app.route('/mean', methods=['POST'])
def mean():
    data = request.get_json()
    result = calculator.mean(data['data'])
    return jsonify(result=result)

@app.route('/median', methods=['POST'])
def median():
    data = request.get_json()
    result = calculator.median(data['data'])
    return jsonify(result=result)

@app.route('/standard_deviation', methods=['POST'])
def standard_deviation():
    data = request.get_json()
    result = calculator.standard_deviation(data['data'])
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
