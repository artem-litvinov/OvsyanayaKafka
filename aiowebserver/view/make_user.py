import asyncio
from aiohttp import web

async def make_user(request):
    return web.Response(text='Hello Aiohttp!')