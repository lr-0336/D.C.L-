import tkinter as tk
from Lock import exel_lock_up,exel_unlock,hlp


window = tk.Tk()

window.title('小汪')

window.geometry('475x350')#窗口大小

bkg = tk.PhotoImage(file='picture\\smile.gif')
bglable = tk.Label(window,image=bkg)
bglable.pack()


ebt = tk.Button(window,text='exel加密',width=15,height=2,command=exel_lock_up)

dbt = tk.Button(window,text='exel解密',width=15,height=2,command=exel_unlock)

hbt = tk.Button(window,text='注意事项',width=15,height=2,command=hlp)

ebt.place(x=10,y=15)#安放按钮

dbt.place(x=175,y=15)

hbt.place(x=345,y=15)

window.resizable(0,0)#锁定窗口大小

window.mainloop()


