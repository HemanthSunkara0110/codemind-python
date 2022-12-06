def rp(n):
    r=int(str(n)[::-1])
    n+=r
    if str(n)==str(n)[::-1]:
        print(n)
        return 0
    else:
        return rp(n)
n=int(input())
rp(n)