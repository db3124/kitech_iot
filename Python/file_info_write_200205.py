import random

hangeul = list('가나다라마바사아자차카타파하')

with open('info.txt', 'w', encoding='utf-8') as file:
    for i in range(1000):
        name = random.choice(hangeul)+random.choice(hangeul)
        weight = random.randrange(40, 200)
        height = random.randrange(140, 230)

        file.write('{}, {}, {}\n'.format(name, weight, height))

print('파일이 생성되었습니다.')