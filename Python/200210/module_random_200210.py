import random as r

# random() : 0 <= N < 1.0 float 데이터 반환
print('random() :', r.random(), int(r.random()))

# randint() : a <= N < b 정수
print('randint() :', r.randint(1, 100))

# uniform(): a <= N < b 실수
print('uniform(): ', r.uniform(2.5, 30.1))

# randrange() : 정수
print('randrange(): ', r.randrange(1, 10))

# choice() : 시퀀스 객체에서 랜덤으로 고름
fruit = ['apple', 'banana', 'orange', 'cherry', 'melon']
print('choice() :', r.choice(fruit))

# shuffle() : 시퀀스 객체 섞기
print(fruit)
r.shuffle(fruit)
print(fruit)

# sample() : list 중에 개수만큼 요소 축출하여 반환
num_list = list(range(1, 46))
print(r.sample(num_list, k=7))