#Stream z kamery ip powinien dzialac tak samo. Wystarczy w argumencie camera_number zamiast 0 podac adress http streamu

import numpy as np
import cv2


class Image_Capture:


    """
    Method to take picture
    :param camera_number : type int, camera to be used to take picture
    :param filepath : type path, filename where taken picture should be save at
    """
    def take_picture(self, camera_number, filepath):
        cap = cv2.VideoCapture(camera_number)
        ret, frame = cap.read()
        cv2.imwrite(filepath, frame)
        cap.release()


if __name__ == "__main__":
    ic = Image_Capture()
    filename = '../output/img_saved.png'
    ic.take_picture(0, filename)
