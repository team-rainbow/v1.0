"""
    頭像:    PID:
    暱稱:    性別:
    生日:    城市:
    相冊:
    交友宣言:

    函數封裝修改功能,條件判斷修改顯示內容
"""

from tkinter import *
import tkinter.messagebox
import pickle
import text_write
db = text_write.Database()
db.create_cursor()

# 創建空白界面
window = Tk()

# 设定窗口的大小(长 x 宽),这里的乘是小x
window.geometry('350x440')

# 標題
window.title("個人資料")

# 頭像
list01=['昵称','性别','年龄','生日','星座','城市','相册','交友宣言']

def fun(index):
    a=open('xinxi.txt','r')
    c=a.readlines()
    d=c[0].split()
    text=list01[index]+':'+d[index]
    var_name=StringVar()
    var_name.set(text)
    return var_name
a='xinxi.txt'
def submit():
    global a
    db.write(a)


tkinter.Label(window,text="ID:",font=('Arial', 10)).place(x=220, y=20)


tkinter.Label(window,textvariable=fun(0),font=('Arial', 10)).place(x=46, y=20)

tkinter.Label(window,textvariable=fun(1),font=('Arial', 10)).place(x=46, y=60)

tkinter.Label(window,textvariable=fun(2),font=('Arial', 10)).place(x=46, y=100)

tkinter.Label(window,textvariable=fun(3),font=('Arial', 10)).place(x=46, y=140)

tkinter.Label(window,textvariable=fun(4),font=('Arial', 10)).place(x=46,y=180)

# tkinter.Label(window,textvariable=fun(5),font=('Arial', 10)).place(x=46,y=220)
#
# tkinter.Label(window,textvariable=fun(6),font=('Arial', 10)).place(x=46, y=260)
#
# tkinter.Label(window,textvariable=fun(7),font=('Arial', 10)).place(x=20, y=320)

# canvas = Canvas(window, height=300, width=500)
# imagefile = PhotoImage(file='stone.gif')
# image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
# canvas.pack(side='top')

def alter_():
    window_alter = Tk()
    window_alter.geometry('350x440')

    tkinter.Label(window_alter, text="昵称:").place(x=20, y=20)

    tkinter.Label(window_alter, text='性別:').place(x=20, y=60)

    tkinter.Label(window_alter, text="年齡:").place(x=20, y=100)

    tkinter.Label(window_alter, text="星座:").place(x=20, y=140)

    tkinter.Label(window_alter, text="城市:").place(x=20, y=180)

    tkinter.Label(window_alter, text="相册:").place(x=20, y=220)

    tkinter.Label(window_alter, text="交友宣言:").place(x=20, y=260)

    var_usr_name = tkinter.StringVar()
    var_usr_name.set('')
    entry_usr_name = tkinter.Entry(window_alter, textvariable=var_usr_name, font=('Arial', 10), borderwidth=0)
    entry_usr_name.place(x=50, y=20)


    # 创建一个IntVar类型的变量
    # 让如下Radiobutton关联在同一个变量
    var = IntVar(window_alter)
    Radiobutton(window_alter, text="男", value=1, variable=var).place(x=60,y=60)
    # text:设置此控件代表的值
    # value:设置此控件关联的变量

    rbtn2 = Radiobutton(window_alter, text="女", value=0, variable=var)
    rbtn2.pack()

    rbtn3 = Radiobutton(window_alter, text="保密", value=2, variable=var)
    rbtn3.pack()

    mb = Menubutton(window_alter, text='请选择', relief=RAISED)  # relief设计按钮的样式
    mb.pack()

    city = Menu(mb, tearoff=False)
    city.add_command(label='北京')
    city.add_command(label='上海')
    city.add_command(label='广州')
    mb.config(menu=city)

    Button(window_alter, text="相冊").place(x=20, y=300)

    Button(window_alter,text="保存",command=submit).place(x=20,y=380)
    Button(window_alter,text="退出").place(x=280,y=380)

    window_alter.mainloop()

Button(window, text ='修改資料', command = alter_).place(x=20, y=380)

window.mainloop()
