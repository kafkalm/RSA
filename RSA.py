#!/usr/bin/env python
#-*- coding:utf-8 -*-
from M_R import *
import random
import base64
from tkinter import messagebox
import sys
sys.setrecursionlimit(10000)    #设置递归深度

#计算两数最大公约数  欧几里德除法
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

#求模逆  扩展欧几里得除法
def ModInverse(e,N,l):
    if N == 0:
        l[0] = 1
        l[1] = 0
        return 1
    r = ModInverse(N,e%N,l)
    temp = l[1]
    l[1] = l[0] - (e//N)*l[1]
    l[0] = temp
    return 1

#生成大素数p,q,N 公钥、密钥
def RSA(bit):
    while True:
        p = RandOdd(bit)
        if MillerRabin(p,20):
            break
    while True:
        q = RandOdd(bit)
        if MillerRabin(q,20):
            break
    N = p*q
    f_N = (p-1)*(q-1)   #N的欧拉函数值
    while True:
        e = random.randrange(2,f_N)
        if gcd(f_N,e) == 1:
            break
    l = [0,0]
    ModInverse(f_N,e,l)
    d = l[1]
    if d<0:
        d = d%f_N
    return p,q,N,e,d

# 将字符转换成八位的二进制 接收 l：字符串 返回值为字符串
def Str2bit(l):
    l=list(l)
    bit_list=[]
    for i in l:
        if 0<len(bin(ord(i)))<=10:
            bit_0b=bin(ord(i)).replace('0b','')
            bit_8=(8-len(bit_0b))*'0'+bit_0b
            bit_list.append(bit_8)
        else:
            messagebox.showerror('错误','输入有误')
            raise SystemError("输入有误")
    bit_list=''.join(bit_list)
    return bit_list

#分组/编码函数 将输入的明文密文分成指定的bit一组
def Divide(plaintext,bit):
    stri = Str2bit(plaintext)
    Plaintext_bit = []
    i = 1
    while i <= len(stri) // bit:
        Plaintext_bit.append(stri[bit * (i - 1):bit * i])
        i = i + 1
    if(len(stri) % bit != 0):
        Plaintext_bit.append(stri[bit*(i-1):])
    return Plaintext_bit


#加密函数
def Encrypt(plaintext,e,N,bit):
    '''

    :param plaintext: str
    :param e: int
    :param N: int
    :param bit: int
    :return: ciphertext: str
    '''
    plaintext_b64 = str(base64.b64encode(plaintext.encode('utf-8')),'utf-8')
    plaintext_list = Divide(plaintext_b64,bit)
    ciphertext_bits = ''
    for i in plaintext_list:
        plaintext_num = int(i,2)
        ciphertext_num = n_p_mod(plaintext_num,e,N) # N 2*bit位 所以 ciphertext_num不超过2*bit位 以2*bit位分组
        ciphertext_bit = bin(ciphertext_num).replace('0b','')
        ciphertext_bits = ciphertext_bits+((2*bit-len(ciphertext_bit))*'0'+ciphertext_bit)
    ciphertext_str = ''
    for i in range(0,len(ciphertext_bits)//8):
        ciphertext_str = ciphertext_str + chr(int(ciphertext_bits[i*8:i*8+8],2))
    ciphertext = str(base64.b64encode(ciphertext_str.encode('utf-8')),'utf-8')
    return ciphertext

#解密函数
def Decrypt(ciphertext,d,N,bit):
    ciphertext_b64 = str(base64.b64decode(ciphertext.encode('utf-8')),'utf-8')
    ciphertext_list = Divide(ciphertext_b64,2*bit)
    plaintext_bits = ''
    for i in ciphertext_list:
        ciphertext_num = int(i,2)
        plaintext_num = n_p_mod(ciphertext_num,d,N)
        plaintext_bit = bin(plaintext_num).replace('0b','')
        plaintext_bits = plaintext_bits + ((2*bit-len(plaintext_bit))*'0'+plaintext_bit)
    plaintext_str = ''
    for i in range(0,len(plaintext_bits)//8):
        plaintext_str = plaintext_str + chr(int(plaintext_bits[i*8:i*8+8],2))
    plaintext = str(base64.b64decode(plaintext_str.encode('utf-8')),'utf-8')
    return plaintext
