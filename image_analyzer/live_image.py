from threading import Thread
import cv2
import time

class cv2_imageStream:

    def __init__(self, camera_number):
        self.camera_number = camera_number
        self.cap = cv2.VideoCapture(self.camera_number)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.FPS = 1 / 30

        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.cap.isOpened():
                (self.status, self.frame) = self.cap.read()
            time.sleep(self.FPS)

    """
    Method to start live image
    :param frame_return: type bool; if true method fill return frame as ndarray
    """
    def start_stream(self, frame_return):


        cv2.putText(self.frame, "Press esc to close window", (30, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Live Image', self.frame)



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

        if frame_return == True:
            return self.frame



if __name__ == "__main__":
    src = 0
    im = cv2_imageStream(src)
    while True:
        try:
            frame = im.start_stream(frame_return=False)
            if frame.any() == None:
                pass
            else:
                print(frame)
        except AttributeError as ae:
            pass