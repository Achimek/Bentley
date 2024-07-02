from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        result = fibonacci(n)
        if result == "Invalid input":
            response = {'error': 'Invalid input'}
            return jsonify(response), 400
        else:
            response = {'number': n, 'fibonacci': result}
            return jsonify(response)
    except (TypeError, ValueError):
        response = {'error': 'Invalid input'}
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
