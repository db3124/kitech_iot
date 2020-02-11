# 부모 클래스
class Parent:
    def __init__(self):
        self.value  = 'test'
        print('부모 클래스의 생성자가 호출되었습니다.')
   
    def test(self):
        print('부모 클래스의 test() 메서드 호출')

# 자식 클래스
class Child(Parent):
    # 생성자
    def __init__(self):
        Parent.__init__(self)
        print('자식 클래스의 생성자가 호출되었습니다.')
    
    def test(self):
        print('자식 클래스의 test() 메서드 호출')
    
    def __str__(self):
        return self.value
   
    def test1(self):
        print('자식 클래스의 test1() 메서드 호출')

child = Child()
child.test()
print(child.value)

print(isinstance(child, Parent))
print(isinstance(child, Child))

print(child)

child.test1()
