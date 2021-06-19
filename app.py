import logging
import os

import aiohttp_jinja2
import jinja2
from aiohttp import web

from handlers import routes
from utils import get_logger, InitAppException


def init_app() -> web.Application:
    try:
        app = web.Application()
        app.add_routes(routes)
        loader = os.path.join(os.getcwd(), 'templates')
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(loader))
        return app
    except InitAppException as exc:
        logging.exception(exc)


def init_db():
    ...


def init():
    get_logger()
    init_db()
    web.run_app(init_app(), port=8000)


if __name__ == '__main__':
    init()
