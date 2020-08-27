#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:18:14 2020

@author: fadewell
"""



#import math
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
    
    while dimensions < 1:
        Yellow = '-2'   ####-2,-3,-4,----> Yellow==k @ k = 0
        Blue = '-2'      ##### -3,-4,-5 ---->Blue == j @ j = -1
        Somon = '2'    ##### 1,3,4,5 -----> Somon = k @ k = 0
        Pink = '1'      ###### 2,3,4 ----> Pink = ij @ ij = 0
        Green= '0'      ##### 1,-1,-2,-3 ----> Green = j @ j = 2
        black = '-1' ##### -2,-3,-4 -----> black == i == ij@ ij = 0
        Cream = '2'
        yaw = 1
        while yaw > 0:
            
            i = 0
            qqrrr22 = qrcode.make(Cream)
            qqrrr22.save('r000partEnQtities000r.png')
            iiim0g0mgg111 = cv2.imread("r000partEnQtities000r.png")
            gggrreeeeyy0 = cv2.cvtColor(iiim0g0mgg111, cv2.COLOR_XYZ2RGB)
            cream, bbox, straight_qrcode = detector.detectAndDecode(iiim0g0mgg111)
            Cream = int(Cream)
            while i < Cream:

                j = 2
                
                qqrrr22 = qrcode.make(black)
                qqrrr22.save('r000partEntities000r.png')
                iiim00mgg111 = cv2.imread("r000partEntities000r.png")
                ggrreeeeyy0 = cv2.cvtColor(iiim00mgg111, cv2.COLOR_HSV2RGB)
                Black, bbox, straight_qrcode = detector.detectAndDecode(iiim00mgg111)
               
                ij = 0
                while i < j :
                    
           
                    qqrr22 = qrcode.make(Green)
                    qqrr22.save('000partEntities000.png')
                    iiim0mgg111 = cv2.imread("000partEntities000.png")
                    ggrreeeyy0 = cv2.cvtColor(iiim0mgg111, cv2.COLOR_RGB2XYZ)
                    green, bbox, straight_qrcode = detector.detectAndDecode(iiim0mgg111)
                    j = 2
                    ijk = ij
                    
                    Green = int(Green)
                    while j > Green :## i<j
                        ij = 0
                        #i = ij
                        qr22 = qrcode.make(Pink)
                        qr22.save('00partEntities00.png')
                        iiimmgg111 = cv2.imread("00partEntities00.png")
                        ggrreeeyy = cv2.cvtColor(iiimmgg111, cv2.COLOR_BGR2HLS)
                        pink, bbox, straight_qrcode = detector.detectAndDecode(iiimmgg111)
                        
                        jk = 2
                        i=0
                        while ij < jk:
                            
                            iji = i
                            k = 0
                             
                            qr22 = qrcode.make(Somon)
                            qr22.save('0partEntities0.png')
                            iiimg111 = cv2.imread("0partEntities0.png")
                            ggreeyy = cv2.cvtColor(iiimg111, cv2.COLOR_BGR2Luv)
                            somon, bbox, straight_qrcode = detector.detectAndDecode(iiimg111)
                            
                            Somon = int(Somon)
                            while  k  < Somon :###### X KiJ X
                                
                                
                                 ### -2
                                qqr2 = qrcode.make(Blue)
                                qqr2.save('0partEntities.png')
                                iimg11 = cv2.imread("0partEntities.png")
                                ggreyy = cv2.cvtColor(iimg11, cv2.COLOR_BGR2LAB)
                                blue, bbox, straight_qrcode = detector.detectAndDecode(iimg11)
                         
                                j = -1
                                while j < k:
                                    
                                    i =  3
                                    k=-1
                                    qr1 = qrcode.make(Yellow)
                                    qr1.save('partEntities.png')
                                    img11 = cv2.imread("partEntities.png")
                                    greyy = cv2.cvtColor(img11, cv2.COLOR_BGR2HSV)
                                    yellow, bbox, straight_qrcode = detector.detectAndDecode(img11)
                                    
                                    
                                    while k <  i:
                                    
                                        qr = qrcode.make(white)
                                        qr.save('partEntities0.png')
                                        img1 = cv2.imread("partEntities0.png")
                                        greyyy = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                                        white, bbox, straight_qrcode = detector.detectAndDecode(img1)
                                        ik = k
                                        Nn=1    
                                        white = 1 ### white == jk , -6
                                        jk = 2
                                        KiJ = 0
                                        JiK = 0
                                        while ik < ij:
                                   

                                            qr2 = qrcode.make(KiJ)
                                            qr2.save('partEntities00.png')
                                            img111 = cv2.imread("partEntities00.png")
                                            greyyyy = cv2.cvtColor(img111, cv2.COLOR_BGR2RGB)
                                            data, bbox, straight_qrcode = detector.detectAndDecode(img111)
                                           
                                           
                                            
                                            if jk == white:
                                                ik = i
                                                
                                        
                                            if  ik == k:
                                                white += 1
                                                KiJ +=1
                                                if jk == white:
                                                    white -= KiJ
                                                    KiJ = 0
                                                    jk -= 1
                                        #    plt.imshow(greyyyy)
                                        #    plt.show()
                                         #   
                                       # ik  = i
                                  
                             
                                       # plt.imshow(greyyy)
                                       # plt.show()
                                        Yellow = int(Yellow)
                                        if  k == Yellow:
                                          #  print(Yellow)
                                            ik = 4
                                            k = ik
                                        
                                        if ik == i :
                                            Yellow = int(Yellow)
                                            Yellow += 1
                                      
                              
                                            if k == Yellow:
                                                k-=1
                                                Yellow = yellow
                                    
                                        jk = k
                                        
                            
                                   # plt.imshow(greyy)
                                 #   plt.show()
                                    Blue = int(Blue)
                                    if j == Blue:  #### blue -2
                                        print(Blue,'Blue Exit')
                                        jk = 2
                                        j = jk
                                   #     i = JiK
                                #    ijk += 1
                                    if jk == k:
                                        Blue = int(Blue)
                                        Blue += 1
                                        print(Blue,'Blue')
                                        if j == Blue:
                                            Blue = blue
                                            j -= 1
                                    k = 0
                 
                           #     plt.imshow(ggreyy)
                           #     plt.show()
                                Somon -=1
                               
                               # if Somon == JiK:
                            #        k+=1
                               #     Somon = somon
                            Somon = somon
                           #     k += 1    ################################# K I J
                       
                            
                            
                           # i = ij
                            i = iji
                            Pink = int(Pink)
                            if i == Pink:
                                jk = -6
                            print(i,ij)
                            if jk == j: 
                                Pink = int(Pink)
                                Pink -= 1
                              
                                if i == Pink:
                               #     print(ijk,'Pink ')
                                    Pink = pink
                                    i+= 1
                                  #  iji = i
                                   
                           
                         #   plt.imshow(ggreeyy)
                        #    plt.show()
                            
            
                      #  j = 2
                      #  plt.imshow(ggrreeeyy)
                      #  plt.show()   
                        Green += 1
                        #j -= 1 ###################  I J
                        ij = ijk
                        i = int(black)
                    j = ij
                    Green = green
                    #Green = int(Green)
                    plt.imshow(ggrreeeyy0)
                    plt.show() 
                    if ij == i:####black
                        ij = 101
                        i = ij
              
                    
                    if j == ij:
                       # i = -2
                        black = int(black)
                        black += 1
                        if ij == black:
                            #print(ijk,'black')
                            black = Black
                            ij-= 1
                    
                
                i = JiK
          
                
                plt.imshow(ggrreeeeyy0)
                plt.show()   
                Cream -= 1
               # i += 1        ### I  
            Cream = cream
  

            print('QR Cream QR')
            
            plt.imshow(gggrreeeeyy0)
            plt.show()   
            yaw -= 1

        dimensions += 1

    ensemble += 1