a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    l.append(l[i])
print(*l[b:])