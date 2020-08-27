#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:13:32 2020

@author: fadewell
"""
import qrcode
#import pyqrcode
#import pandas as pd
#import numpy as np
#from pandas import D
import matplotlib.pyplot as plt
import cv2 as cv2
detector = cv2.QRCodeDetector()

#import pandas as pd
#import
ensemble = 0
white = 0
ijk = 0
while ensemble <1 :
    dimensions = 0
    white = '1'   ######## white <---->Green, Cream           1
    Yellow = '-2'   ####-2,-3,-4,----> Yellow==k @ k = 0
    Blue = '-2'      ##### -3,-4,-5 ---->Blue == j @ j = -1
    Somon = '0'    ##### 1,3,4,5 -----> Somon = k @ k = 0
    Pink = '2'      ###### 2,3,4 ----> Pink = ij @ ij = 0
    Green= '2'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
    black = '2' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
    Tree = '2'  #### i 
    Cream = '2'  ######## 3,4,5-------> is white too 2
    while dimensions < 1:
        qqrrr22 = qrcode.make(Cream)
        qqrrr22.save('r000partEnQtities000r.png')
        iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
        gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
        cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)
        
        
        yaw = 1
        while yaw > 0:
            
            i = 0
            qr2 = qrcode.make(Tree)
            qr2.save('partEntities00.png')
            img111 = cv2.imread("partEntities00.png")
            Treee = cv2.cvtColor(img111, cv2.COLOR_HSV2RGB)
            tree, bbox, straight_qrcode = detector.detectAndDecode(Treee)
            Tree = int(Tree)                              
            while i < Tree:
                j = 0
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_RGB2XYZ)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
                black = int(Black)
                while j < black :
                    qrr22 = qrcode.make(Green)
                    qrr22.save('000partEntities000.png')
                    iiim0mgg111 = cv2.imread("000partEntities000.png")
                    ggrreeeyy0 = cv2.cvtColor(iiim0mgg111,cv2.COLOR_BGR2HLS)
                    green, bbox, straight_qrcode = detector.detectAndDecode(iiim0mgg111)
                    
                    k = 0
                    Green = int(Green)
                    while k < Green:
                    
                    
                        plt.imshow(ggrreeeyy0)
                        plt.show()
                        Green-=1
                    Green = green
                    plt.imshow(ggrreeeeyy0)
                    plt.show()
                    j+=1
                print(i)
                plt.imshow(Treee)
                plt.show()
                i+=1
        
            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()
        
            yaw-=1
        dimensions +=1
    ensemble +=1