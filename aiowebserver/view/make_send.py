import time
import os, sys
from aiohttp import web
sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra
# from tools.aiokafka_producer import create_producer

cassandra = create_cassandra()
cassandra.connect(keyspace='users')
# producer = create_producer()

async def create_message(req):
    mid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO messages (mid, uid, date, text, status) VALUES ('%s', '%s', '%s', '%s', '%s')" % (mid, req["uid"],  str(time.time()), req["message"], "sending")
    # await producer.send('test-topic', 'message %s sent' % mid)
    return await cassandra.exec_query(query)

async def make_send(request):
    req = await request.post()
    result = await create_message(req)
    return web.Response(text='OK!')
