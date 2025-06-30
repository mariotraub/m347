from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

account_url = "http://localhost:8080/Account"

def add_crypto(user_id: str, amount: str):
    requests.post(f"{account_url}/AddCrypto?userId={user_id}&amount={amount}")


def remove_crypto(user_id: str, amount: str):
    requests.post(f"{account_url}/RemoveCrypto?userId={user_id}&amount={amount}")

def check_friends(user_id: str, friend: str):
    response = requests.get(f"{account_url}/Friends?userId={user_id}")
    data = response.json()
    return any(str(item.get("id")) == str(friend) for item in data)

def check_balance(user_id: str, amount: str):
    response = requests.get(f"{account_url}/Cryptos?userId={user_id}")
    return int(response.text) >= int(amount)


@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    user_id = data.get("id")
    amount = data.get("amount")
    receiverId = data.get("receiverId")

    if not check_friends(user_id, receiverId):
        return jsonify({"error": "Receiver is not a friend"}), 403
    if not check_balance(user_id, amount):
        return jsonify({"error": "Insufficient funds"}), 403

    
    remove_crypto(user_id, amount)
    add_crypto(receiverId, amount)
    return '[]', 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)
