import os

class sequence_runner:
    test_sequence_name = None
    bar_code = ''

    def __init__(self, test_sequence_name, bar_code):
        self.test_sequence_name = test_sequence_name
        self.bar_code = bar_code

    def run_sequence(self):
        os.system(f'python -m pytest {self.test_sequence_name}') # zrobic zapis do html report z aktualna godzina, data, nazwa sek i barcodem

if __name__ == '__main__':
    runner = sequence_runner(r'./test_sequences/test_sample1.py', bar_code='1234')
    runner.run_sequence()