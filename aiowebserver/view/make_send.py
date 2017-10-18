import asyncio
from aiohttp import web

async def make_send(request):
    return web.Response(text='Hello Aiohttp!')