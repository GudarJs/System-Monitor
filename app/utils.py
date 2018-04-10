import subprocess
try:
    import json as _json
except ImportError:
    import simplejson as _json


def json(data):
    return _json.dumps(data)

def shutdown():
    subprocess.Popen(['shutdown', '0'])

def reboot():
    subprocess.Popen(['systemctl', 'reboot', '-i'])

def execute(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    return output
