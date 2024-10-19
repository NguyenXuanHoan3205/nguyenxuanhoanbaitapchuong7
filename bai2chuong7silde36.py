# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:15:10 2024

@author: honan
"""
#Bài tập áp dụng: Chương 7 - slide 36
#Bài 2:
import math
def chuvi(hinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0]
        return 4*canh 
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) 
    elif hinh == "tron":
        bk = args[0]
        return 2*math.pi*bk 
    else:
        return "hinh khong hop le"
#if __name__=="__main__":
print("Chu vi hình vuông: ", chuvi('vuong',3))
print("Chu vi hình chữ nhật: ", chuvi('chunhat',3,4))
print("Chu vi hình tròn: ", chuvi('tron',3))

