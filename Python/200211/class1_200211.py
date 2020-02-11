# 데이터 저쟝용 list 선언, 데이터 입력
# students =[
#     {'Name' : 'Jane', 'Korean' : 92, 'Math' : 70, 'Science' : 79, 'Art' : 88},
#     {'Name' : 'Bob', 'Korean' : 82, 'Math' : 77, 'Science' : 70, 'Art' : 51},
#     {'Name' : 'Mike', 'Korean' : 44, 'Math' : 40, 'Science' : 100, 'Art' : 72},
#     {'Name' : 'Adam', 'Korean' : 90, 'Math' : 81, 'Science' : 79, 'Art' : 60},
#     {'Name' : 'Eve', 'Korean' : 85, 'Math' : 54, 'Science' : 69, 'Art' : 95},
#     {'Name' : 'Tom', 'Korean' : 66, 'Math' : 50, 'Science' : 70, 'Art' : 72},
#     {'Name' : 'John', 'Korean' : 36, 'Math' : 73, 'Science' : 79, 'Art' : 80},
# ]

# 클래스를 이용한 인스턴스 생성
# st_a = Student()
# print(type(st_a))
# print(st_a)

# st_a.name = 'daughter'
# print(st_a.name)

# st_b = Student()
# print(type(st_b))
# print(st_b.name)

# Student 클래스 정의
class Student:
    # constructor 정의
    def __init__(self, name, kor, math, sc, art):
        self.Name = name
        self.Korean = kor
        self.Math = math
        self.Science = sc
        self.Art = art
    
    # 각 과목의 점수의 합을 구해 반환하는 메서드
    def score_sum(self):
        return self.Korean + self.Math + self.Science + self.Art

    # 과목의 평균값을 구해 반환하는 메서드
    def score_avg(self):
        return self.score_sum/4

# 1. list에 추가할 object를 만드는 함수
# def makeStudent(name, kor, math, sc, art):
#     return {
#         'Name' : name,
#         'Korean' : kor,
#         'Math' : math,
#         'Science' : sc,
#         'Art' : art
#         }

# def makeStudent_class(name, kor, math, sc, art):
#     st_temp = Student()
#     st_temp.name = name
#     st_temp.Korean = kor
#     st_temp.Math = math
#     st_temp.Science = sc
#     st_temp.Art = art

#     return st_temp

# students =[
#     makeStudent_class('Jane', 92, 70, 79, 88),
#     makeStudent_class('Bob', 82, 77, 70, 51),
#     makeStudent_class('Mike', 44, 40, 100, 72),
#     makeStudent_class('Adam', 90, 81, 79, 60),
#     makeStudent_class('Eve', 85, 54, 69, 95),
#     makeStudent_class('Sharon', 66, 50, 70, 72),
#     makeStudent_class('John', 36, 73, 79, 80)
# ]

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

# 학생들의 이름, 총점, 평균
print('이름', '총점', '평균', sep='\t')

# 학생 리스트 반복 출력
for st in students:
    # dic 참조
    # score_sum = st['Korean'] + st['Math'] + st['Science'] + st['Art']
    
    # 클래스 인스턴스 속성 참조
    # score_sum = st.Korean + st.Math + st.Science + st.Art
    # score_avg = score_sum / 4
    # print(st['Name'], score_sum, score_svg, sep='\t')
    # 클래스 인스턴스 속성 참조
    # print(st.Name, score_sum, score_avg, sep='\t')
    print(st.Name, st.score_sum(), st.score_avg())