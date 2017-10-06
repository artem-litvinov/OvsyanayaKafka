import time
import os, sys
try:
    from producer import Producer
except ImportError:
    sys.path.append(os.path.abspath(os.path.join('common'))) # dev
    from producer import Producer
from cassandra.cluster import Cluster
from flask import Flask, jsonify, redirect, request, render_template
try:
    sys.path.append('./gen-py')
    from kafka_message.ttypes import Kafka_Message
except ImportError:
    sys.path.append(os.path.abspath(os.path.join('common','gen-py')))
    from kafka_message.ttypes import Kafka_Message

def create_cassandra_connection(ip):
    try:
        return Cluster([ip])
    except BaseException as e:
        time.sleep(3)
        create_cassandra_connection(ip)

def create_kafka_connection(host, port):
    try:
        return Producer(host, port)
    except BaseException as e:
        time.sleep(3)
        create_kafka_connection(host, port)

def create_app():
    app = Flask(__name__)
    producer = create_kafka_connection('34.214.200.68', '9092')
    cluster = create_cassandra_connection('172.17.0.2')
    session = cluster.connect('users')

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
        req = request.form
        session.execute('USE users')
        uid = str(int(round(time.time() * 1000)))
        print session.execute("INSERT INTO users (uid, name, type, contact) VALUES (%s, %s, %s, %s)", (uid, req["name"],  req["type"], req["contact"]))
        return uid

    @app.route('/send', methods=['POST'])
    def send_message():
        req = request.form
        session.execute('USE users')
        mid = str(int(round(time.time() * 1000)))
        try:
            print session.execute("INSERT INTO messages (mid, uid, date, text, status) VALUES (%s, %s, %s, %s, %s)", (mid, req["uid"],  str(time.time()), req["message"], "sending"))
            producer.send('test-topic', mid)
            return mid
        except BaseException as e:
            print e
            return e

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')