import time
import os, sys
import asyncio
from aiohttp import web
from aioprometheus import Service, timer

sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra
from tools.metrics import MAKE_USER_REQUEST_TIME, USER_CREATING_TIME

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

@timer(USER_CREATING_TIME)
async def create_user(req):
    uid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO users (id, name, type, contact) VALUES ('%s', '%s', '%s', '%s')" % (uid, req['name'],  req['type'], req['contact'])
    return await cassandra.exec_query(query)


# @timer(MAKE_USER_REQUEST_TIME)
async def make_user(request):
    req = await request.post()
    result = await create_user(req)
    return web.Response(text='OK!')
