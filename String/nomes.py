nome, sobrenome, idade = "Ana", "Julia", 3
text1 = 'python programming for real life networking use'
text2 = 'networking use'
text3 = '     python programming for real life networking use     '
text4 = 'cisco, hp, nortel'

print nome
print sobrenome
print idade

# print id of memory
print id(nome)
print id(sobrenome)
print id(idade)

# print type
print nome.__class__
print sobrenome.__class__
print idade.__class__
# or
print type(nome)
print type(sobrenome)
print type(idade)



# prit functions
print dir(nome)
print
print dir(sobrenome)
print
print dir(idade)

print nome[0:2]
print len(nome)
print len(sobrenome)


print text1.lower()
print text1.upper()
print text1.capitalize()
print text2.find('use')
print text2[11:14]
print text3.strip()
print text3
print text3.replace(' ', '')
print text4.replace(', ', '-')
print text4.split(',')
print " ".join(text4)

if "use" in text1:
    print True
else:
    print False