import serial
import time

class PSU():
    ser = None

    def __init__(self, com):
        """
        Creat object with hold reference to control Korad power supply
        :param com: Com port with connected psu
        """
        self.com = com

        self.ser = serial.Serial()

        self.ser.port = self.com
        self.ser.baudrate = 9600
        self.ser.parity = serial.PARITY_NONE
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 0.5

    def identyfication(self):
        """
        get korad psu identyficator
        :return: korad identyficator is serial success, None if SerialException
        """
        try:
            self.ser.open()
            self.ser.write('*IDN?'.encode())
            time.sleep(0.1)
            received = self.ser.read(100)
            self.ser.flush()
            self.ser.close()
            return received
        except serial.SerialException as se:
            print(str(se))
            received = None
            return received

    def setVoltage(self,voltage):
        """
        Set output voltage
        :param voltage: voltage which will be set on output
        :return: None
        """
        typ = type(voltage)
        if typ is not float:
            raise TypeError('Value need to by float! Received falue is {}'.format(typ))
        if voltage < 0 or voltage > 30.0:
            raise ValueError('Value need to by between 0 and 30')
        try:
            self.ser.open()
            self.ser.write(f'VSET1:{voltage}'.encode())
            time.sleep(0.1)
            self.ser.flush()
            self.ser.close()
        except serial.SerialException as se:
            print(str(se))

    def setCurrent(self,current):
        """
        Set current on output
        :param current: Current which will be set on output
        :return: None
        """
        typ = type(current)
        if typ is not float:
            raise TypeError('Value need to by float! Received falue is {}'.format(typ))
        if current < 0 or current >= 5.0:
            raise ValueError('Value need to by between 0 and 5')
        try:
            self.ser.open()
            self.ser.write(f'ISET1:{current}'.encode())
            time.sleep(0.1)
            self.ser.flush()
            self.ser.close()
        except serial.SerialException as se:
            print(str(se))

    def getSet_Voltage(self):
        """
        Return voltage set to output
        :return: voltage set to output
        """
        try:
            self.ser.open()
            self.ser.write('VSET1?'.encode())
            time.sleep(0.1)
            voltage = float(self.ser.read(50))
            self.ser.flush()
            self.ser.close()
            return voltage
        except serial.SerialException as se:
            print(str(se))
            voltage = None
            return voltage

    def getSet_Current(self):
        """
        Return current set to output
        :return: Return current set to output
        """
        try:
            self.ser.open()
            self.ser.write('ISET1?'.encode())
            time.sleep(0.1)
            current_str = str(self.ser.read(50))
            current_str_replaced = current_str.replace("K","")
            current_str_replaced = current_str_replaced.replace("b'","")
            current_str_replaced = current_str_replaced.replace("'","")
            current = float(current_str_replaced)
            self.ser.flush()
            self.ser.close()
            return current
        except serial.SerialException as se:
            print(str(se))
            current = None
            return current

    def getActual_Voltage(self):
        """
        Get supplied voltage
        :return: voltage on output
        """
        try:
            self.ser.open()
            self.ser.write('VOUT1?'.encode())
            time.sleep(0.1)
            voltage = float(self.ser.read(50))
            self.ser.flush()
            self.ser.close()
            return voltage
        except serial.SerialException as se:
            print(str(se))
            return None

    def getActual_Current(self):
        """
        Get supplied current
        :return: Current on output
        """
        try:
            self.ser.open()
            self.ser.write('IOUT1?'.encode())
            time.sleep(0.1)
            current = float(self.ser.read(50))
            self.ser.flush()
            self.ser.close()
            return current
        except serial.SerialException as se:
            print(str(se))
            return None

    def output_on(self):
        """
        Turn On output
        :return: None
        """
        try:
            self.ser.open()
            self.ser.write('OUT1'.encode())
            time.sleep(0.1)
            self.ser.flush()
            self.ser.close()
        except serial.SerialException as se:
            print(str(se))

    def output_off(self):
        """
        Turn Off output
        :return: None
        """
        try:
            self.ser.open()
            self.ser.write('OUT0'.encode())
            time.sleep(0.1)
            self.ser.flush()
            self.ser.close()
        except serial.SerialException as se:
            print(str(se))

if __name__=="__main__":
    """
    Kind of psu self test
    """
    psu = PSU('COM9')
    print(psu.identyfication())
    psu.setVoltage(3.3)
    psu.output_on()
    time.sleep(2)
    psu.output_off()