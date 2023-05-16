case = int(input())
result = []
for i in range(case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2: #동일좌표일때
        if r1 == r2:#반지름도 같을때
            if r1 == 0:#반지름이 0일때
                result.append(1)
                continue
            result.append(-1)
            continue
        result.append(0)
        continue

    r = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2) #두 원점의 거리
    tp = r1+r2
    if r > tp:
        result.append(0)
    elif r < tp:
        if r1 + r < r2 or r2 + r < r1:
            result.append(0)
        elif r1+r == r2 or r2+r == r1:
            result.append(1)
        else:
            result.append(2)
    else:
        result.append(1)
for i in result:
    print(i)