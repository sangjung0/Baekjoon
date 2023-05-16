import sys

T = int(sys.stdin.readline())
reuslt = 0

def connect(N_A,N,num,W,typ =0):
    global result
    a = (num+1)%N
    b = (num+N-1)%N
    u = (num + N)%(N*2)
    if num+1 > N:
        a += N
        b += N

    #print(num,a,b,u)
    #print(N_A)
    d = {a:0,b:0,u:0}
    if N_A[num] + N_A[a] <= W and a != num and N_A[a] != 0:
        d[a] = N_A[num] + N_A[a]
    if N_A[num] + N_A[b] <= W and b != num and N_A[b] != 0:
        d[b] = N_A[num] + N_A[b]
    if N_A[num] + N_A[u] <= W and u != num and N_A[u] != 0:
        d[u] = N_A[num] + N_A[u]

    key = sorted(d, key= lambda x : d[x],reverse=True)

    check = 0
    if d[key[0]] == 0:
        if typ==0:
            N_A[num] =0
            result += 1
            return False
        else:
            return True
    else:
        N_A[num] = 0
        for i in key:
            if d[i] != 0:
                if typ != 0:
                    if d[i] > typ:
                        check = connect(N_A,N,i,W,typ = d[i])
                else:
                    check = connect(N_A,N,i,W,typ =d[i])
                if check:
                    N_A[i] = 0
                    result += 1
                    return False
        return True

for _ in range(T):
    N,W = map(int,sys.stdin.readline().split())
    N_1 = list(map(int,sys.stdin.readline().split()))
    N_2 = list(map(int,sys.stdin.readline().split()))
    N_A = N_1+N_2

    result = 0
    while (sum(N_A) != 0 ):
        num = N_A.index(max(N_A)) #최댓값으로 시작해보기
        connect(N_A,N,num,W)

    print(result)