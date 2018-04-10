from sanic import Blueprint
from sanic.response import json

from app.os.models import OS


os_module = Blueprint('os', url_prefix='/os')

@os_module.route('/', methods=['GET'])
async def os(request):
    return json(OS())
