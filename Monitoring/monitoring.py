import json
import os

HOSTS_FILE = 'hosts.json'

class Host:
    def __init__(self, name, url, notification):
        self.name = name
        self.url = url
        self.notification = notification


def create_json_file():
    hosts = {}
    hosts['hosts'] = []
    content = json.dumps(hosts)
    if not os.path.exists(HOSTS_FILE):
        f = open(HOSTS_FILE, "w")
        f.write(content)
        f.close()


def read_json_file():
    return json.loads(open(HOSTS_FILE).read())


def check_exist_hosts():
    list = read_json_file()
    if list['hosts']:
        return True
    else:
        return False


def update_host_list():
    create_json_file()
    list_of_hosts = []

    if not check_exist_hosts():
        print 'Deseja cadastrar novas urls?'
        res = raw_input()
        if res == 'Y':
            print 'Qual o nome do host?'
            name = raw_input()
            print 'Qual a URL?'
            url = raw_input()
            print 'Deseja notificao para esta URL?'
            notification = raw_input()
            if notification == 'Y':
                notification = True
            elif notification == 'N':
                notification = False
            else:
                notification = ''
            host = Host(name=name, url=url, notification=notification)
            list_of_hosts.append(host)


            # TODO update file list
            # new_file = open(HOSTS_FILE, 'w')
            # new_file.write(list_of_hosts)
            # new_file.close()



# TODO create get request urls