from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        some_json = request.get_json()
        first_num = int(some_json['first_num'])
        second_num = int(some_json['second_num'])
        result = first_num + second_num
        return jsonify({'result': result})
    else:
        return "Hello :)"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
