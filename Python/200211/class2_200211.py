# Student 클래스 정의
class Student:
    count = 0

    # constructor 정의
    def __init__(self, name, kor, math, sc, art):
        self.Name = name
        self.Korean = kor
        self.Math = math
        self.Science = sc
        self.Art = art

        Student.count += 1
        print('인스턴스가 생성되었습니다.')
    
    # 각 과목의 점수의 합을 구해 반환하는 메서드
    def score_sum(self):
        return self.Korean + self.Math + self.Science + self.Art

    # 과목의 평균값을 구해 반환하는 메서드
    def score_avg(self):
        return self.score_sum()/4
    
    # __str__() 재정의
    def __str__(self):
        return '{}\t{}\t{}\t'.format(self.Name, self.score_sum(), self.score_avg())
    
    @classmethod
    def print(cls):
        print(Student.count)

Student.print()

# Student 클래스를 이용한 Object 생성
students =[
    Student('Jane', 92, 70, 79, 88),
    Student('Bob', 82, 77, 70, 51),
    Student('Mike', 44, 40, 100, 72),
    Student('Adam', 90, 81, 79, 60),
    Student('Eve', 85, 54, 69, 95),
    Student('Sharon', 66, 50, 70, 72),
    Student('John', 36, 73, 79, 80)
]

print('{}개의 리스트 요소가 생성되었습니다.'.format(Student.count))

# 학생들의 이름, 총점, 평균
print('이름', '총점', '평균', sep='\t')

# 학생 리스트 반복 출력
for st in students:
    # print(st.Name, st.score_sum(), st.score_avg(), sep='\t')
    # __str_()
    print(st)