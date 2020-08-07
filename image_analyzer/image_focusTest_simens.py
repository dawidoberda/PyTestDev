import numpy as np
import cv2
import os
from image_analyzer.image_markers import Marker
import time
import json
import math

class SimensFocus:


    def middle_focus(self, filename):
        marker = Marker()
        exist = os.path.exists(filename)
        if exist == False:
            raise FileExistsError('Cannot find given file')
        try:
            target = cv2.imread(filename)
        except FileNotFoundError as fnfe:
            return str(fnfe)
        except :
            return "Other error occur"

        #target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite("../output/target_gray.png", target)
        x, y, color = target.shape
        middle_size = 0
        if x == 7000:
            middle_size = 3000

        time.sleep(1)
        target_tmp = marker.find_marker_position(image_path=filename, show_image=False)
        #cv2.imwrite("tmp/target_tmp.png", target_tmp)

        with open('./tmp/marker_position.txt') as f:
            marker_positions_rect = json.load(f)

        marker0 = marker_positions_rect.get('0')
        marker1 = marker_positions_rect.get('1')
        marker2 = marker_positions_rect.get('2')
        marker3 = marker_positions_rect.get('3')

        marker0_corner0 = marker0[0][0]
        marker0_corner1 = marker0[0][1]
        marker0_corner2 = marker0[0][2]
        marker0_corner3 = marker0[0][3]
        marker1_corner0 = marker1[0][0]
        marker1_corner1 = marker1[0][1]
        marker1_corner2 = marker1[0][2]
        marker1_corner3 = marker1[0][3]
        marker2_corner0 = marker2[0][0]
        marker2_corner1 = marker2[0][1]
        marker2_corner2 = marker2[0][2]
        marker2_corner3 = marker2[0][3]
        marker3_corner0 = marker3[0][0]
        marker3_corner1 = marker3[0][1]
        marker3_corner2 = marker3[0][2]
        marker3_corner3 = marker3[0][3]

        #MARKER 0
        marker0_width = marker0_corner1[0] - marker0_corner0[0]
        marker0_height = marker0_corner3[1] - marker0_corner0[1]
        marker0_middle_X = int((marker0_width/2) + marker0_corner0[0])
        marker0_middle_Y = int((marker0_height/2) + marker0_corner0[1])
        cv2.drawMarker(target_tmp, (marker0_middle_X, marker0_middle_Y), (0,0,255), cv2.MARKER_CROSS, 100,20,16)

        # MARKER 1
        marker1_width = marker1_corner1[0] - marker1_corner0[0]
        marker1_height = marker1_corner3[1] - marker1_corner0[1]
        marker1_middle_X = int((marker1_width / 2) + marker1_corner0[0])
        marker1_middle_Y = int((marker1_height / 2) + marker1_corner0[1])
        cv2.drawMarker(target_tmp, (marker1_middle_X, marker1_middle_Y), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        # MARKER 2
        marker2_width = marker2_corner1[0] - marker2_corner0[0]
        marker2_height = marker2_corner3[1] - marker2_corner0[1]
        marker2_middle_X = int((marker2_width / 2) + marker2_corner0[0])
        marker2_middle_Y = int((marker2_height / 2) + marker2_corner0[1])
        cv2.drawMarker(target_tmp, (marker2_middle_X, marker2_middle_Y), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        # MARKER 3
        marker3_width = marker3_corner1[0] - marker3_corner0[0]
        marker3_height = marker3_corner3[1] - marker3_corner0[1]
        marker3_middle_X = int((marker3_width / 2) + marker3_corner0[0])
        marker3_middle_Y = int((marker3_height / 2) + marker3_corner0[1])
        cv2.drawMarker(target_tmp, (marker3_middle_X, marker3_middle_Y), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        simensStar_middle_X = int(((marker2_middle_X - marker0_middle_X)/2) + marker0_middle_X)
        simensStar_middle_Y = int(((marker1_middle_Y - marker0_middle_Y)/2) + marker0_middle_Y)

        cv2.drawMarker(target_tmp, (simensStar_middle_X, simensStar_middle_Y), (0, 255, 0), cv2.MARKER_SQUARE, middle_size, 20, 8)
        target_gray = cv2.cvtColor(target_tmp, cv2.COLOR_BGR2GRAY)
        for r in range(1450, 50, -10):
            points = []
            contrast = []
            for alfa_deg in range(1, 360, 1):
                alfa_rad = (alfa_deg*math.pi)/180
                x = r * math.cos(alfa_rad)
                y = r * math.sin(alfa_rad)
                px = int(simensStar_middle_X - x)
                py = int(simensStar_middle_Y - y)
                p = [px, py]
                points.append(p)
                c = target_gray[px, py]
                contrast.append(c)
                cv2.circle(target_tmp, (px, py), 1, (0, 0, 255), 1, 1) #for debug
            print(contrast)
            #TODO : zrobic max i min i wtedy intens


        cv2.imwrite("tmp/target_tmp.png", target_tmp)

if __name__ == "__main__":
    focusTest = SimensFocus()
    filename = "..\\output\\target.png"
    result = focusTest.middle_focus(filename)
