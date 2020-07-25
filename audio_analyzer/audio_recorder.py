import sounddevice as sd
from scipy.io.wavfile import write
from os import path


class Recorder:

    """Class constructor
    :param samplerate: type int. define sampling frequency of recording
    :param output_file: type path. output file name with recorded sound
    """
    def __init__(self, samplerate, output_file):
        self.samplerate = samplerate
        self.output_file = output_file

    """
    Method to record sound and save as wave
    :param duration: type int. recording duration in seconds
    """
    def record(self, duration):
        myrecording = sd.rec(int(duration * self.samplerate), samplerate=self.samplerate, channels=2)
        sd.wait()
        if path.exists(self.output_file):
            write(self.output_file, self.samplerate, myrecording)
        else:
            raise FileNotFoundError("Given path cannot by found")


if __name__ == "__main__":
    sp = 44100
    out_file = path.join('../output', 'output.wav')
    recorder = Recorder(sp, out_file)
    recorder.record(2)
