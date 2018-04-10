import psutil
from app.utils import json


class Disk():
    def __init__(self):
        self.partitions = []
        for partition in psutil.disk_partitions():
            total_size = psutil.disk_usage(partition[1])[0]
            self.partitions.append({
                'label': partition[0],
                'total_size': total_size
            })

    def stats(self):
        partitions = []
        for partition in psutil.disk_partitions():
            free_size = psutil.disk_usage(partition[1])[2]
            partitions.append({
                'label': partition[0],
                'free_size': free_size
            })
        stats = []
        for stat in psutil.disk_io_counters(perdisk=True):
            stats.append({
                'label': stat,
                'read_count': psutil.disk_io_counters(perdisk=True)[stat][0],
                'write_count': psutil.disk_io_counters(perdisk=True)[stat][1],
                'read_bytes': psutil.disk_io_counters(perdisk=True)[stat][2],
                'write_bytes': psutil.disk_io_counters(perdisk=True)[stat][3],
            })
        return json({
            'partitions': partitions,
            'stats': stats
        })
