import pyqrcode

class QR_Writer:

    qr = None

    """
    Method to generate qr code
    :param value: this value will be coded in qr code
    """
    def generate(self, value):
        self.qr = pyqrcode.create(value)


    """
    Method to save generated qr code into file
    :param filename: path where qr code will be stored
    :param scale : scale of saved file
    """
    def save(self, filename, scale):
        self.qr.png(filename, scale=scale)


if __name__ == "__main__":
    writer = QR_Writer()
    writer.generate('1234')
    file_path = '../output/qr_code.png'
    writer.save(file_path, scale=8)


