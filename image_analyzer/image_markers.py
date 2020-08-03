#https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html
#https://datigrezzi.com/2019/11/12/markers-detection-perspective-transformation-opencv-python/
#https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html

import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

class Marker:

    def generate_marker(self, id):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.img = aruco.drawMarker(aruco_dict, id, 700)
        plt.imshow(self.img, cmap=mpl.cm.gray, interpolation="nearest")
        plt.show()

    def save_marker(self, file):
        plt.imshow(self.img, cmap=mpl.cm.gray, interpolation="nearest")
        plt.savefig(file)
#TODO: find marker

if __name__ == "__main__":
    marker = Marker()
    marker.generate_marker(1)
    file_path = os.path.join("../output", "gen_aruco_marker.png")
    marker.save_marker(file_path)