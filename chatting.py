
from tkinter import *
import time
import text_write
db = text_write.Database()
db.create_cursor()


root = Tk()
root.title("进入聊天室")

#创建几个frame作为容器
fram_left_top = Frame(width=380,height=270,bg='white')
fram_left_center = Frame(width=380,height=100,bg='white')
fram_left_button1 = Frame(width=380,height=40)
fram_right = Frame(width=170,height=430,bg='white')


#发送按钮事件
def sendmessage():
    #在聊天室内容上方加一行发送人信息及发送时间
    msgto = "我：" +time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
    b=str(msgto).split(":",1)
    c = text_msg.get('0.0', END)
    #插入msgto信息
    text_msglist.insert(END,msgto)
    #插入输入框text_msg中的信息
    text_msglist.insert(END, c)
    # 删除输入框text_msg中的信息
    text_msg.delete('0.0', END)
    b.append(c)



#创建需要的元素
text_msglist = Text(fram_left_top)
text_msg = Text(fram_left_center)
friend_info= Label(fram_right)
button_sendmsg = Button(fram_left_button1,text='发送',command=sendmessage)


#使用grid设置各个容器的位置
fram_left_top.grid(row=0,column=0,padx=2,pady=5)
fram_left_center.grid(row=1,column=0,padx=2,pady=5)
fram_left_button1.grid(row=2,column=0,padx=2,pady=5)
fram_right.grid(row=0,column=1,rowspan=3,padx=4,pady=5)

fram_left_top.grid_propagate(0)
fram_left_center.grid_propagate(0)
fram_left_button1.grid_propagate(0)

#把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)

root.mainloop()