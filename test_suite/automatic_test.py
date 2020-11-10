from dataclasses import dataclass
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import sqlite3

class Automatic_Test:

    test_list = []
    r = None
    engine = None
    Automatic_Test_Results = None

    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        meta = MetaData()
        self.Automatic_Test_Results = Table(
            'Automatic_Test_Results', meta,
            Column('id', Integer, primary_key=True),
            Column('Name', String),
            Column('Result', String),
            Column('Code', String),
        )
        meta.create_all(self.engine)

    @dataclass
    class Result:
        name: str
        result: str
        code: str = None


    def add_step(self, test_name):
        self.test_list.append(test_name)


    def test_result(self, test_name, test_result, code=None):
        if test_name in self.test_list:
            if test_result == "PASS":
                print("PASS")
            elif test_result == "FAIL":
                print("FAIL")
                print(f'Fail description is {code}')
            elif test_result == 'ERROR':
                print("ERROR")
                print(f'Error code is {code}')
            else:
                print("ERROR")
                test_result = 'ERROR'
                print('RESULT UNKNOWN')

            self.r = self.Result(name=test_name, result=test_result, code=code)

            ins = self.Automatic_Test_Results.insert().values(Name=self.r.name, Result=self.r.result, Code=self.r.code)
            conn = self.engine.connect()
            result = conn.execute(ins)

        else:
            print("TEST IS NOT IN DEFINED TEST LIST")


    def return_results(self):
        sel = self.Automatic_Test_Results.select()
        conn = self.engine.connect()
        sel_output = conn.execute(sel)
        return sel_output