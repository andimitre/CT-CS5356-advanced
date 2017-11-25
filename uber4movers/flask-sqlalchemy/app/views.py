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
    """
    This is the home or index API
    Call this api to get back "Hello World!"
    ---
    tags:
      - Home
    responses:
      200:
        description: Success
    """
    return "Hello, World!"

@app.route('/createCode', methods=['POST'])
def createCode():
    """
    This is the SMS code API
    Call this api passing a phone number and get back that phone number and its associated code
    ---
    tags:
      - Create SMS code
    parameters:
      - name: body
        in: body
        type: string
        required: true
        description: the phone number
        schema:
          type: object
          properties:
            phone:
              type: string
              description: the phone number
              default: "9999999999"
    responses:
      200:
        description: Success
        schema:
          type: object
          properties:
            code:
              type: integer
              description: the generated SMS code
              default: 2318
            phone:
              type: string
              description: the phone number
              default: "9999999999"
    """
    code = randNums()
    phone = {'phone': request.json['phone'], 'code': code}
    # # inst. twilio client
    client = Client(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
    client.api.account.messages.create(
        to=phone['phone'],
        from_="5162899596",
        body=phone['code'])
    # temp_code_holder.append(phone['code'])
    u = models.User(name='man2', phone=phone['phone'], code=phone['code'], is_verified=False)
    db.session.add(u)
    db.session.commit()
    resp = Response(json.dumps(phone), status=200, mimetype='application/json')
    return resp

@app.route('/checkCode', methods=['POST'])
def checkCode():
    """
    This is the check SMS code endpoint
    Call this api passing an SMS code and get a 200 response if the code and phone number are correct
    ---
    tags:
      - Check SMS code
    parameters:
      - name: body
        in: body
        type: string
        required: true
        description: the phone number
        schema:
          type: object
          properties:
            code:
              type: string
              description: the SMS code
              default: "1234"
            phone:
              type: string
              description: the phone number
              default: "9999999999"
    responses:
      200:
        description: Success
        schema:
          type: string
          default: User and SMS code don't exist
    """
    code = {'code': request.json['code'], 'phone': request.json['phone']}
    # if code and phone exist authorize user
    user = models.User.query.filter_by(code=code['code'], phone=code['phone']).first()
    value = "User and SMS code don't exist"
    if (user):
        user.is_verified = True
        value = "Code exists!"
        db.session.commit()
    resp = Response(json.dumps(value), status=200, mimetype='application/json')
    return resp


@app.route('/isVerified', methods=['POST'])
def isVerified():
    """
    This is the is user verified endpoint
    Call this api passing a phone number to check whether the user is verified
    ---
    tags:
      - Is user verified
    parameters:
      - name: body
        in: body
        type: string
        required: true
        description: the phone number
        schema:
          type: object
          properties:
            phone:
              type: string
              description: the phone number
              default: "9999999999"
    responses:
      200:
        description: Success
        schema:
          type: string
          default: User is not verified
    """
    data = {'phone': request.json['phone']}
    user = models.User.query.filter_by(phone=data['phone']).first()
    value = "Unverified user"
    if (user):
        value = "User is Verified" if user.is_verified else "Unverified user"
    resp = Response(json.dumps(value), status=200, mimetype='application/json')
    return resp


@app.route('/createJob', methods=['POST'])
def createJob():
    return "job created"

@app.route('/isJobAccepted', methods=['POST'])
def isJobAccepted():
    return "job accepted"
