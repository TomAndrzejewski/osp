import cv2
import numpy as np
import json

def Colordetection(RR, GG, BB):

    color = 0
    R = np.array(RR, dtype = np.uint8)
    G = np.array(GG, dtype = np.uint8)
    B = np.array(BB, dtype = np.uint8)
    myDict=json.loads('{"Image Pixels (U8)":[[]],"Image Pixels (U8) 2":[[]],"Image Pixels (U8) 3":[[]],"element":0}')
    
    frame = cv2.merge([B, G, R])
    #success, img = cap.read()
    (oB, oG, oR) = cv2.split(frame)
    #frame = cv2.resize(image, (500, 500))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Żółty
    low_yellow = np.array([25, 58, 99])
    high_yellow = np.array([31, 252, 164])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    contours, hierarchy = cv2.findContours(yellow_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    areaSet = 2000
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSet):
            color = 1
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y),
                                (x + w, y + h),
                                (0, 255, 255), 2)

            cv2.putText(frame, "Yellow", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 255))


    # Czerwony
    low_red = np.array([0, 97, 57])
    high_red = np.array([8, 250, 127])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    contours, hierarchy = cv2.findContours(red_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSet):
            color=2
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y),
                                    (x + w, y + h),
                                    (0, 0, 255), 2)

            cv2.putText(frame, "Red", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))


    # Zielony
    low_green = np.array([49, 63, 61])
    high_green = np.array([89, 189, 120])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    contours, hierarchy = cv2.findContours(green_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSet):
            color = 3
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y),
                                        (x + w, y + h),
                                        (0, 255, 0), 2)

            cv2.putText(frame, "Green", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))


    # Niebieski
    low_blue = np.array([101, 80, 45])
    high_blue = np.array([118, 225, 129])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    contours, hierarchy = cv2.findContours(blue_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSet):
            color = 4
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y),
                                (x + w, y + h),
                                (255, 0, 0), 2)

            cv2.putText(frame, "Blue", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (255, 0, 0))


    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    if (color != 0):
        retFrame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        (retB, retG, retR) = cv2.split(frame)

        myDict["Image Pixels (U8)"] = retR.tolist()
        myDict["Image Pixels (U8) 2"] = retG.tolist()
        myDict["Image Pixels (U8) 3"] = retB.tolist()
        myDict["element"] = color
        MyJson = json.dumps(myDict)

        return MyJson
    else:
        myDict["Image Pixels (U8)"] = oR.tolist()
        myDict["Image Pixels (U8) 2"] = oG.tolist()
        myDict["Image Pixels (U8) 3"] = oB.tolist()
        myDict["element"] = color
        MyJson = json.dumps(myDict)

        return MyJson 
        
    
