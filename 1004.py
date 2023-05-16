case = int(input())
for c in range(case):
    x1, y1, x2, y2 = map(int, input().split(" "))
    x1_to_x2 = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    number = int(input())
    k = 0#이탈/진입
    for n in range(number):
        x , y, r = map(int, input().split(" "))
        x1_to_x = ((x1-x)**2+(y1-y)**2)**(1/2)
        x2_to_x = ((x2-x)**2+(y2-y)**2)**(1/2)

        if x1_to_x < r:
            if x2_to_x > r:
                k += 1
        elif x1_to_x >= r:
            if x2_to_x < r:
                k += 1
    print(k)