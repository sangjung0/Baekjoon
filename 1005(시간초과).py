import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n,k = map(int,sys.stdin.readline().split())
    t = [0] + list(map(int,sys.stdin.readline().split()))
    order = [[] for _ in range(n+1)]
    in_degrees = [0 for _ in range(n+1)]
    time = [0 for _ in range(n+1)]

    for  i in range(k):
        a,b = list(map(int,sys.stdin.readline().split()))
        order[a].append(b)
        in_degrees[b] += 1

    win = int(sys.stdin.readline())
    if sum(t) == 0:
        print(0)
        continue

    stack =[]
    for i in range(n+1):
        if in_degrees[i] == 0:
            stack.append(i)
            time[i] = t[i]
    
    while stack:
        q = stack.pop()
        for i in order[q]:
            in_degrees[i] -= 1
            time[i] = max(time[q] + t[i],time[i])
            if in_degrees[i] == 0:
                stack.append(i)

    print(time[win])
        