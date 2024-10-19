# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:52:58 2024

@author: honan
"""
#Bài tập áp dụng: Chương 7 - slide 36
#Bài 1:
def tinhtong(*args, **kwargs):
    return sum(args)
#Cách 2:
    #tong = 0
    #for i in args:
        #tong += i
    #return tong
def tinh_tich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich
#if __name__=="__main__":
ds = [1,2,3,4,5]
print(tinhtong(*ds))
print(tinh_tich(*ds))

    