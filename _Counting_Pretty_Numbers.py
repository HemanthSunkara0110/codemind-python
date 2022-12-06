n=int(input())
for i in range(1,n+1,1):
    v,k=map(int,input().split())
    r=0
    for j in range(v,k+1,1):
        if j%10==2 or j%10==3 or j%10==9:
            r+=1
    print(r,end='
')