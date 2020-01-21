n = int(input())

for i in range(n):
    for j in range(2*n-1):
        A = (2*n-1)//2
        if A-i <= j <= A+i:
            print('*', end='')
        else:
            print(' ', end='')
            
    print()
