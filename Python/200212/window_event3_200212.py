from tkinter import *
from tkinter import messagebox
# event handler
def key_event(event):
    print(event)

    messagebox.showinfo('키보드 이벤트', '(' + str(event.x) + ', ' + str(event.y) + ')')

# 위젯
window=Tk()
window.geometry('300x300')

window.bind('<Key>', key_event)

window.mainloop()