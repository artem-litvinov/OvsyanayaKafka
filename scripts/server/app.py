import time
from flask import Flask, jsonify, request
from cassandra.cluster import Cluster

app = Flask(__name__)
cluster = Cluster(['localhost'])
session = cluster.connect('users')

@app.route('/user/<id>', methods=['GET'])
def user(id):
    users = []
    session.execute('USE users')
    if id == "all":
        rows = session.execute("SELECT * FROM users")
        for row in rows:
            users.append({
                'type': row.type,
                'user_id': row.user_id,
                'contact': row.contact,
            })
        return jsonify(users)
    else:
        user = session.execute("SELECT * FROM users WHERE user_id='%s'" % (id))[0]
        return jsonify({
            'type': user.type,
            'user_id': user.user_id,
            'contact': user.contact,
        })

@app.route('/user', methods=['POST'])
def create_user():
    req = request.json
    print request
    session.execute('USE users')
    user_id = str(int(round(time.time() * 1000)))
    print req
#    session.execute("INSERT INTO users (user_id, type, contact) VALUES (%s, %s, %s)", (user_id, req["type"], req["contact"]))
    return user_id

if __name__ == '__main__':
    app.run(debug=True)