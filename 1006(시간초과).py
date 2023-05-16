import sys

T = int(sys.stdin.readline())
reuslt = 0

def connect(N_A,N,num,W,typ =0):
    global result
    if num+1 > N:
        a = (num+1)%N + N
        b = (num+N-1)%N + N
    else:
        a = (num+1)%N
        b = (num+N-1)%N
    u = (num + N)%(N*2)

    d = {a:0,b:0,u:0}
    if N_A[num] + N_A[a] <= W and a != num:
        d[a] = N_A[num] + N_A[a]
    if N_A[num] + N_A[b] <= W and b != num:
        d[b] = N_A[num] + N_A[b]
    if N_A[num] + N_A[u] <= W and u != num:
        d[u] = N_A[num] + N_A[u]

    key = sorted(d, key= lambda x : d[x],reverse=True)

    check = 0
    if d[key[0]] == 0:
        if typ==0:
            N_A[num] = W+1
            result += 1
            return False
        else:
            return True
    else:
        N_A[num] = W+1
        for i in key:
            if d[i] != 0:
                if typ != 0:
                    if d[i] > typ:
                        check = connect(N_A,N,i,W,typ = d[i])
                else:
                    check = connect(N_A,N,i,W,typ =d[i])
                if check:
                    N_A[i] = W+1
                    result += 1
                    return False
        return True

for _ in range(T):
    N,W = map(int,sys.stdin.readline().split())
    N_1 = list(map(int,sys.stdin.readline().split()))
    N_2 = list(map(int,sys.stdin.readline().split()))
    N_A = N_1+N_2

    CHECK = N*2*(W+1)
    result = 0
    while (sum(N_A) < CHECK ):
        num = N_A.index(min(N_A)) #최댓값으로 시작해보기
        connect(N_A,N,num,W)

    print(result)