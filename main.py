#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:15:45 2020

@author: brianmatejevich
"""

import cv2
import time as t
import numpy as np
import math



font = cv2.FONT_HERSHEY_SIMPLEX 


start = t.time()
stop = start + 10000
lap_length = 50+1
push_ups = 0
pull_ups = 0
squats = 0

pull_count = 0
push_count = 0
squat_count = 0

total_time = 0
laps = 0

TIME_TO_DO_PULL_UPS = 15
TIME_TO_DO_PUSH_UPS = 15
TIME_TO_DO_SQUATS = 20

while t.time()<stop:
    screen = 64*np.ones((830,1300,3), np.uint8)
    #print(t.time()-start)
    dt = round(t.time()-start,5)
    minutes = math.floor(dt/60)
    seconds = round(dt%60)
    tenths = round(round(dt%1,3)*100)
    message = "{0:0=2d}".format(minutes)+":"+"{0:0=2d}".format(seconds)+":"+"{0:0=2d}".format(tenths)
    img = cv2.putText(screen, "Time: ", (10,200), font,3, (255,255,0), 8, cv2.LINE_AA)
    img = cv2.putText(img, message, (855,200), font,3, (255,255,0), 8, cv2.LINE_AA) 
    img = cv2.putText(img, "Pull-ups:", (10,300), font,3, (255,255,0), 8, cv2.LINE_AA) 
    img = cv2.putText(img, "Push-ups:", (10,400), font,3, (255,255,0), 8, cv2.LINE_AA) 
    img = cv2.putText(img, "Squats:", (10,500), font,3, (255,255,0), 8, cv2.LINE_AA) 
    
    total_time = seconds+ minutes*60 
    lap_time = (total_time%lap_length)
    if lap_time >= lap_length-1:
        lap_time = 0
        pull_count = 0
        push_count = 0
        squat_count = 0
    
    
    #15 seconds
    if lap_time <= TIME_TO_DO_PULL_UPS and lap_time/(TIME_TO_DO_PULL_UPS/5) > pull_count:
        pull_count +=1
        pull_ups +=1
    img = cv2.putText(img, "{0:0=3d}".format(pull_ups), (1100,300), font,3, (255,255,0), 8, cv2.LINE_AA) 
    
    #15 seconds
    if lap_time > TIME_TO_DO_PULL_UPS and lap_time <= TIME_TO_DO_PULL_UPS+TIME_TO_DO_PUSH_UPS and (lap_time-TIME_TO_DO_PULL_UPS)/(TIME_TO_DO_PUSH_UPS/10) > push_count:
        push_count +=1
        push_ups +=1
    img = cv2.putText(img, "{0:0=3d}".format(push_ups), (1100,400), font,3, (255,255,0), 8, cv2.LINE_AA)
    
    #20 seconds
    if lap_time > TIME_TO_DO_PULL_UPS+TIME_TO_DO_PUSH_UPS and lap_time <= TIME_TO_DO_PULL_UPS+TIME_TO_DO_PUSH_UPS+TIME_TO_DO_SQUATS and (lap_time-TIME_TO_DO_PULL_UPS-TIME_TO_DO_PUSH_UPS)/(TIME_TO_DO_SQUATS/15) > squat_count:
        squat_count +=1
        squats +=1
        if squat_count == 15:
            laps+=1
    img = cv2.putText(img, "{0:0=3d}".format(squats), (1100,500), font,3, (255,255,0), 8, cv2.LINE_AA)
    img = cv2.putText(img, "{0:0=2d}".format(laps), (1160,600), font,3, (255,255,0), 8, cv2.LINE_AA)
    img = cv2.putText(img, "Laps:", (10,600), font,3, (255,255,0), 8, cv2.LINE_AA)
    
    progress = (pull_ups+push_ups+squats)/600.0
    
    start_point = (20, 750) 
    end_point = (1220, 800) 
    color = (255,255,0) 
    thickness = 2
    img = cv2.rectangle(img, start_point, end_point, color, thickness) 
    img = cv2.rectangle(img, start_point, (20+int(1200*progress),800), color, -1) 
    img = cv2.putText(img, str(int(progress*100))+"%",(20+int(1200*progress)-15,720), font,1, (255,255,0), 1, cv2.LINE_AA)
    
    
    img = cv2.putText(img, "MURPH CHALLENGE", (180,100), font,3, (255,255,0), 8, cv2.LINE_AA)

    if laps == 2: #should be 20
        screen = 64*np.ones((850,1300,3), np.uint8)
        img = cv2.putText(screen, "Complete", (250,500), font,6, (255,255,0), 8, cv2.LINE_AA)
        cv2.imshow("timer", img)  
        cv2.waitKey(0)
    
    

    
    cv2.imshow("timer", img)  
    cv2.waitKey(1)