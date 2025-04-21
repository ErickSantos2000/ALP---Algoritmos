lista_ordenada = []
while True:
  nome = input('')
  if nome in 'FIM':
      break
  lista_ordenada.append(nome)
  lista_ordenada.sort()
  for i in lista_ordenada:
    print(i)
  print('**FIM**') 
  

