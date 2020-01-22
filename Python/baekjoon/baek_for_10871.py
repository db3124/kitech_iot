N, X= map(int, input().split())

A = map(int, input().split())
A = list(A)

for i in range(N):
    if A[i]<X:
        print(A[i], '', end='')
