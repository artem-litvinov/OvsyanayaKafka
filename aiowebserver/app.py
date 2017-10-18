import os
import logging
import asyncio
import jinja2
import aiohttp_jinja2
from aiohttp import web
from routes import setup_routes

if __name__ == '__main__':
    WEBSERVER_PORT=8080
    logger = logging.getLogger(__name__)
    
    '''
        try:
            WEBSERVER_PORT = os.environ['WEBSERVER_PORT']
        except KeyError as err:
            logger.error("KeyError! Please set WEBSERVER_PORT environment variable")
            raise

        try:
            KAFKA_HOST = os.environ['KAFKA_HOST']
        except KeyError as err:
            logger.error("KeyError! Please set KAFKA_HOST environment variable")
            raise

        try:
            CASSANDRA_HOST = os.environ['CASSANDRA_HOST']
        except KeyError as err:
            logger.error("KeyError! Please set CASSANDRA_HOST environment variable")
            raise
    '''

    app = web.Application()
    setup_routes(app)
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('view', 'templates'))
    web.run_app(app, port=int(WEBSERVER_PORT), host='0.0.0.0')