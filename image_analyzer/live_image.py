from imutils.video import VideoStream
import imutils
import cv2
import time

# vs = VideoStream(src=0).start()
# time.sleep(1.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=800, height=600)
    cv2.imshow('Live image', frame)

    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()


class ImageStream:

    vs = None

    def __init__(self,source):
        self.source = source

    def start_stream(self):
        self.vs = VideoStream(self.source).start()
        time.sleep(1.0)

        # TODO: zrobic metode ktora pokazuje obraz. sprawdzic tez jak zrobic aby zatrzymywala sie na jakis inny sygnal oprocz przycisku