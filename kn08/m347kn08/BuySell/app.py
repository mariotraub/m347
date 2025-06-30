from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

account_url = "localhost:8080/Account"

def add_crypto(user_id: int, amount: int):
    requests.post(f"{account_url}/AddCrypto?userId={user_id}&amount={amount}")


def remove_crypto(user_id: int, amount: int):
    requests.post(f"{account_url}/RemoveCrypto?userId={user_id}&amount={amount}")


@app.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    user_id = data.get('id')
    amount = data.get('amount')

    if user_id is None or amount is None or amount < 0:
        return jsonify(False)


    add_crypto(user_id, amount)
    return jsonify(True)

@app.route('/sell', methods=['POST'])
def sell():
    data = request.get_json()
    user_id = data.get('id')
    amount = data.get('amount')

    if user_id is None or amount is None or amount < 0:
        return jsonify(False)

    remove_crypto(user_id, amount)
    return jsonify(True)

if __name__ == '__main__':
    app.run(debug=True)
