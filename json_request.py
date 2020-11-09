import json
import click
import requests
import os
import re
import test_suite
import time



def post_request_from_config(tests_dir, test_seq):

    step_list = []
    automatic_test = test_suite.automatic_test.Automatic_Test()

    test_manager = test_suite.test_manager.Test_Manager()
    test_manager.start_test(True)

    configure_test = test_suite.configure_test.Configure_Test()

    #LOADING TEST SEQ

    try:
        with open(test_seq) as f:
            sequence = json.load(f)
    except FileNotFoundError as fnfe:
        print(str(fnfe))
        exit(1)

    for key in sequence.keys():
        step_list.append(key)


    print(step_list)


    #EXECUTING SEQ
    for step in step_list:
        print(f'CURRENTLY EXECUTING STEP IS {step}')
        type_of_test = sequence.get(step)
        print(f'Type of present test is {type_of_test}')

        #AUTOMATIC STEP
        if type_of_test == 'automatic':

            automatic_test.add_step(step)

            step_file = os.path.join(tests_dir, step+".txt")

            exist = os.path.exists(step_file)

            if not exist:
                print("file not found !!")
                automatic_test.test_result(step, "ERROR", fail_code="file not found")
                exit(1)

            try:
                with open(step_file) as f:
                    request = json.load(f)
            except FileNotFoundError as fnfe:
                print(str(fnfe))
                automatic_test.test_result(step, "ERROR", fail_code="file not found")
                exit(1)

            #print(request)


            response = requests.post('http://192.168.0.90/axis-cgi/papi/commands', json = request)

            print("Status code: ", response.status_code)
            print("Printing Entire Post Request")
            print(response.json())

            #CHECKING CONDITIONS
            condition_file = os.path.join(tests_dir,"conditions",step+"_condition.txt")
            exist = os.path.exists(condition_file)

            if not exist:
                print("condition file is not exist!")
                automatic_test.test_result(step, "ERROR", fail_code="condition file is not exist!")
                exit(1)

            try:
                with open(condition_file) as f:
                    condition = json.load(f)
            except FileNotFoundError as fnfe:
                print(str(fnfe))
                automatic_test.test_result(step, "ERROR", fail_code="file not found")
                exit(1)

            condition_keys = condition.keys()
            #print(condition_keys)

            condition_to_check_list = []

            for key in condition_keys:
                actual_condition = condition.get(key)

                if type(actual_condition) == dict:
                    for inner_key in actual_condition.keys():
                        condition_to_check_list.append(actual_condition)
                else:
                    condition_to_check_list.append({key: actual_condition})

            print(f'coditions to check : {condition_to_check_list}')

            #Looking for condition in response
            for condition in condition_to_check_list:
                expected_key = str(condition.keys())

                a_string = expected_key
                result = re.search(r"\(\[\'([A-Za-z0-9-]+)\'\]\)", a_string)
                expected_key = result.group(1)

                print(f'expected key is {expected_key}')
                expected_value = condition.get(expected_key)
                print(f'expected value for this key is {expected_value}')

                #Testing for value
                response_json = response.json()
                response_dict = response_json.get('data')

                response_msg = str(response_dict)

                if expected_value == "True":
                    searched_string = f'\'{expected_key}\': {expected_value}'
                else:
                    searched_string = f'\'{expected_key}\': \'{expected_value}\''

                test_search = response_msg.find(str(searched_string))

                if not test_search == -1:
                    automatic_test.test_result(step, 'PASS')
                else:
                    automatic_test.test_result(step, "FAIL", fail_code="Condition not fulfilled")

        #MANUAL STEP
        elif type_of_test == 'manual':
            print('manual')

        #CONFIGURE STEP
        elif type_of_test == 'configure':
            print('configure')

        #WRITE-READ STEP
        elif type_of_test == "write-read":
            print("Write-Read")
            automatic_test.add_step(step)

            step_generic = str(step).split("_")
            step_name = step_generic[0]

            step_write_file = os.path.join(tests_dir, step_name+"_write.txt")
            step_read_file = os.path.join(tests_dir, step_name + "_read.txt")

            exist_write = os.path.exists(step_write_file)
            exist_read = os.path.exists(step_read_file)

            if not exist_write:
                print("write file not found !!")
                automatic_test.test_result(step, "ERROR", fail_code="write file not found !!")
                exit(1)

            if not exist_read:
                print("read file not found !!")
                automatic_test.test_result(step, "ERROR", fail_code="write file not found !!")
                exit(1)


            try:
                with open(step_write_file) as f:
                    request_write = json.load(f)
            except FileNotFoundError as fnfe:
                print(str(fnfe))
                automatic_test.test_result(step, "ERROR", fail_code="write file not found !!")
                exit(1)

            try:
                with open(step_read_file) as f:
                    request_read = json.load(f)
            except FileNotFoundError as fnfe:
                print(str(fnfe))
                automatic_test.test_result(step, "ERROR", fail_code="write file not found !!")
                exit(1)

            response = requests.post('http://192.168.0.90/axis-cgi/papi/commands', json=request_write)

            print("Status code: ", response.status_code)

            print("Wait for 3 seconds after posting write request..")
            time.sleep(3)

            response = requests.post('http://192.168.0.90/axis-cgi/papi/commands', json=request_read)

            print("Status code: ", response.status_code)
            print("Printing Entire Post Request")
            print(response.json())

            #CHECKING CONDITIONS
            condition_file = os.path.join(tests_dir,"conditions",step+"_condition.txt")
            exist = os.path.exists(condition_file)

            if not exist:
                print("condition file is not exist!")
                automatic_test.test_result(step, "ERROR", fail_code="condition file is not exist!")
                exit(1)

            try:
                with open(condition_file) as f:
                    condition = json.load(f)
            except FileNotFoundError as fnfe:
                print(str(fnfe))
                automatic_test.test_result(step, "ERROR", fail_code="condition file is not exist!")
                exit(1)

            condition_keys = condition.keys()

            condition_to_check_list = []

            for key in condition_keys:
                actual_condition = condition.get(key)

                if type(actual_condition) == dict:
                    for inner_key in actual_condition.keys():
                        condition_to_check_list.append(actual_condition)
                else:
                    condition_to_check_list.append({key: actual_condition})

            print(f'coditions to check : {condition_to_check_list}')

            #Looking for condition in response
            for condition in condition_to_check_list:
                expected_key = str(condition.keys())

                a_string = expected_key
                result = re.search(r"\(\[\'([A-Za-z0-9-]+)\'\]\)", a_string)
                expected_key = result.group(1)

                print(f'expected key is {expected_key}')
                expected_value = condition.get(expected_key)
                print(f'expected value for this key is {expected_value}')

                #Testing for value
                response_json = response.json()
                response_dict = response_json.get('data')

                response_msg = str(response_dict)


                if expected_value == "True" or str(expected_value).isnumeric():
                    searched_string = f'\'{expected_key}\': {expected_value}'
                else:
                    searched_string = f'\'{expected_key}\': \'{expected_value}\''

                test_search = response_msg.find(str(searched_string))

                if not test_search == -1:
                    automatic_test.test_result(step, 'PASS')
                else:
                    automatic_test.test_result(step, "FAIL", fail_code="Condition not fulfilled")



        print("===================================")

    automatic_results = None
    configure_results = None

    if automatic_test.return_results() != None:
        automatic_results = automatic_test.return_results()
    if configure_test.return_results() !=None:
        configure_results = configure_test.return_results()

    test_manager.stop_test(automatic_test_results=automatic_results, configure_test_results=configure_results)
    #TODO: dodac reszte testow i PAPI

if __name__ == "__main__":
    tests_dir = "C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req\\tests"
    test_seq = os.path.join("C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req", "sample_test_seq.txt")
    post_request_from_config(tests_dir=tests_dir, test_seq=test_seq)