# list 선언
nums = [25, 103, 36, 44, 75, 3, 81]

# 최솟값 반환 함수
min_val = min(nums)

# 최댓값 반환 함수
max_val = max(nums)

# list 요소들의 합 반환 함수
sum_val = sum(nums)

# list 요소들의 평균
avg_val = sum(nums) / len(nums)

print('-----list에 사용 가능한 함수-----')
print('list 요소 중 최솟값 :', min_val)
print('list 요소 중 최댓값 :', max_val)
print('list 요소들의 합 :', sum_val)
print('list 요소들의 평균 :', int(avg_val))
