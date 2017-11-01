import os
import logging
import asyncio
import jinja2
import aiohttp_jinja2
from aiohttp import web
from routes import setup_routes
from aioprometheus import Service

loop = asyncio.get_event_loop()

async def start_monitor(svr):
    await svr.start(port=8000)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    try:
        WEBSERVER_PORT = os.environ['WEBSERVER_PORT']
    except KeyError as err:
        logger.error("KeyError! Please set WEBSERVER_PORT environment variable! Using port 8080")
        WEBSERVER_PORT=8080
    
    svr = Service(loop=loop)
    app = web.Application()
    setup_routes(app)

    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('view', 'templates'))

    try:
        loop.run_until_complete(start_monitor(svr))
        web.run_app(app, port=int(WEBSERVER_PORT), host='0.0.0.0')
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(svr.stop())
