import psutil
from app.utils import json


class Network():
    def __init__(self):
        self.devices = []
        for device in psutil.net_io_counters(pernic=True):
            self.devices.append(device)

    def stats(self):
        devices = []
        for device in psutil.net_io_counters(pernic=True):
            devices.append({
                'label': device,
                'bytes_sent': psutil.net_io_counters(pernic=True)[device][0],
                'bytes_recv': psutil.net_io_counters(pernic=True)[device][1],
                'packets_sent': psutil.net_io_counters(pernic=True)[device][2],
                'packets_recv': psutil.net_io_counters(pernic=True)[device][3],
            })
        return json({
            'devices': devices
        })
