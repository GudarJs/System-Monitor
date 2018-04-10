import asyncio

from sanic import Blueprint
from sanic.response import json

from app.cpu.models import CPU


cpu_module = Blueprint('cpu', url_prefix='/cpu')

@cpu_module.route('/', methods=['GET'])
async def cpu(request):
    return json(CPU())

@cpu_module.websocket('/stats')
async def cpu_stats(request, ws):
    while True:
        data = CPU().stats()
        await ws.send(data)
        await asyncio.sleep(1)
