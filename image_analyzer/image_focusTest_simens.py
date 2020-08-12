import numpy as np
import cv2
import os
from image_analyzer.image_markers import Marker
import time
import json
import math
import matplotlib.pyplot as plt
from scipy import signal

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
        marker0_middle_X = (marker0_width/2) + marker0_corner0[0]
        marker0_middle_Y = (marker0_height/2) + marker0_corner0[1]
        marker0_middle_point = (int(marker0_middle_X), int(marker0_middle_Y))
        cv2.drawMarker(target_tmp, (int(marker0_middle_X), int(marker0_middle_Y)), (0,0,255), cv2.MARKER_CROSS, 100,20,16)

        # MARKER 1
        marker1_width = marker1_corner1[0] - marker1_corner0[0]
        marker1_height = marker1_corner3[1] - marker1_corner0[1]
        marker1_middle_X = (marker1_width / 2) + marker1_corner0[0]
        marker1_middle_Y = (marker1_height / 2) + marker1_corner0[1]
        marker1_middle_point = (int(marker1_middle_X), int(marker1_middle_Y))
        cv2.drawMarker(target_tmp, (int(marker1_middle_X), int(marker1_middle_Y)), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        # MARKER 2
        marker2_width = marker2_corner1[0] - marker2_corner0[0]
        marker2_height = marker2_corner3[1] - marker2_corner0[1]
        marker2_middle_X = (marker2_width / 2) + marker2_corner0[0]
        marker2_middle_Y = (marker2_height / 2) + marker2_corner0[1]
        marker2_middle_point = (int(marker2_middle_X), int(marker2_middle_Y))
        cv2.drawMarker(target_tmp, (int(marker2_middle_X), int(marker2_middle_Y)), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        # MARKER 3
        marker3_width = marker3_corner1[0] - marker3_corner0[0]
        marker3_height = marker3_corner3[1] - marker3_corner0[1]
        marker3_middle_X = (marker3_width / 2) + marker3_corner0[0]
        marker3_middle_Y = (marker3_height / 2) + marker3_corner0[1]
        marker3_middle_point = (int(marker3_middle_X), int(marker3_middle_Y))
        cv2.drawMarker(target_tmp, (int(marker3_middle_X), int(marker3_middle_Y)), (0, 0, 255), cv2.MARKER_CROSS, 100, 20, 16)

        length = marker2_middle_X - marker0_middle_X
        factor = 2
        middle_size = length/factor
        print(middle_size)
        max_r = int((middle_size / 2) - 50)
        print(max_r)


        line02_mid_point = (int((marker0_middle_point[0]+marker2_middle_point[0])/2), int((marker0_middle_point[1]+marker2_middle_point[1])/2))

        line13_mid_point = (int((marker1_middle_point[0] + marker3_middle_point[0]) / 2),
                            int((marker1_middle_point[1] + marker3_middle_point[1]) / 2))

        line01_mid_point = (int((marker0_middle_point[0] + marker1_middle_point[0]) / 2),
                            int((marker0_middle_point[1] + marker1_middle_point[1]) / 2))

        line23_mid_point = (int((marker2_middle_point[0] + marker3_middle_point[0]) / 2),
                            int((marker2_middle_point[1] + marker3_middle_point[1]) / 2))

        simensStar_middle_X = ((line02_mid_point[0] * line13_mid_point[1] - line02_mid_point[1] * line13_mid_point[0]) * (line01_mid_point[0] - line23_mid_point[0]) - (line02_mid_point[0] - line13_mid_point[0]) * (line01_mid_point[0] * line23_mid_point[1] - line01_mid_point[1] * line23_mid_point[0])) / (
                    (line02_mid_point[0] - line13_mid_point[0]) * (line01_mid_point[1] - line23_mid_point[1]) - (line02_mid_point[1] - line13_mid_point[1]) * (line01_mid_point[0] - line23_mid_point[0]))
        simensStar_middle_Y = ((line02_mid_point[0] * line13_mid_point[1] - line02_mid_point[1] * line13_mid_point[0]) * (line01_mid_point[1] - line23_mid_point[1]) - (line02_mid_point[1] - line13_mid_point[1]) * (line01_mid_point[0] * line23_mid_point[1] - line01_mid_point[1] * line23_mid_point[0])) / (
                    (line02_mid_point[0] - line13_mid_point[0]) * (line01_mid_point[1] - line23_mid_point[1]) - (line02_mid_point[1] - line13_mid_point[1]) * (line01_mid_point[0] - line23_mid_point[0]))

        siemensX = 0
        siemensY = 0
        #find pizza marker
        target_gray = cv2.cvtColor(target_tmp, cv2.COLOR_BGR2GRAY)
        print(f'y1 = {int(simensStar_middle_X - (middle_size/2)+50)}')
        print(f'y2 = {int(simensStar_middle_X + (middle_size/2)+50)}')
        print(f'x1 = {int(simensStar_middle_Y - (middle_size/2)+50)}')
        print(f'x2 = {int(simensStar_middle_Y + (middle_size/2)+50)}')
        siemens_estimated_position = target_tmp[int(simensStar_middle_Y - (middle_size/2)-50):int(simensStar_middle_Y + (middle_size/2)+50),
                                     int(simensStar_middle_X - (middle_size/2)-50):int(simensStar_middle_X + (middle_size/2)+50)]

        siemens_estimated_position_grey = cv2.cvtColor(siemens_estimated_position, cv2.COLOR_BGR2GRAY)
        #template = cv2.imread('./image/pizza_marker.png')
        template = cv2.imread('./image/template.PNG')
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        print(f'w= {w} ; h = {h}')
        res = cv2.matchTemplate(siemens_estimated_position_grey, template, cv2.TM_CCOEFF_NORMED)

        # FOR DEBUG OF MATCH TEMPLATE
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1920, 1080)
        cv2.imshow('image', res)
        key = cv2.waitKey(0)

        cv2.destroyAllWindows()

        threshold = 0.7
        maximum = np.amax(res)
        print(maximum)
        loc = np.where(res >= threshold)
        print(loc)

        if loc[0].size == 0:
            raise ValueError('Mach template array is empty ! Template not found')

        for pt in zip(*loc[::-1]):
            # cv2.rectangle(siemens_estimated_position, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            cv2.drawMarker(siemens_estimated_position, (pt[0]+int(w/2), pt[1]+int(h/2)), (0,0,255), cv2.MARKER_CROSS, 20, 4, 2)
            siemensX = pt[0]+int(w/2)
            siemensY = pt[1]+int(h/2)


        #DRAW MARKERS AND LINES
        line02 = cv2.line(target_tmp, marker0_middle_point, marker2_middle_point, (0, 0, 255), 4, 2)
        cv2.drawMarker(target_tmp, line02_mid_point, (0, 255, 0), cv2.MARKER_CROSS, 20, 4, 2)
        line13 = cv2.line(target_tmp, marker1_middle_point, marker3_middle_point, (0, 0, 255), 4, 2)
        cv2.drawMarker(target_tmp, line13_mid_point, (0, 255, 0), cv2.MARKER_CROSS, 20, 4, 2)
        line01 = cv2.line(target_tmp, marker0_middle_point, marker1_middle_point, (0, 0, 255), 4, 2)
        cv2.drawMarker(target_tmp, line01_mid_point, (0, 255, 0), cv2.MARKER_CROSS, 20, 4, 2)
        line23 = cv2.line(target_tmp, marker2_middle_point, marker3_middle_point, (0, 0, 255), 4, 2)
        cv2.drawMarker(target_tmp, line23_mid_point, (0, 255, 0), cv2.MARKER_CROSS, 20, 4, 2)
        vertical_middle_line = cv2.line(target_tmp, line02_mid_point, line13_mid_point, (52, 174, 235), 4, 2)
        horizontal_middle_line = cv2.line(target_tmp, line01_mid_point, line23_mid_point, (52, 174, 235), 4, 2)
        cv2.drawMarker(target_tmp, (int(simensStar_middle_X), int(simensStar_middle_Y)), (205, 18, 230),
                       cv2.MARKER_CROSS, 20, 4, 2)
        cv2.drawMarker(target_tmp, (int(simensStar_middle_X), int(simensStar_middle_Y)), (0, 255, 0), cv2.MARKER_SQUARE, int(middle_size), 20, 8)

        SFR_list = []
        circuit_list = []
        MTF = []
        max_r = int((w/2) * 7.5)
        print(max_r)
        Spoke = 144

        #Calculation of Circuits
        for r in range(max_r, int((w/2)-30), -10):
            circuit = int(2 * math.pi * r)
            circuit_list.append(circuit)
            # print(f'circuit = {circuit}')

        #Calculation of SFR
        for circuit in circuit_list:
            SFR = Spoke / circuit  # SFR is in lp/pixel
            SFR_list.append(SFR)
            # print(f'SFR = {SFR} lp/pixel')


        fts = (2 * Spoke) / circuit_list[0] # fts = 2 * SFR due to Nyquist rule, sampling freq is the same for all cicruits so only one is calculated
        probe_point_qty = circuit_list[0] * fts  #so it's equal to 2 * spoke

        sample_contrast = []

        for r in range(max_r, int((w / 2) - 30), -10):
            points = []
            contrast = []

            for alfa_deg in range(1, 36000, 125):
                alfa = alfa_deg / 100
                alfa_rad = (alfa * math.pi) / 180
                x = r * math.cos(alfa_rad)
                y = r * math.sin(alfa_rad)
                px = int(siemensX - x)
                py = int(siemensY - y)
                p = [px, py]
                points.append(p)
                c = siemens_estimated_position_grey[px, py]
                contrast.append(c)
                cv2.circle(siemens_estimated_position, (px, py), 1, (0, 0, 255), 1, 1)  # for debug


            # if r > int((w / 2) - 30) and r <= int((w / 2) - 30) +10 :
            #     sample_contrast = contrast

            if r > 500 and r <= 510 :
                sample_contrast = contrast

            Imax = max(contrast)
            Imin = min(contrast)
            print(f'Imax = {Imax}')
            print(f'Imin = {Imin}')
            Modulation = (Imax - Imin) / (Imax + Imin)
            MTF.append(Modulation)
            print(f'Modulation = {Modulation}')


        plt.figure(1)
        plt.plot(circuit_list, SFR_list)
        plt.title('SFR / Circuit ')
        plt.xlabel('Circuit [pixel]')
        plt.ylabel('SFR [lp/pixel]')
        #plt.show()
        plt.savefig('../output/SFR_middle_simens.png')


        plt.figure(2)
        plt.plot(SFR_list, MTF)
        plt.title('MTF Middle')
        plt.xlabel('SFR [lp/pixel]')
        plt.ylabel('MTF')
        #plt.show()
        plt.savefig('../output/MTF_Middle.png')

        plt.figure(3)
        plt.plot(sample_contrast)
        plt.title('Sample contrast')
        plt.xlabel('Position')
        plt.ylabel('Contrast')
        plt.show()
        plt.savefig('../output/sample_contrast.png')

        cv2.imwrite('tmp/siemens_estimated_position.png', siemens_estimated_position)
        cv2.imwrite("tmp/target_tmp.png", target_tmp)

if __name__ == "__main__":
    focusTest = SimensFocus()
    #filename = "..\\output\\target.png"
    #filename = "..\\output\\target_7x5.png"
    #filename = "..\\output\\test_target_photo - low.png"
    filename = "..\\output\\test_target_photo.png"
    #filename = "..\\output\\target_test.png"
    result = focusTest.middle_focus(filename)
