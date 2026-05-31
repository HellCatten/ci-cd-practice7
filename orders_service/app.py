from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
orders = []
@app.route('/create_order', methods=['POST'])
def create_order():
    auth_token = request.headers.get('Authorization')
    if not auth_token:
        return jsonify({'message': 'Unauthorized'}), 403
    auth_response = requests.post('http://auth_service:5001/login', json={'username':
        'user1', 'password': 'password123'})
    if auth_response.status_code != 200:
        return jsonify({'message': 'Authentication failed'}), 403

    data = request.json
    order_id = len(orders) + 1
    orders.append({'order_id': order_id, 'item': data.get('item')})
    return jsonify({'message': 'Order created', 'order_id': order_id}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)