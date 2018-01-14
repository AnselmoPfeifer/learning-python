import requests
import json

list_of_hosts = json.loads(open('monitoring_hosts.json').read())


def check_status_url(url):
    try:
        response = requests.get(url, verify=True, timeout=100)
        return response.status_code
    except IOError:
        return 404

for host in list_of_hosts['hosts']:
    print 'Checking url is ok: {}'.format(host['url'])
    print 'HTTP_STTAUS: {}'.format(check_status_url(host['url']))