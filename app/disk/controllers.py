import asyncio

from sanic import Blueprint
from sanic.response import json

from app.disk.models import Disk


disk_module = Blueprint('disk', url_prefix='/disk')

@disk_module.route('/', methods=['GET'])
async def disk(request):
    return json(Disk())

@disk_module.websocket('/stats')
async def disk_stats(request, ws):
    while True:
        data = Disk().stats()
        await ws.send(data)
        await asyncio.sleep(1)
