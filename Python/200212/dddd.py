from tkinter import *
from tkinter import messagebox

# window 생성
window = Tk()

# window 이름 설정
window.title("My First Window")

# 이벤트 함수 : 핸들러 함수
def myFunc():
    messagebox.showinfo('이미지 출력', 'Happy Color')

photo = PhotoImage(file='happycolor.png')
label_photo = Label(window, image=photo)

btn_img = Button(window, image = photo, command = myFunc)

label_photo.pack()
#btn_img.pack()

# window 출력(위젯을 감싸고 있는 기본 틀)
window.mainloop()