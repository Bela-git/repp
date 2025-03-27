from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# 這一行啟用 CORS，允許所有來源的請求
CORS(app)

# 定義一個 API 路由
@app.route('/api/data')
def get_data():
    return jsonify({'name': 'John Doe', 'job': 'Developer'})

if __name__ == '__main__':
    app.run(debug=True)
