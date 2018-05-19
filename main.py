#!/usr/bin/env python
#-*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox
from RSA import *

'''
    16271120
    马天波
    RSA密码实验
'''

def mtb_jiami():
    if P.get()=='' or Q.get()=='' or N.get()=='':
        tkinter.messagebox.showerror('错误','没有生成密钥')
        raise SystemError('没有生成密钥')
    elif Bit.get()=='':
        tkinter.messagebox.showerror('错误','请输入N的比特数')
        raise SystemError('没有输入N的比特数')
    mw2.delete('1.0', 'end')
    mingwen = mw1.get('1.0', 'end')
    if len(mingwen) <= 1:
        tkinter.messagebox.showerror('错误', '没有输入明文')
        raise SystemError('没有输入明文')
    num_e = int(e.get())
    num_N = int(n.get())
    num_bit = int(Bit.get())
    miwen = Encrypt(mingwen,num_e,num_N,num_bit)
    mw2.insert('1.0',miwen)

#解密函数
def mtb_jiemi():
    if P.get()=='' or Q.get()=='' or N.get()=='':
        tkinter.messagebox.showerror('错误','没有生成密钥')
        raise SystemError('没有生成密钥')
    elif Bit.get()=='':
        tkinter.messagebox.showerror('错误','请输入N的比特数')
        raise SystemError('没有输入N的比特数')
    mw1.delete('1.0', 'end')
    miwen = mw2.get('1.0','end')
    if len(miwen) <= 1:
        tkinter.messagebox.showerror('错误', '没有输入密文')
        raise SystemError('没有输入密文')
    num_d = int(d.get())
    num_N = int(n.get())
    num_bit = int(Bit.get())
    mingwen = Decrypt(miwen,num_d,num_N,num_bit)
    mw1.insert('1.0',mingwen)

#清空函数
def qingkong():
    mw1.delete('1.0', 'end')
    mw2.delete('1.0', 'end')
    Bit.delete('0','end')
    p.set('')
    q.set('')
    n.set('')
    e.set('')
    d.set('')

#随机生成密钥
def rand():
    if Bit.get() == '':
        tkinter.messagebox.showerror('错误','没有输入比特数')
        raise SystemError('没有输入比特数')
    num_bit = int(Bit.get())
    if num_bit != 128 and num_bit != 256 and num_bit !=512 and num_bit != 1024:
        tkinter.messagebox.showerror('错误','比特数应为128/256/512/1024')
        raise SystemError('比特数输入错误')
    a = RSA(num_bit)
    p.set(a[0])
    q.set(a[1])
    n.set(a[2])
    e.set(a[3])
    d.set(a[4])


root=Tk()
root.title("RSA")
root.geometry("750x400")
root.resizable(width=False, height=FALSE)
Label(root,text='RSA加密解密程序',width=15,height=2).place(x=300,y=0)
Label(root,text="明文",width=5,height=2).place(x=10,y=25)
Label(root,text="密文",width=5,height=2).place(x=10,y=200)
Label(root,text="P",width=1,height=1).place(x=310,y=50)
Label(root,text="Q",width=1,height=1).place(x=520,y=50)
Label(root,text='N',width=1,height=1).place(x=310,y=90)
Label(root,text='N的比特数',width=10,height=1).place(x=303,y=125)
Label(root,text='128/256/512/1024bit',width=26,height=1).place(x=530,y=125)
Label(root,text='公钥',width=3,height=1).place(x=310,y=160)
Label(root,text='私钥',width=3,height=1).place(x=310,y=200)
p = StringVar()
q = StringVar()
n = StringVar()
e = StringVar()
d = StringVar()
P = Entry(root,textvariable = p,state='readonly',width=25)
P.place(x=330,y=50)
Q = Entry(root,textvariable = q,state='readonly',width=25)
Q.place(x=540,y=50)
N = Entry(root,textvariable = n,state='readonly',width=55)
N.place(x=330,y=90)
E = Entry(root,textvariable = e,state='readonly',width=52)
E.place(x=350,y=160)
D = Entry(root,textvariable = d,state='readonly',width=52)
D.place(x=350,y=200)
Bit = Entry(root,width = 22)
Bit.place(x=380,y=125)
mw1 = Text(root,width=40,height=10)
mw1.place(x=15,y=60)
mw2 = Text(root,width=40,height=10)
mw2.place(x=15,y=235)
Button(root,text="加密",width=20,height =2,command=mtb_jiami).place(x=360,y=320)
Button(root,text="解密",width=20,height =2,command=mtb_jiemi).place(x=550,y=320)
Button(root,text="清空",width=20,height = 2,command=qingkong).place(x=550,y=250)
Button(root,text='随机生成密钥',width=20,height=2,command=rand).place(x=360,y=250)
root.mainloop()