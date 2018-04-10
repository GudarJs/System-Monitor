from sanic import Sanic
from sanic_cors import CORS

from app.cpu.controllers import cpu_module
from app.disk.controllers import disk_module
from app.main.controllers import main_module
from app.network.controllers import network_module
from app.os.controllers import os_module
from app.ram.controllers import ram_module

app = Sanic()
CORS(app)

app.config.from_object('config')

# Register blueprints
app.register_blueprint(cpu_module)
app.register_blueprint(disk_module)
app.register_blueprint(main_module)
app.register_blueprint(network_module)
app.register_blueprint(os_module)
app.register_blueprint(ram_module)
