import time
import os, sys
import asyncio
from aiohttp import web
from prometheus_client import Summary

sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra
from tools.aiokafka_producer import create_producer

loop = asyncio.get_event_loop()

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('make_send_request_processing_seconds', 'Time spent processing send message request')

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

async def send(mid):
    producer = create_producer()
    await producer.send('test-topic', mid)

async def create_message(req):
    mid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO messages (id, uid, date, text, status) VALUES ('%s', '%s', '%s', '%s', '%s')" % (mid, req["uid"],  str(time.time()), req["message"], "sending")
    await cassandra.exec_query(query)
    loop.run_until_complete(send(mid))
    return mid


@REQUEST_TIME.time()
async def make_send(request):
    req = await request.post()
    result = await create_message(req)
    return web.Response(text=str('OK! mid=%s' % (result)))
