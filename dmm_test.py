# dmm_test.py

import dmm_keysight as dk
import click

@click.command()
def test():
    print('DMM class. Start Test')

    dmm = dk.DMM()

    connection_successful = dmm.connect('TCPIP0::K-34461A-09586.local::hislip0::INSTR')

    if not connection_successful:
        exit()

    print(dmm.identificator())

    self_test = dmm.selftest()

    print(self_test)

    if self_test == '+0\n':
        print('self test is pass')
    else:
        print('self test is fail')


if __name__=="__main__":
    test()