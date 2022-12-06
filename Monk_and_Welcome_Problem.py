n=int(input())
k=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(len(k)):
    k[i]=k[i]+m[i]
print(*k)