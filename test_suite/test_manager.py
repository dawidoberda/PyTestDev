#TODO: tutaj zrobic i zapisywanie do bazy danych i generowanie raportow
#TODO: dodac zapisywanie danych do bazy danych. polaczyc to w jakis sposob z configure_test. najlepiej tak aby przez configure przekazywac tylko adres i credentials do bazy
#jak by sie pojawial jakis nastepny rodzaj testu to tez trzeba tutaj go dodac w warunkach stop_test

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import sqlite3

class Test_Manager:

    serial_number = None
    total_test_result = None

    def start_test(self, diagnostic_mode, serial_number=None):
        if diagnostic_mode==True:
            pass
        elif diagnostic_mode==False:
            if serial_number == None:
                raise ValueError("Serial number cannot by empty")
            else:
                self.serial_number = serial_number

    def stop_test(self, automatic_test_results = None, configure_test_results = None ):
        tests_results = {}
        if automatic_test_results == None:
            if configure_test_results == None:
                raise ValueError("Empty test results")
            else:
                tests_results = configure_test_results
        else:
            tests_results = automatic_test_results
            if configure_test_results != None:
                tests_results.update(configure_test_results)

        print(tests_results)



        engine = create_engine('sqlite:///:memory:', echo=True)
        meta = MetaData()
        Test_Results = Table(
            'Test_Results', meta,
            Column('id', Integer, primary_key=True),
            Column('Serial_Number', String),
            Column('Test_Result', String),
            Column('Error_Code', String),
        )
        meta.create_all(engine)



