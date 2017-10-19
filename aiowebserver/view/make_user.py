import time
import os, sys
from aiohttp import web
sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

async def create_user(req):
    uid = str(int(round(time.time() * 1000)))
    query = "INSERT INTO users (uid, name, type, contact) VALUES ('%s', '%s', '%s', '%s')" % (uid, req['name'],  req['type'], req['contact'])
    return await cassandra.exec_query(query)

async def make_user(request):
    req = await request.post()
    result = await create_user(req)
    return web.Response(text='OK!')
