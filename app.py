import logging
import os

import aiohttp_jinja2
import jinja2
import socketio
from aiohttp import web

from handlers import routes
from utils import get_logger, InitAppException


def init_app() -> web.Application:
    try:
        sock_io = socketio.AsyncServer()
        app = web.Application()
        app.add_routes(routes)
        loader = os.path.join(os.getcwd(), 'templates')
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(loader))
        sock_io.attach(app)
        return app
    except InitAppException as exc:
        logging.exception(exc)


def init_db():
    ...


def init():
    get_logger()
    init_db()
    logging.info('start serving')
    web.run_app(init_app(), port=8000)
    logging.info('end serving')


if __name__ == '__main__':
    init()
