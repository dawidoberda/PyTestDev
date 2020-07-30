#https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/

from imutils.video import VideoStream
import imutils
import cv2
import time
from pyzbar.pyzbar import decode

vs = None

vs = VideoStream(src = 0).start()
time.sleep(1.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=800, height=600)


    barcodes = decode(frame)

    for barcode in barcodes:
        x, y, width, height = barcode.rect
        print(x)
        print(y)
        print(width)
        print(height)
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        print(barcodeData)

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Live image', frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
    elif key == 27:
        break

cv2.destroyAllWindows()
vs.stop()

