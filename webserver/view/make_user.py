import time
import os, sys
from aiohttp import web
from aioprometheus import Service, Summary, timer

sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('make_user_request_processing_seconds', 'Time spent processing user making request')
USER_CREATING_TIME = Summary('make_user_operation_processing_seconds', 'Time spent processing user making operation')

@timer(USER_CREATING_TIME)
async def create_user(req):
    uid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO users (id, name, type, contact) VALUES ('%s', '%s', '%s', '%s')" % (uid, req['name'],  req['type'], req['contact'])
    return await cassandra.exec_query(query)


@timer(REQUEST_TIME)
async def make_user(request):
    svr = Service(loop=loop)
    svr.registry.register(REQUEST_TIME)
    svr.registry.register(USER_CREATING_TIME)

    req = await request.post()
    result = await create_user(req)
    return web.Response(text='OK!')
