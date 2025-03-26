from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"name": "John", "job": "Developer"})

if __name__ == '__main__':
    app.run(debug=True)
