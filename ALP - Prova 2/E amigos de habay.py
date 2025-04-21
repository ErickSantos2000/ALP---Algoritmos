yes = []
no = []
maior = ''
while (True):
    linha =  input()
    if linha == 'FIM':
        break
    nome, op = map(str, linha.split())
    if (op == 'YES' and nome not in yes):
        yes.append(nome)
        if len(nome) > len(maior):
            maior = nome 
    elif (op == 'NO' and nome not in no):
            no.append(nome)
yes.sort() 
no.sort()
for nome in yes: 
    print(nome)
for nome in no: 
    print(nome)
print('Amigo do Habay:')
print(maior)


























