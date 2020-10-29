

class Automatic_Test:

    test_list = []
    results_dict = {}

    def add_step(self, test_name):
        self.test_list.append(test_name)


    def test_result(self, test_name, test_result, fail_code=None, error_code=None):
        if test_name in self.test_list:
            if test_result == "PASS":
                print("PASS")
            elif test_result == "FAIL":
                print("FAIL")
                print(f'Fail description is {fail_code}')
            elif test_result == 'ERROR':
                print("ERROR")
                print(f'Error code is {error_code}')
            else:
                print("ERROR")
                test_result = 'ERROR'
                print('RESULT UNKNOWN')

            self.results_dict[test_name] = test_result

        else:
            print("TEST IS NOT IN DEFINED TEST LIST")


    def return_results(self):
        return self.results_dict