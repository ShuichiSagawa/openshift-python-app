from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from OpenShift!',
        'hostname': socket.gethostname(),
        'version': os.getenv('APP_VERSION', 'v1.0')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
