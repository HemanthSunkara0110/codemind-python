v,k,r=map(int,input().split(' '))
c=0;
for v in range(v,k+1,1):
    if(v%r==0):
        c+=1
print(c)
