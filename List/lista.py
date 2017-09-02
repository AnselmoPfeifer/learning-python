nomes = ['Zero Nome', 'Primeiro Nome', 'Segundo Nome', 'Terceiro Nome', 'Quarto Nome']
print 'Todos os nomes'
print nomes

print ''
print 'Somente um nome'
print nomes[2]

print ''
print 'Alguns da lista'
print nomes[0:3]
print nomes[3]

print ''
print 'Adicionando um nome na lista'
nomes.append('Quinto Nome')
nomes.append(100)
print nomes

print ''
print 'Removendo um nome'
nomes.remove(100)
nomes.remove('Quinto Nome')
print nomes

print ''
print 'Ordenacao de lista'
numeros = [1,2,3,4,5,6,7,9,8]
print numeros[0:4]