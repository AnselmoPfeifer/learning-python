#!/usr/bin/python
import os
import subprocess
import json

from jinja2 import Environment
from jinja2 import FileSystemLoader

# sed "s/<replace>/$node/g" /etc/docker-gc/job-docker-gc.yaml > /etc/docker-gc/job.yaml
# env = Environment(loader=FileSystemLoader('jenkins/scheduler/files'))
# env.get_template('job-docker-gc.jinja').render({'node': node})#


def replace_name_job(node):
    template = 'job-docker-gc.jinja'
    target = 'etc/docker-gc/{}.yaml'.format(node)
    env = Environment(loader=FileSystemLoader(''))
    with open(target, 'w') as file_target:
        file_target.write(env.get_template(template).render({'node': node}))


def get_nodes_by_name():
    cmd = ["kubectl", "get", "nodes", "-o", "json"]
    print(cmd)
    out = subprocess.check_output(cmd)
    nodes = json.loads(out)
    return nodes


def get_all_jobs():
    cmd = "kubectl get job --namespace=jenkins"
    jobs = os.system(cmd)
    return jobs


def create_jobs():
    print ('Starting process of Create Jobs')
    nodes = get_nodes_by_name()
    print('nodes: {}'.format(nodes))
    for node in nodes:
        node_name = node
        print(node_name)
        replace_name_job(node_name)
        # cmd = "kubectl create -f /etc/docker-gc/job.yaml"
        # return os.system(cmd)

create_jobs()
