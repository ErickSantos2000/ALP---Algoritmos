a, b, c = list(map(float , input().split()))
delta = b**2 -4*a*c
if delta >0:
   x1=(-b+delta**0.5)/(2*a)
   x2=(-b-delta**0.5)/(2*a)
   print(f'2 {x1:.3f} {x2:.3f}')
elif delta==0:
    x = -b/2*a                
    print(f'1 {x:.3f}') 
else:
     print('0')



