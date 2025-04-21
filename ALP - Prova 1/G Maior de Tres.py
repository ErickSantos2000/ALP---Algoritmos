

a =int(input())
b =int(input())
c =int(input())
if a<b<c:
   print(f"{c} {b} {a}",end=" ")
elif a<c<b:
   print(f"{b} {c} {a}",end=" ")
elif b<a<c:
   print(f"{c} {a} {b}",end=" ")
elif b< c <a:
  print(f"{a} {c} {b}",end=" ")
elif c < a <b:
  print(f"{b} {a} {c}",end=" ")
else:
  print(f"{a} {b} {c}",end=" ")

