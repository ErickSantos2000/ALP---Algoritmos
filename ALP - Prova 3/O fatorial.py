def fat(n):
  if n == 0 or n == 1:
      return 1
  return n * fat(n - 1)

while True:
    n = int(input())
    print(fat(n))
    if n == 0:
      break
      
