import tabulate

data = [
    {
        'name':  'foo',
        'status': 'enable'
    },
    {
        'name':  'bar',
        'status': 'disable'
    }
]

data.sort()


report = tabulate.tabulate(data, headers='keys', tablefmt='grid')
print report