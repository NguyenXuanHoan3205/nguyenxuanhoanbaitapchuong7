# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:05:14 2024

@author: honan
"""
#Bài tập cơ bản: Chương 7 - Slide 58
#Bài #1:
#Bài 1/a:
def canbac_n(x,n):
    return x**(1/n)
#Bài 1/b:
def binhphuong(n):
    if n>0:
        return n**2
    else:
        return "Số không hợp lệ, nhập lại"
#Bài 1/c:    
def sochan_am(n):
    return n<0 and n%2 == 0
#Bài 1/d:
def ktra_so(n):
    if n < 0 and n%2 != 0:
        return -1
    elif n > 0 and n%2 == 0:
        return 1 
    return 0 
#Bài 1/e:
def ktra_gtri():
    n = input("Nhập n: ")
    if n.replace(',','',1).replace('-','',1).isdigit():
        n = float(n)
    #if n,lstrip('-').isdigit():(-)123
    #n = int(n)
    #if n.strip('-').isdigit():(-)123(-)(- nếu chuỗi)
    #n = int(n)
    if -89 <= n <= 90:
        return n 
    print("Không hợp lệ, nhập lại")
    return ktra_gtri()
print(canbac_n(8,3))
print(binhphuong(3))
print(sochan_am(-4))
print(ktra_so(5))
print(ktra_gtri())

