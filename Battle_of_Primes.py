def prm(vk):
    c=0
    for i in range(1,vk+1):
        if vk%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
vk=a+b
while(vk):
    vk+=1
    if(prm(vk)):
        print(vk-a-b)
        break