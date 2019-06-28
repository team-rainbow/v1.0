import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import text_write

db = text_write.Database()
db.create_cursor()

#实例化object，建立窗口window
window = tk.Tk()

#给窗口的可视化起名字
window.title('Wellcome broccoli')

#设定窗口的大小(长 * 宽)
window.geometry('350x400')  # 这里的乘是小x

# 加载 wellcome image
canvas = tk.Canvas(window, width=350, height=500)
image_file = tk.PhotoImage(file='')

canvas.pack(side='top')
tk.Label(window, text='欢迎来到西兰花', font=('Arial', 14,), compound="center",
         image=image_file, ).place(x=110, y=20)

# 第5步，用户信息
tk.Label(window, text='用户名:', font=('Arial', 10)).place(x=30, y=185)
tk.Label(window, text='密码:', font=('Arial', 10)).place(x=30, y=240)
# 用户名输入框
var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(
    window, textvariable=var_usr_name,
    font=('Arial', 14), borderwidth=0)
entry_usr_name.place(x=100, y=185)
# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd,
                         font=('Arial', 14), show='*', borderwidth=0)
entry_usr_pwd.place(x=100, y=240)

# 用户登录功能
def usr_login():
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 判断用户输入用户名和密码是否正确
    if db.login(usr_name, usr_pwd):
        tkinter.messagebox.showinfo(title='Welcome', message='亲爱的' + usr_name + '欢迎您！')
    else:  # 如果发现用户名不存在
        tkinter.messagebox.showerror(title='Error', message='用户名或者密码错误!')


# 找回密码
def usr_forgot_pwd():
    window_forgot_pwd = tk.Toplevel()
    window_forgot_pwd.geometry('300x200')
    window_forgot_pwd.title('forgot password window')

    user_name = tk.StringVar()
    tk.Label(window_forgot_pwd, text='用户名: ').place(x=20, y=20)
    entry_new_name = tk.Entry(window_forgot_pwd, textvariable=user_name)
    entry_new_name.place(x=110, y=20)

    phone_number = tk.StringVar()
    tk.Label(window_forgot_pwd, text='手机号码: ').place(x=20, y=60)
    entry_new_name = tk.Entry(window_forgot_pwd, textvariable=phone_number)
    entry_new_name.place(x=110, y=60)

    def forgot_pwd():
        phone = phone_number.get()
        usr_name = user_name.get()
        # 如果用户名及密码正确，进入改密码窗口
        if db.forgot_passwd(usr_name, phone):
            usr_find_pwd()
        elif phone == '' or usr_name == '':
            tkinter.messagebox.showerror(title='错误', message='此号码或者用户名不能为空!')
        else:
            tkinter.messagebox.showerror(title='错误', message='此号码或者用户名未找到!')

    btn_comfirm_forgot_pwd = tk.Button(window_forgot_pwd, text='找回密码',
                                       command=forgot_pwd)
    btn_comfirm_forgot_pwd.place(x=130, y=100)

    # 修改密码
    def usr_find_pwd():
        usr_name = user_name.get()

        def change_pwd():
            pwd1 = user_pwd.get()
            pwd2 = user_pwd_confirm.get()
            if pwd1 == pwd2:
                db.change_passwd(usr_name, pwd1)

                tkinter.messagebox.showinfo(title='恭喜您', message='密码已经修改成功!')
                window_change_pwd.destroy()
            else:
                tkinter.messagebox.showerror(title='Error', message='两次密码输出不一致!')

        window_change_pwd = tk.Toplevel()
        window_change_pwd.geometry('300x200')
        window_change_pwd.title('change password window')

        user_pwd = tk.StringVar()
        tk.Label(window_change_pwd, text='新密码: ').place(x=20, y=20)
        entry_new_name = tk.Entry(window_change_pwd, textvariable=user_pwd)
        entry_new_name.place(x=110, y=20)

        user_pwd_confirm = tk.StringVar()
        tk.Label(window_change_pwd, text='再次输入密码: ').place(x=20, y=60)
        entry_new_name = tk.Entry(window_change_pwd, textvariable=user_pwd_confirm)
        entry_new_name.place(x=110, y=60)

        btn_comfirm_change_pwd = tk.Button(window_change_pwd, text='确定修改密码', command=change_pwd)
        btn_comfirm_change_pwd.place(x=130, y=100)


#用户注册功能
def usr_sign_up():
    def login_info():
        # 以下就是获取我们注册时所输入的信息
        usr_pwd = new_pwd.get()
        usr_pwdf = new_pwd_confirm.get()
        usr_name = new_name.get()
        usr_phone = new_phone_number.get()
        usr_email = new_email.get()

        if usr_pwd != usr_pwdf:
            tkinter.messagebox.showerror(title="错误", message='两次输入密码必须一致!')

        elif usr_name == '' or usr_pwd == '':
            tkinter.messagebox.showerror(title="错误！", message='用户名或者密码不能为空!')

        elif db.chachong(usr_name):
            tkinter.messagebox.showerror(title="错误！", message='此用户名已经被使用!')
        else:
            db.register(usr_name, usr_pwd, usr_phone, usr_email)
            tkinter.messagebox.showinfo(title="hello", message='您已经注册成功!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x250')
    window_sign_up.title('sign up window')

    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('')  # 将最初显示定为'example@python.com'
    tk.Label(window_sign_up, text='用户名: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=110, y=10)  # `entry`放置在坐标（150,10）.

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=110, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='再次输入密码: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=110, y=90)

    new_phone_number = tk.StringVar()
    tk.Label(window_sign_up, text='手机号码: ').place(x=10, y=130)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_phone_number, )
    entry_usr_pwd_confirm.place(x=110, y=130)

    new_email = tk.StringVar()
    tk.Label(window_sign_up, text='email: ').place(x=10, y=170)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_email, )
    entry_usr_pwd_confirm.place(x=110, y=170)

    # 下面的login_info
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=login_info)
    btn_comfirm_sign_up.place(x=120, y=210)
    btn_exit = tk.Button(window_sign_up, text='离开')
    btn_exit.place(x=200, y=210)


# 登录界面按钮
btn_login = tk.Button(window, text='登录', command=usr_login, )
btn_login.place(x=110, y=290)
btn_sign_up = tk.Button(window, text='注册', command=usr_sign_up, )
btn_sign_up.place(x=210, y=290)
btn_exit = tk.Button(window, text='退出', command=window.quit, borderwidth=0)
btn_exit.place(x=280, y=350)
btn_forgot_pwd = tk.Button(window, text='忘记密码?', command=usr_forgot_pwd, borderwidth=0)
btn_forgot_pwd.place(x=20, y=350)

window.mainloop()
