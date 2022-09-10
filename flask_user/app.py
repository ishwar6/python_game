import json
import logging
import os
import jwt
from functools import wraps
from flask_mongoengine import MongoEngine
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from models.user import ConfigClass ,User
from werkzeug.security import generate_password_hash

load_dotenv()  
do_debug = os.getenv("DEBUG", "False") == "True"



app: Flask = Flask("be_app")
app.config.from_object(ConfigClass)

# Setup Flask-MongoEngine
db = MongoEngine(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
        except:
            return jsonify({
                'message' : 'Token is invalid!!'
            }), 401
        return  f(current_user, *args, **kwargs)
    return decorated


@app.post('/createuser')
@token_required
def index():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    user_name=data.get("username")
    password=data.get("password")
    age = data.get("age")

    if user_name is None:
        return jsonify({"error":"Please enter username"})
    elif password is None:
        return jsonify({"error":"Please enter password"})
    elif age is None or not type(age)==int:
        return jsonify({"error":"Please enter age"})

    check_user = User.objects(username=user_name).first()
    if check_user:
        return jsonify({"error":"Username already taken"})

    try:
        user = User(username=user_name,password=generate_password_hash(password),age=age)
        user.save()
        return jsonify({"Status":True})
    except Exception as e:
        return jsonify({"error":"Error: User Creation Failed"})


if __name__ == '__main__':
    # configure logging
    logging.basicConfig(filename="logs/flask_log.txt",
                        filemode='w+',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

  
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "localhost")
    app.run(debug=do_debug, host="0.0.0.0", port=port)