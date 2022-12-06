n=int(input())
c=0
r=0
l=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
if(c==2):
    while(n):
        d=n%10
        r=r*10+d
        n=n//10
    for x in range(1,r+1):
        if(r%x==0):
            l+=1
    if(l==2):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")