import tkinter as tk
from tkinter import *
import time
import threading
# import qd_client as client
import tkinter.messagebox
import tkinter.scrolledtext as tst


root1 = tk.Tk()
root1.title("进入聊天室")

# 创建几个frame作为容器
# root.resizable(False, False)  # 设置窗口大小不可变
fram_left_top = Frame(root1,width=380, height=276)
fram_left_center = Frame(root1,width=380, height=100)
fram_left_button1 = Frame(root1,width=380, height=40)
fram_right = Frame(root1,width=170, height=430, bg='white')
# 使用grid设置各个容器的位置
fram_left_top.grid(row=0, column=0, padx=2, pady=5)
fram_left_center.grid(row=1, column=0, padx=2, pady=5)
fram_left_button1.grid(row=2, column=0, padx=2, pady=5)
fram_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
fram_left_top.grid_propagate(0)
fram_left_center.grid_propagate(0)
fram_left_button1.grid_propagate(0)

def show():
    # 显示框
    text_msglist.config('我', foreground='red')
    text_msglist.config('user1', foreground='blue')
    # 开启一个线程用于接收消息并显示在聊天窗口
    t = threading.Thread(target=recvmessage)
    t.start()

# 发送信息
def sendmessage():
    str = text_msg.get('1.0','end-1c')
    if str != "" and str != None:
        # 在聊天室内容上方加一行发送人信息及发送时间
        msgto ="我：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        # 插入msgto信息
        text_msglist.config(state=NORMAL)
        text_msglist.insert(tk.END, msgto,'我')
        # 插入输入框text_msg中的信息
        text_msglist.insert(tk.END, str + '\n')
        # 将滚动条拉到最后显示最新消息
        text_msglist.see(tk.END)
        # 通过设置state属性设置textEdit不可编辑
        text_msglist.config(state=DISABLED)
        # 删除输入框text_msg中的信息
        text_msg.delete('0.0', tk.END)
    else:
        tk.messagebox.showinfo('警告', "不能发送空白信息！")
# 接收信息
def recvmessage(data):
    # data = client.recv_msg()
    while True:
        # 接受时间和接收的数据
        msgfrom = 'user1:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
        text_msglist.config(state='normal')
        # server作为标签,改变字体颜色
        text_msglist.insert(tk.END, msgfrom, 'user1')
        text_msglist.insert(tk.END,data)
        # 将滚动条拉到最后显示最新消息
        text_msglist.see(tk.END)
        text_msglist.config(state='disabled')

# 创建需要的元素
text_msglist = Text(fram_left_top, width=46)
text_msglist.config(state=DISABLED)
text_msg = Text(fram_left_center, width=46)
text_msg.focus_force()
button_sendmsg = Button(fram_left_button1, text='发送', command=sendmessage)
# 聊天窗口添加滚动条
text_msglist = tst.ScrolledText(fram_left_top, width=45, height=16)
# 输入窗口添加滚动条
text_msg = tst.ScrolledText(fram_left_center, width=45, height=5)
text_msg.focus_force()
# 把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)


root1.mainloop()
