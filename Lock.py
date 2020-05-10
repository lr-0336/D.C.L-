from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory
import windnd
import eexel as ee
from ups import test
import dexel as de

def exel_lock_up():

    if test()==1:
        tips()


    def route():

        tk.withdraw()
        value=entry.get()
        num = ee.exelo(value)
        if num == 0:
            esuccess()
        else:
            df2()
        
        
                
    def dragged_files(files):
        msg = '\n'.join((item.decode('gbk') for item in files))
        # 弹窗
        # showinfo('您拖放的文件', msg)
        path.set(msg)

    tk = Toplevel()
    tk.geometry('220x60')
    tk.title('加密')
    tk.resizable(0,0)#锁定窗口大小

    # 正常选择按钮打开文件
    path = StringVar()
    Label(tk, text="目标路径:").grid(row=0, column=0)
    entry = Entry(tk, textvariable=path)
    entry.delete(0,END)
    entry.insert(0,'拖拽文件到此窗口点确定')
    entry.grid(row=0, column=1)

    #按钮
    Button(tk,text='确定',width=10,command=route).place(x=5,y=25)
    Button(tk,text='取消',width=10,command=tk.withdraw).place(x=135,y=25)




    # 拖拽文件
    windnd.hook_dropfiles(tk, func=dragged_files)
    tk.mainloop()
    return 0

def exel_unlock():

    def route():
        tk.withdraw()
        value=entry.get()
        num = de.unexel(value)
        if num == 0:
            dsuccess()
        else:
            df2()
                
    def dragged_files(files):
        msg = '\n'.join((item.decode('gbk') for item in files))
        # 弹窗
        # showinfo('您拖放的文件', msg)
        path.set(msg)

    tk = Toplevel()
    tk.geometry('220x60')
    tk.title('解密')
    tk.resizable(0,0)#锁定窗口大小

    # 正常选择按钮打开文件
    path = StringVar()
    Label(tk, text="目标路径:").grid(row=0, column=0)
    entry = Entry(tk, textvariable=path)
    entry.delete(0,END)
    entry.insert(0,'拖拽文件到此窗口点确定')
    entry.grid(row=0, column=1)

    #按钮
    Button(tk,text='确定',width=10,command=route).place(x=5,y=25)
    Button(tk,text='取消',width=10,command=tk.withdraw).place(x=135,y=25)




    # 拖拽文件
    windnd.hook_dropfiles(tk, func=dragged_files)
    tk.mainloop()
    return 0

def hlp():

    tk = Toplevel()
    tk.title('注意事项')
    tk.geometry('605x605')#窗口大小
    tk.resizable(0,0)#锁定窗口大小
    global bkg1 
    bkg1 = PhotoImage(file='picture\\notes.gif')
    bglable = Label(tk,image=bkg1)
    bglable.pack()
    return 0

def tips():

    tk = Toplevel()
    tk.title('提示')
    tk.geometry('500x145')#窗口大小
    tk.resizable(0,0)#锁定窗口大小
    global bkg2 
    bkg2 = PhotoImage(file='picture\\tips.gif')
    bglable = Label(tk,image=bkg2)
    bglable.pack()


def esuccess():
    
    num = 1
    tk = Toplevel()
    tk.title('成功')
    tk.geometry('630x200')#窗口大小
    tk.resizable(0,0)#锁定窗口大小
    global bkg3 
    bkg3 = PhotoImage(file='picture\\esu.gif')
    bglable = Label(tk,image=bkg3)
    bglable.pack()
    Button(tk,text='确定',width=20,command=tk.withdraw).place(x=190,y=150)

def dsuccess():

    tk = Toplevel()
    tk.title('成功')
    tk.geometry('630x200')#窗口大小
    tk.resizable(0,0)#锁定窗口大小
    global bkg4 
    bkg4 = PhotoImage(file='picture\\dsu.gif')
    bglable = Label(tk,image=bkg4)
    bglable.pack()
    Button(tk,text='确定',width=20,command=tk.withdraw).place(x=190,y=150)


def df2():

    tk = Toplevel()
    tk.title('出错啦')
    tk.geometry('630x200')#窗口大小
    tk.resizable(0,0)#锁定窗口大小
    global bkg7 
    bkg7 = PhotoImage(file='picture\\df2.gif')
    bglable = Label(tk,image=bkg7)
    bglable.pack()
    Button(tk,text='额~~',width=20,command=tk.withdraw).place(x=190,y=150)

