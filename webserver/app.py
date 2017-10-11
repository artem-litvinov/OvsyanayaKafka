import os
import time
from producer import Producer

from cassandra.cluster import Cluster
from flask import Flask, jsonify, redirect, request, render_template

def create_app(session, producer):
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='Create user')

    @app.route('/sender')
    def sender():
        return render_template('sender.html', title='Send message')

    @app.route('/user/<id>', methods=['GET'])
    def user(id):
        users = []
        session.execute('USE users')
        if id == "all":
            rows = session.execute("SELECT * FROM users")
            for row in rows:
                users.append({
                    'uid': row.uid,
                    'name': row.name,
                    'type': row.type,
                    'contact': row.contact,
                })
            return jsonify(users)
        else:
            user = session.execute("SELECT * FROM users WHERE uid='%s'" % (id))[0]
            return jsonify({
                'uid': user.uid,
                'name': user.name,
                'type': user.type,
                'contact': user.contact,
            })

    @app.route('/user', methods=['POST'])
    def create_user():
        req = request.json
        session.execute('USE users')
        uid = str(int(round(time.time() * 1000)))
        print session.execute("INSERT INTO users (uid, name, type, contact) VALUES (%s, %s, %s, %s)", (uid, req["name"],  req["type"], req["contact"]))
        return uid

    @app.route('/send', methods=['POST'])
    def send_message():
        req = request.json
        session.execute('USE users')
        mid = str(int(round(time.time() * 1000)))
        print session.execute("INSERT INTO messages (mid, uid, date, text, status) VALUES (%s, %s, %s, %s, %s)", (mid, req["uid"],  str(time.time()), req["message"], "sending"))
        producer.send('test-topic', mid)
        return mid

    return app

if __name__ == '__main__':
    try:
        WEBSERVER_PORT = os.environ['WEBSERVER_PORT']
    except KeyError as err:
        print(err, "Please set WEBSERVER_PORT environment variable")
        raise

    try:
        KAFKA_HOST = os.environ['KAFKA_HOST']
    except KeyError as err:
        print(err, "Please set KAFKA_HOST environment variable")
        raise

    try:
        CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
    except KeyError as err:
        print(err, "Please set CASSANDRA_HOST environment variable")
        raise

    app = create_app(Cluster([CASSANDRA_HOST]).connect('users'), Producer(KAFKA_HOST, '9092'))
    app.run(debug=True, port=int(WEBSERVER_PORT), host='0.0.0.0')
