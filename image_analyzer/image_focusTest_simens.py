import numpy as np
import cv2
import os
from image_analyzer.image_markers import Marker
import time
import json

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
        target_tmp = marker.find_marker_position(image_path=filename)
        cv2.imwrite("tmp/target_tmp.png", target_tmp)

        with open('./tmp/marker_position.txt') as f:
            marker_positions_rect = json.load(f)

        marker0 = marker_positions_rect.get('0')
        marker1 = marker_positions_rect.get('1')
        marker2 = marker_positions_rect.get('2')
        marker3 = marker_positions_rect.get('3')

        #TODO: dalej pracowac



if __name__ == "__main__":
    focusTest = SimensFocus()
    filename = "..\\output\\target.png"
    result = focusTest.middle_focus(filename)
