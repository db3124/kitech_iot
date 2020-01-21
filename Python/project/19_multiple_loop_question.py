n = int(input())

for i in range(n):
    for j in range(2n-1):
        if (2n-1)//2=j or (j-i) <= (2n-1)//2 <= (j+i):
            print('*', end='')
        else:
            print(' ', end='')



    print() 
