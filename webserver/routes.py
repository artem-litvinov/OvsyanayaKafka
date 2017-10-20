import os
import asyncio
from view.user import user
from view.index import index
from view.sender import sender
from view.make_user import make_user
from view.make_send import make_send

routes = [
    ('GET', '/', index, 'root'),
    ('GET', '/index', index, 'index'),
    ('GET', '/sender', sender, 'sender'),
    ('GET', '/user/{id}', user, 'user'),
    ('POST', '/user', make_user, 'make_user'),
    ('POST', '/send', make_send, 'make_send'),
]

def setup_routes(app):
    project_root = os.path.dirname(os.path.abspath(__file__))
    print (project_root)
    app.router.add_static('/pub/',
        path=str(project_root + '/view/pub/'),
        name='pub')

    for r in routes:
        app.router.add_route(r[0], r[1], r[2], name=r[3])