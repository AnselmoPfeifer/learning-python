import json
import sys
import os

class Host:

    def __init__(self, name, url, notification):
        self.name = name
        self.url = url
        self.notification = notification

list_of_hosts = []


def check_list_of_host():
    file_name = 'hosts.json'
    if not os.path.exists('hosts.json') and not list_of_hosts:
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

            new_file = open('hosts.json', 'r')
            new_file.read()

    else:
        list_of_url = json.loads(open(file_name).read())





check_list_of_host()
# host = Host(name='Test', url='https://www.anselmopfeifer.com', notification=False)


