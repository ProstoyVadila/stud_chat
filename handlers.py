import datetime
import logging
from typing import Any

import aiohttp_jinja2
from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def start_handler(req: web.Request):
    logging.debug('in start handler')
    return


@routes.get('/auth')
@aiohttp_jinja2.template('auth.html')
async def auth_handler(req: web.Request) -> dict[str, Any]:
    logging.debug('in name handler')
    return {
        'current_date': datetime.datetime.now()
    }


@routes.post('/auth')
@aiohttp_jinja2.template('index.html')
async def auth_next_step_handler(req):
    logging.debug('next step')
