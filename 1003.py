def fibonacci(n,p,x=0,y=0):
    if n in p.keys():
        return p[n]
    elif n == 0:
        return 1,0
    elif n == 1 :
        return 0,1
    else:
        tp1 = n-1
        tp2 = n-2
        p[tp1] = fibonacci(tp1,p)
        p[tp2] = fibonacci(tp2,p)
        x = p[tp1][0] + p[tp2][0]
        y = p[tp1][1] + p[tp2][1]
        return x,y

cs = int(input())
p = {}
for _ in range(cs):
    n = int(input())
    x=0
    y=0
    x,y = fibonacci(n,p)
    print(x,y)

"""def fibonacci(d,n):
    if n == 0:
        d[0] = d[0] + 1
        return
    elif n == 1 :
        d[1] = d[1] + 1
        return
    else:
        fibonacci(d,n-1)
        fibonacci(d,n-2)
        return

cs = int(input())
for _ in range(cs):
    n = int(input())
    d = [0,0]
    fibonacci(d,n)
    print(d[0],d[1])"""
