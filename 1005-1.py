import sys
sys.setrecursionlimit(10**6)

def construction(c,order,win,p=[],n=0):
    check = True
    for i in order[n:]:
        if win == i[1]:
            construction(c,order,i[0],p = p+[win],n = order.index(i))
            check = False
    if check:
        c.append(p+[win])
    return 

case = int(sys.stdin.readline())
for _ in range(case):
    n,k = map(int,sys.stdin.readline().split())
    t = list(map(int,sys.stdin.readline().split()))
    order = []
    for  i in range(k):
        order.append(list(map(int,sys.stdin.readline().split())))
    order.reverse()
    win = int(sys.stdin.readline())
    r = []
    c = []
    construction(c,order,win)
    result = []
    for i in c:
        time = 0
        for j in i:
            time += t[j-1]
        result.append(time)
    result.sort()
    print(result[-1])