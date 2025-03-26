from flask import Flask, jsonify

app = Flask(__name__)

# 根路徑
@app.route('/')
def home():
    return 'Hello, Flask!'

# 自定義 API 路徑
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'name': 'John Doe', 'job': 'Developer'})

if __name__ == '__main__':
    app.run(debug=True)
