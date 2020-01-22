T = int(input())

for i in range(T):
    X = map(int, input().split())
    group = list(X)    
    print('Case #', i+1, ': ', group[0]+group[1], sep='')
