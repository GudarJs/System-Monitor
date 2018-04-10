import asyncio

from sanic import Blueprint
from sanic.response import json

from app.network.models import Network


network_module = Blueprint('network', url_prefix='/network')

@network_module.route('/', methods=['GET'])
async def network(request):
    return json(Network())

@network_module.websocket('/stats')
async def network_stats(request, ws):
    while True:
        data = Network().stats()
        await ws.send(data)
        await asyncio.sleep(1)
