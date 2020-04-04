from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/orders', methods=['POST'])
def order_inform():
    customer_name = request.form['name_give']
    count_of_merchandise = request.form['count_give']
    customer_address = request.form['address_give']
    customer_phone_number = request.form['phone_give']


    inform = {
        'name': customer_name,
        'count': count_of_merchandise,
        'address': customer_address,
        'phone_number': customer_phone_number
    }

    db.orders.insert_one(inform)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

