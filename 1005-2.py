import sys
sys.setrecursionlimit(10**6)

def construction(order,key,t,win,save):
    if win in save.keys():
        return save[win]
    
    result = []
    tp = t[win-1]
    if win in key:
        for i in order[win]:
            result.append(tp + construction(order,key,t,i,save))
    else:
        result.append(tp)
    result.sort()
    save[win] = result[-1]
    return result[-1]

case = int(sys.stdin.readline())

for _ in range(case):
    n,k = map(int,sys.stdin.readline().split())
    t = list(map(int,sys.stdin.readline().split()))
    order = []
    o = {}
    for  i in range(k):
        order.append(list(map(int,sys.stdin.readline().split())))

    key = o.keys()
    for i in order:
        if i[1] in key:
            o[i[1]].append(i[0])
        else:
            o[i[1]] = [i[0]]
    win = int(sys.stdin.readline())
    save = {}
    result = construction(o,o.keys(),t,win,save)
    print(result)

##위상정렬 안쓰면 답 없음
#현재 내가 짠 알고리즘은 BFS방법이다