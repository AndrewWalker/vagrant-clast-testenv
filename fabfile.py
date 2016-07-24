from fabric.api import env, run, local, cd
from fabtools import require

def get_machine_ports():
    result = local('vagrant ssh-config | grep Port', capture=True)
    lines = result.splitlines()
    ports = [ line.split()[-1] for line in lines ]
    return ports

env.user = 'vagrant'
env.password = 'vagrant'
env.hosts = [ '127.0.0.1:' + p for p in get_machine_ports() ]
env.forward_agent = True

def update_codegen():
    with cd("clast"):
        run("git checkout master")
        run("git pull")
        run("pip install --upgrade -r clastgen/requirements.txt --pre")
        run("python codegen.py")
