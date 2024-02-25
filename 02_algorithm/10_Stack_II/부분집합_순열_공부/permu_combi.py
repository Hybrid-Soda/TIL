def permu(i):
    if i == N:
        print(*P)
    for j in range(i, N):
        P[i], P[j] = P[j], P[i]
        permu(i+1)
        P[i], P[j] = P[j], P[i]

N = 4
P = ['A', 'B', 'C', 'D']
permu(0)
print('------------')

def combi(arr, i):
    if len(arr) == N:
        print(*arr)
        return

    if i < len(C):
        combi(arr + [C[i]], i+1)
        combi(arr, i+1)

N = 2
C = ['A', 'B', 'C', 'D', 'E']
combi([], 0)