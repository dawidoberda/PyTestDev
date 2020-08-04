#https://docs.opencv.org/trunk/d5/dae/tutorial_aruco_detection.html
#https://datigrezzi.com/2019/11/12/markers-detection-perspective-transformation-opencv-python/
#https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html

import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
from image_analyzer.live_image import cv2_imageStream
import json

class Marker:

    def generate_marker(self, id):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.img = aruco.drawMarker(aruco_dict, id, 700)
        plt.imshow(self.img, cmap=mpl.cm.gray, interpolation="nearest")
        plt.show()

    def save_marker(self, file):
        plt.imshow(self.img, cmap=mpl.cm.gray, interpolation="nearest")
        plt.savefig(file)

    def find_marker_position(self, image_path):
        frame = cv2.imread(image_path)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters_create()
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

        plt.figure()
        plt.imshow(frame_markers)
        plt.show()

        for i in range(len(ids)):
            rectangle = corners[i][0]
        return rectangle

    def show_marker_live(self, camera_number, snap_path, markers_path):

        class MarkerLive(cv2_imageStream):

            def start_stream(self, snap_path, markers_path):

                gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
                parameters = aruco.DetectorParameters_create()
                corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
                frame_markers = aruco.drawDetectedMarkers(self.frame.copy(), corners, ids)

                cv2.putText(frame_markers, "Press esc to close window", (30, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

                cv2.putText(frame_markers, "Press s to take snap", (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                cv2.imshow('Live Image', frame_markers)

                key = cv2.waitKey(1)

                # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                    self.cap.release()
                    cv2.destroyAllWindows()
                    exit()
                elif key == 27:
                    self.cap.release()
                    cv2.destroyAllWindows()
                    exit()
                elif key == ord("s"):
                    cv2.imwrite(snap_path, frame_markers)
                    i =0
                    markers_dic = {}
                    for id in ids:
                        x = {int(id): corners[i].tolist()}
                        markers_dic.update(x)
                        i = i + 1
                    with open(markers_path, 'w') as outfile:
                        json.dump(markers_dic, outfile)
                    exit()




        ml = MarkerLive(camera_number)
        while True:
            try:
                ml.start_stream(snap_path, markers_path)
            except AttributeError as ae:
                pass


if __name__ == "__main__":
    marker = Marker()
    #marker.generate_marker(2)
    #file_path = os.path.join("../output", "gen_aruco_marker2.png")
    #marker.save_marker(file_path)

    #positions = marker.find_marker_position("../output/snap.png")
    #print(positions)

    marker.show_marker_live(0, snap_path="../output/snap_live.png", markers_path='../output/markers.txt')
