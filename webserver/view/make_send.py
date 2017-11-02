import time
import os, sys
import asyncio
from aiohttp import web
from aioprometheus import Service, Summary, timer

sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra
from tools.aiokafka_producer import create_producer
from tools.metrics import PRODUCING_TIME, SEND_MESAGE_REQUEST_TIME, MESSAGE_CREATING_TIME

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

@timer(PRODUCING_TIME)
async def send(mid):
    producer = create_producer()
    await producer.send('test-topic', mid)

@timer(MESSAGE_CREATING_TIME)
async def create_message(req):
    mid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO messages (id, uid, date, text, status) VALUES ('%s', '%s', '%s', '%s', '%s')" % (mid, req["uid"],  str(time.time()), req["message"], "sending")
    await cassandra.exec_query(query)
    await send(mid)
    return mid


# @timer(SEND_MESAGE_REQUEST_TIME)
async def make_send(request):
    req = await request.post()
    result = await create_message(req)
    return web.Response(text=str('OK! mid=%s' % (result)))

