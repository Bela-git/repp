from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'job': 'Developer'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
