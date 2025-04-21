x = int(input())
termos = []
for i in range(1,x+1):
  termos.append(f'1/{i}')
expressao = " + ".join(termos)
print(expressao)