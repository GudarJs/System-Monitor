import psutil
from app.utils import json


class RAM():
    def __init__(self):
        self.total = psutil.virtual_memory()[0]
        self.swap_total = psutil.swap_memory()[0]

    def stats(self):
        return json({
            'free': psutil.virtual_memory()[1],
            'swap_free': psutil.swap_memory()[1]
        })
