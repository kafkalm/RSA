#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random
import math

#生成指定位数的随机奇数
def RandOdd(bit):
    return random.randrange(2**(bit-1)+1,2**bit,2)

#快速求模
def n_p_mod(n,p,N):
    if p == 0:
        return 1
    x = n_p_mod((n*n)%N,p>>1,N)   #递归调用 x^p % N = ((x*x)%p)^(p/2) % N
    if p&1 !=0: #n为奇数
        x = (x*n)%N
    return x

#单次Miller-Rabin素性检测 a in [2,n-1] n为待检测的数
def MillerRabinKnl(a,n):
    p = n-1
    p = bin(p).replace('0b','')
    p_2 = p[::-1]
    s = p_2.index('1')
    d = p[0:len(p)-s]
    d = int(d,2)
    # s = math.floor(math.log(p,2))
    # d = 1
    # while s>0:
    #     d = p // 2**s   #整除
    #     if p == d*2**s :
    #         break
    #     s = s - 1
    x = n_p_mod(a,d,n)  #求a^d mod n
    for r in range(0,s):    # r in [0,s-1]
        y = n_p_mod(a,d*2**r,n) #求 a^(2^r*d) mod n
        if x == 1 or y == n-1 :  # a^d mod n != 1 , a^(2^r*d) mod n != -1
            return True
    z = (a*a) % n
    if  z == 1 or z == n-1:     #二次探测定理 若p是奇素数 则 x in [1,p-1] x^2 mod p == 1  则 x=1 or x= p-1
        return False
    return False

#多次Miller-Rabin素性检测 n为待检测的数 k为检测次数
def MillerRabin(n,k):
    while k>0:
        if n == 1:
            return False
        if n == 2:
            return True
        a = random.randint(2,n-1)
        if not MillerRabinKnl(a,n):
            return False
        k = k -1
    return True

