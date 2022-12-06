import math
p,r,t=map(int,input().split())
v=p*pow((1+(r/100)),t)
print('%.2f'%v)