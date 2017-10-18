import asyncio
from aiohttp import web

async def user(request):
    return web.Response(text='Hello Aiohttp!')