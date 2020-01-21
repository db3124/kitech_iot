count = int(input())

i = 0
while True:
    print(i)
    i += 1
    if i == count:
        break

print('--------------')

count = int(input('반복 횟수 : '))
for i in range(count+1):
    if i % 2 == 0:
        continue
    print(i)
