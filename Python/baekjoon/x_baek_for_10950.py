T = int(input())
# print(T)

for i in range(T):
    X = input().split()
    A, B = X
    group = tuple()
    group[i] = A+B
    
for i in range(T):
    print(group[i])
    
