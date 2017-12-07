from app import app, db, models
from random import randint
from flask import jsonify, request, Response, json
from twilio.rest import Client
from datetime import datetime
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
    return "Hello!"

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
    data = {'user_id': request.json['user_id'],'mover_id': request.json['mover_id'],'num_of_rooms': request.json['num_of_rooms'],'start': request.json['start'],'end': request.json['end'], 'price': request.json['price'], 'description': request.json['description'],'is_accepted': request.json['is_accepted']}
    j = models.Jobs(user_id=data['user_id'], mover_id=data['mover_id'], num_of_rooms=data['num_of_rooms'], price=data['price'], description=data['description'], is_accepted=data['is_accepted'])
    # start=datetime(data['start']), end=datetime(data['end'])
    db.session.add(j)
    db.session.commit()
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

@app.route('/getJobs', methods=['GET'])
def getJobs():
    jobs = models.Jobs.query.filter_by(is_accepted=False)
    data = []
    if (jobs):
        for elem in jobs:
            # data[elem.id] = [elem.user_id, elem.mover_id, elem.num_of_rooms,elem.start, elem.end, elem.price, elem.description, elem.is_accepted]
            temp_data = {'id': elem.id, 'user_id': elem.user_id,'mover_id': elem.mover_id,'num_of_rooms': elem.num_of_rooms,'start': elem.start,'end': elem.end, 'price': elem.price, 'description': elem.description,'is_accepted': elem.is_accepted}
            data.append(temp_data)
    else:
        data.append("No data, no bueno")
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp


@app.route('/getUsers', methods=['GET'])
def getUsers():
    user = models.User.query.all()
    data = []
    if (user):
        for elem in user:
            # data[elem.id] = [elem.name, elem.phone, elem.code, elem.is_verified]
            temp_data = {'id': elem.id, 'name': elem.name,'phone': elem.phone, 'code': elem.code,'is_verified': elem.is_verified}
            data.append(temp_data)
    else:
        data.append("No data, no bueno")
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

#
# @app.route('/getJobsByUser', methods=['GET'])
# def getJobsByUser():
#     return "job accepted"

@app.route('/acceptJob', methods=['POST'])
def acceptJob():
    data = {'job_id': request.json['job_id']}
    jobs = models.Jobs.query.filter_by(id=data['job_id']).first()
    value = "Job does not exist"
    if (jobs):
        jobs.is_accepted = True
        value = "Job accepted"
        db.session.commit()
    resp = Response(json.dumps(value), status=200, mimetype='application/json')
    return resp
