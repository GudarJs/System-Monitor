import asyncio

from sanic import Blueprint
from sanic.response import json

from app.ram.models import RAM


ram_module = Blueprint('ram', url_prefix='/ram')

@ram_module.route('/', methods=['GET'])
async def ram(request):
    return json(RAM())

@ram_module.websocket('/stats')
async def ram_stats(request, ws):
    while True:
        data = RAM().stats()
        await ws.send(data)
        await asyncio.sleep(1)
