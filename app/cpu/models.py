import psutil
import cpuinfo

from os import getloadavg
from app.utils import json


class CPU():
    def __init__(self):
        self.name = cpuinfo.get_cpu_info()['brand']
        self.number_of_cores = cpuinfo.get_cpu_info()['count']
        self.architecture = cpuinfo.get_cpu_info()['arch']

    def stats(self):
        cores = []
        for core in psutil.cpu_percent(percpu=True):
            cores.append(core)
        return json({
            'cores': cores,
            'load_average': getloadavg()
        })
