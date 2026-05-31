from flask import Flask, request, jsonify
app = Flask(__name__)
users = {'user1': 'password123', 'user2': 'securepass'}
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful', 'token': 'fake-jwt-token'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)