import jwt
import datetime

app = Flask(__name__)
SECRET = "secret_key"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    if username:
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'msg': 'Missing username'}), 400

@app.route('/data', methods=['GET'])
def data():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'msg': 'Missing token'}), 401
    try:
        jwt.decode(token, SECRET, algorithms=['HS256'])
        return jsonify({'data': 'Protected data'})
    except:
        return jsonify({'msg': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)
