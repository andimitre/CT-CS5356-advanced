from app import app, db, models
from random import randint
from flask import jsonify, request, Response, json
from twilio.rest import Client
import os

def randNums():
    num = randint(1000, 9999)
    return num

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/createCode', methods=['POST'])
def createCode():
    code = randNums()
    phone = {'phone': request.json['phone'], 'code': code}
    # inst. twilio client
    client = Client(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
    client.api.account.messages.create(
        to=phone['phone'],
        from_="5162899596",
        body=phone['code'])
    # temp_code_holder.append(phone['code'])
    u = models.User(name='man2', phone=phone['phone'], code=phone['code'], is_verified=False)
    db.session.add(u)
    db.session.commit()
    return jsonify(phone)

@app.route('/checkCode', methods=['POST'])
def checkCode():
    code = {'code': request.json['code'], 'phone': request.json['phone']}
    # if code and phone exist authorize user
    user = models.User.query.filter_by(code=code['code'], phone=code['phone']).first()
    if (user):
        user.is_verified = True
        db.session.commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/isVerified', methods=['POST'])
def isVerified():
    data = {'phone': request.json['phone']}
    user = models.User.query.filter_by(phone=data['phone']).first()
    value = False
    if (user):
        value = True if user.is_verified else False
    resp = Response(json.dumps(value), status=200, mimetype='application/json')
    return resp
