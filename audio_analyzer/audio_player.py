import sounddevice as sd
import soundfile as sf
from os import path


class Player:

    """
    Class constructor
    :param filename: type path. Store file name of file which will be played
    """
    def __init__(self, filename):
        self.filename = filename

    """
    Method to play sound
    """
    def play(self):
        if path.exists(self.filename):
            data, fs = sf.read(self.filename, dtype='float32')
            sd.play(data, fs)
            status = sd.wait()
        else:
            raise FileNotFoundError("Given file name cannot by found")


if __name__ == "__main__":
    fn = path.join('../output', 'output.wav')
    p = Player(fn)
    p.play()