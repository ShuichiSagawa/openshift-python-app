from flask import Flask, jsonify
import os
import socket
   
app = Flask(__name__)
   
@app.route('/')
def hello():
    return jsonify({
       'message': 'Hello from OpenShift! (Updated v2.0)',  # 変更
        'hostname': socket.gethostname(),
       'version': os.getenv('APP_VERSION', 'v2.0'),  # 変更
       'new_feature': 'CI/CD Pipeline enabled!'  # 追加
   })
   
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)