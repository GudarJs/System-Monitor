from sanic import Blueprint
from sanic.response import json

from app.cpu.models import CPU
from app.disk.models import Disk
from app.network.models import Network
from app.os.models import OS
from app.ram.models import RAM
from app.utils import shutdown, reboot, execute


main_module = Blueprint('main')

@main_module.route('/')
async def main_handler(request):
    res = {
        'cpu': CPU(),
        'disk': Disk(),
        'network': Network(),
        'os': OS(),
        'ram': RAM(),
    }
    return json(res)
    
@main_module.post('/shutdown')
async def shutdown_handler(request):
    shutdown()
    return json({
        'status': 'ok'
    })
    
@main_module.post('/reboot')
async def reboot_handler(request):
    reboot()
    return json({
        'status': 'ok'
    })
    
@main_module.post('/execute')
async def execute_handler(request):
    command = request.json['command']
    response = execute(command)
    return json({
        'response': response
    })
