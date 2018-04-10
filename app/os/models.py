import socket
import distro
import platform


class OS():
    def __init__(self):
        self.name = platform.system()
        self.kernel = platform.release()
        self.hostname = socket.gethostname()
        if self.name == 'Linux':
            self.linux_distribution = LinuxDistribution()

class LinuxDistribution():
    def __init__(self):
        self.name = distro.linux_distribution()[0]
        self.version = distro.linux_distribution()[1]
        self.codename = distro.linux_distribution()[2]
