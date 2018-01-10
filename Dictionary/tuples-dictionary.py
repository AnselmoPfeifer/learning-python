import json

lista_tipos_de_convites = ['Vip', 'Normal', 'Meia', 'Cortesia']
lista_tipos_de_convites.append('Penetra')

print lista_tipos_de_convites
print lista_tipos_de_convites[1]

tuple_tipos_convites = ('Vip', 60, 'Normal', 50, 'Meia', 30, 'Cortesia', 0)
# tuple_lista_tipos_de_convites.append('Penetra') // Este tipo nao permite append
print tuple_tipos_convites
print tuple_tipos_convites[0:2]

convites_com_valor = {
    'Vip': 60,
    'Normal': 50,
    'Meia': 30,
    'Cortesia': 0
}

print convites_com_valor['Vip']
print convites_com_valor.keys()
print convites_com_valor.values()

DIC = {
    "hosts": [
        {
            "name": "host1",
            "url": "dominio1.com.br",
        },
        {
            "name": "host2",
            "url": "dominio2.com.br",
        },
        {
            "name": "host3",
            "url": "dominio3.com.br",
        }
    ]
}

for k, v in DIC.iteritems():
    print k
    print v

RESULT = json.loads(open('dic.json').read())

for key, value in RESULT['version_map'].iteritems():
    print key
    for app in value['apps']:
        print app['name']
        print app['github'][:7]
        print app.has_key('github')

        if "Admin" in app['name']:
            print 'OK'
        else:
            print 'Not'