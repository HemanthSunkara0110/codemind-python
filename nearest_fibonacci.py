n=int(input())
l=[]
v=r=0
k=1
for j in range(n):
    l.append(v)
    r=v+k
    v=k
    k=r
    if l[j]>n:
        break
if(l[j]-n==n-l[j-1]):
    print(l[j-1],l[j])
elif(l[j]-n>n-l[j-1]):
    print(l[j-1])
else:
    print(l[j])