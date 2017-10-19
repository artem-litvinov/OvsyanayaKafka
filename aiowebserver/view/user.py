import json
import os, sys
import asyncio
from aiohttp import web
sys.path.append(os.path.join(sys.path[0], '../tools'))
from tools.aio_cassandra import create_cassandra

cassandra = create_cassandra()
cassandra.connect(keyspace='users')

async def get_user(id):
    user = (await cassandra.get_from_table_by_id('users', id))[0]
    user = {
        'id': user.uid,
        'type': user.type,
        'name': user.name,
        'contact': user.contact,
    }
    return user

async def get_all_users():
    rows = (await cassandra.exec_query('SELECT * FROM users'))
    users = []
    for row in rows:
        users.append({
            'id': row.uid,
            'type': row.type,
            'name': row.name,
            'contact': row.contact,
        })
    return users

async def user(request):
    user_id = request.match_info['id']
    if user_id == 'all':
        return web.Response(text=json.dumps(await get_all_users()))
    else:
        return web.Response(text=json.dumps(await get_user(user_id)))
