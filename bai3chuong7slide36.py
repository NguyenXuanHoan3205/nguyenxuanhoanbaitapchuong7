# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:35:16 2024

@author: honan
"""
#Bài tập áp dụng: Chương 7 - slide 36
#Bài 3:
#Tương tự bài 56 trong lab
import math
def chuvi_dt(hinh, pheptinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0]
        return 4*canh if pheptinh == "chuvi" else canh**2
        #if pheptinh == "chuvi"
        #  return 4*canh
        # else:
        # return canh**2
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh == "chuvi" else dai*rong
    elif hinh == "tron":
        bk = args[0]
        return 2*math.pi*bk if pheptinh == "chuvi" else math.pi*bk**2
    else:
        return "hinh khong hop le"
#if __name__=="__main__":
print("Chu vi hình vuông: ", chuvi_dt('vuong','chuvi',3))
print("Diện tích hình vuông: ", chuvi_dt('vuong','dientich',3))
print("Chu vi hình chữ nhật: ", chuvi_dt('chunhat','chuvi',3,4))
print("Diện tích hình chữ nhật: ", chuvi_dt('chunhat','dientich',3,4))
print("Chu vi hình tròn: ", chuvi_dt('tron','chuvi',3))
print("Diện tích hình tròn: ", chuvi_dt('tron','dientich',3))
