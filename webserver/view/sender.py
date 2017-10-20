import asyncio
import aiohttp_jinja2
from aiohttp import web

async def sender(request):
    return aiohttp_jinja2.render_template('sender.html', request, {'title': 'Send message'})