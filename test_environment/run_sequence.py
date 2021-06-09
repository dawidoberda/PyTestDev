import os
import datetime

class sequence_runner:
    test_sequence_name = None
    bar_code = ''
    report_path = ''

    def __init__(self, test_sequence_name, bar_code, report_path):
        self.test_sequence_name = test_sequence_name
        self.bar_code = bar_code

        today_day = datetime.date.today()
        today_hour = datetime.datetime.now().strftime("%H_%M_%S")
        self.report_path = os.path.join(report_path, f'test_report_{bar_code}_{today_day}_{today_hour}.html')

        print(self.report_path)

    def run_sequence(self):
        os.system(f'python -m pytest {self.test_sequence_name} --html={self.report_path}')

if __name__ == '__main__':
    runner = sequence_runner(r'./test_sequences/test_sample1.py', bar_code='1234', report_path='C:\data')
    runner.run_sequence()