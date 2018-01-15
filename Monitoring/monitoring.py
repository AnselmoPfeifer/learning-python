import json
import os


class Host:
    def __init__(self, name, url, notification):
        self.name = name
        self.url = url
        self.notification = notification


def create_json_file():
    import json
    hosts = {}
    hosts['hosts'] = []
    json = json.dumps(hosts)
    f = open("hosts.json", "w")
    f.write(json)
    f.close()


def check_list_of_host():
    lista= json.loads(open('hosts.json').read())
    if not os.path.exists('hosts.json') and not lista['hosts']:
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
            new_file = open('hosts.json', 'w')
            new_file.write(list_of_hosts)
            new_file.close()

    else:
        list_of_url = json.loads(open(file_name).read())






#check_list_of_host()
# host = Host(name='Test', url='https://www.anselmopfeifer.com', notification=False)


