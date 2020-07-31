from imutils.video import VideoStream
import imutils
import cv2
import time

class ImageStream:

    vs = None

    def __init__(self, source):
        self.source = source

    def start_stream(self):
        self.vs = VideoStream(src = self.source).start()
        time.sleep(1.0)

        while True:
            frame = self.vs.read()
            frame = imutils.resize(frame, width=800, height=600)
            cv2.putText(frame, "Press esc to close window", (30, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Live image', frame)

            key = cv2.waitKey(1)

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            elif key == 27:
                break

        cv2.destroyAllWindows()
        self.vs.stop()

class cv2_imageStream:
    pass #sprobowac napisac ta klase na nowo przy uzyciu tylko cv2. przyklad : https://stackoverflow.com/questions/50058811/how-to-access-video-stream-from-an-ip-camera-using-opencv-in-python/50060784

if __name__ == "__main__":
    im = ImageStream(0)

    im.start_stream()