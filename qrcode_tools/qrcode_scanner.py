#https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/

from imutils.video import VideoStream
import imutils
import cv2
import time
from pyzbar.pyzbar import decode

class QR_scanner:

    vs = None
    barcodeData = None

    """
    Method to run contiouns scaning
    """
    def continous_scan(self):

        self.vs = VideoStream(src = 0).start()
        time.sleep(1.0)

        while True:
            frame = self.vs.read()
            frame = imutils.resize(frame, width=800, height=600)

            barcodes = decode(frame)

            for barcode in barcodes:
                x, y, width, height = barcode.rect
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
                self.barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type


                text = "{} ({})".format(self.barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv2.putText(frame, "Press esc to close window", (30, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Live image', frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break
            elif key == 27:
                break

        cv2.destroyAllWindows()
        self.vs.stop()

    """Method to scan qr code and return if contains given mask
    :param mask: type str; mask which will be search in scanned qr code"""
    def scan(self, mask):
        self.vs = VideoStream(src = 0).start()
        time.sleep(1.0)

        while True:
            frame = self.vs.read()
            frame = imutils.resize(frame, width=800, height=600)

            barcodes = decode(frame)

            for barcode in barcodes:
                x, y, width, height = barcode.rect
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
                self.barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type


                text = "{} ({})".format(self.barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


            scanned_qrcode = str(self.barcodeData)
            contain_mask = scanned_qrcode.find(str(mask))

            if contain_mask != -1:
                cv2.putText(frame, "Press Enter to confirm!", (x, y + 30 + height),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break
            elif key == 27:
                break
            elif key == 13:
                break

            self.barcodeData = 0

            cv2.putText(frame, "Press esc to close window", (30, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Live image', frame)

        return scanned_qrcode
        cv2.destroyAllWindows()
        self.vs.stop()


if __name__ == "__main__":
    scanner = QR_scanner()
    #scanner.continous_scan()
    print(scanner.scan('12'))