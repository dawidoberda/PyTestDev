from pyzbar.pyzbar import decode
from PIL import Image


class QR_Reader:

    """
    Method which allows to read bar code from file
    :param filename : path with qr_code to decode
    """
    def read(self, filename):
        d = decode(Image.open(filename))
        return d[0].data.decode('ascii')


if __name__ == '__main__':
    reader = QR_Reader()
    file_path = '../output/qr_code.png'
    print(reader.read(file_path))
