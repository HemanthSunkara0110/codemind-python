r=int(input())
v=list(map(int,input().split()))
for k in range(1,max(v)+1):
    l=0
    for i in range(0,len(v)):
        if v[i]%k==0:
            l+=1
    if l==len(v):
        R=k
print(R)