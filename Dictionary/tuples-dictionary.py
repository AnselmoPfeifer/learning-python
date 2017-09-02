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