import asyncio
import aiohttp_jinja2
from aiohttp import web

async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, {'title': 'Create user'})