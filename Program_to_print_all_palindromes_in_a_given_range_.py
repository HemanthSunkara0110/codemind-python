v=int(input())
k=int(input())
for i in range(v,k+1,1):
    t=i
    s=0
    while(i>0):
        r=i%10
        s=s*10+r
        i=i//10
    if(t==s):
        print(t,end=' ')