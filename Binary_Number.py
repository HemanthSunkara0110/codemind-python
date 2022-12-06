def binn(n):
    vk=[]
    while n>=1:
        vk.append(n%2)
        n=n//2
    vk=vk[::-1]
    return vk
n=int(input())
vk=[]
vk.append([0])
for i in range(1,2**n):
    vk.append(binn(i))
for i in vk:
    a=[]
    i=i[::-1]
    for j in i:
        a.append(j)
    if len(a)!=n:
        for _ in range(len(a),n):
            a.append(0)
    print(*a[::-1],sep='')