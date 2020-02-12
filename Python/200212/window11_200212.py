from tkinter import *
from tkinter import messagebox
# tkinter? 파이썬에서 GUI 관련된 모듈 제공하는 lib
# C:\Users\bitcamp2\AppData\Local\Programs\Python\Python38-32\Lib\tkinter

# 이벤트 함수 : 핸들러 함수
def myFunc():
    messagebox.showinfo('London', 'This is London.')

def checkFunc():
    if chk.get() == 0:
        messagebox.showinfo('Checkbutton', '체크상태가 아닙니다.')
    else:
        messagebox.showinfo('Checkbutton', '체크되었습니다.')

def radioFunc():
    if val.get() == 1:
        label_c.configure(text='JAVA') # 라벨 속성 수정
    elif val.get() == 2:
        label_c.configure(text='Python')
    elif val.get() == 3:
        label_c.configure(text='C')
    else:
        messagebox.showinfo('', '정상적인 입력 데이터가 아닙니다.')
    

# window 생성
window = Tk()

# window 이름 설정
window.title("My First Window")

# window 크기 지정 ex) '(폭) 100 x (높이) 100'
window.geometry('700x400')
# window 크기 조정 여부 설정
# window.resizable(width=FALSE, height=FALSE)

# 텍스트 표현을 위한 Label
# text : 화면에 표현할 텍스트
# font : 폰트 종류, 사이즈
# fg   : 폰트색
# bg   : 배경색
# width, height: 텍스트 표현 영역
# anchor : 위치 ex) SE : South-East
label_a = Label(
    window,
    text = 'Window Programming with Python1',
    font = ('궁서체', 30),
    fg = 'white',
    bg = 'brown',
    width = 40,
    height = 2,
    anchor = CENTER
    )


label_b = Label(
    window,
    text = 'Window Programming with Python2',
    font = ('궁서체', 30),
    fg = 'white',
    bg = 'black',
    width = 40,
    height = 2,
    anchor = CENTER
    )


label_c = Label(
    window,
    text = 'Window Programming with Python3',
    font = ('궁서체', 30),
    fg = 'black',
    bg = 'orange',
    width = 40,
    height = 2,
    anchor = CENTER
    )

# 이미지 위젯 : 이미지 표현
# width, height : 이미지를 표현할 수 있는 영역(이미지의 사이즈가 아님)
# photo = PhotoImage(file='london.gif')
# label_photo = Label(window, image=photo)

# 버튼 위젯 : 버튼 표현
btn_close = Button(
    window,
    text = '프로그램 종료',
    fg = 'white',
    bg = 'gray',
    command = quit
    )

# 이미지 버튼 처리. 이벤트 헨들러 함수 이용
# btn_img = Button(
#     window,
#     image = photo,
#     command = myFunc()
# )

# 체크 박스
chk = IntVar()
check_btn_a = Checkbutton(
    window,
    text = '체크해주세요.',
    variable = chk,
    value = 1,
    command = checkFunc
)

# radio 버튼 : Radiobutton
val = IntVar()
radio_btn_a = Radiobutton(
    window,
    text = 'JAVA',
    variable = val,
    value = 0,
    command = radioFunc
)
radio_btn_b = Radiobutton(
    window,
    text = 'Python',
    variable = val,
    value = 2,
    command = radioFunc()
)
radio_btn_c = Radiobutton(
    window,
    text = 'C',
    variable = val,
    value = 3,
    command = radioFunc
)


# 실제 화면 출력 : 아래 순서에 따라 출력됨
label_c.pack()
# label_a.pack()
# label_b.pack()
# label_photo.pack()
check_btn_a.pack()
# btn_img.pack()
radio_btn_a.pack()
radio_btn_b.pack()
radio_btn_c.pack()
btn_close.pack()

# window 출력(위젯을 감싸고 있는 기본 틀)
window.mainloop()