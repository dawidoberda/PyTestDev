import json
import click
import requests
import os



def post_request_from_config(tests_dir, test_seq):

    step_list = []

    try:
        with open(test_seq) as seq:
            tests = json.load(f)
    except FileNotFoundError as fnfe:
        print(str(fnfe))
        exit(1)

    # try:
    #     with open(file) as f:
    #         request = json.load(f)
    # except FileNotFoundError as fnfe:
    #     print(str(fnfe))
    #     exit(1)
    #
    # print(request)
    #
    #
    # response = requests.post('http://192.168.0.90/axis-cgi/papi/commands', json = request)
    #
    # print("Status code: ", response.status_code)
    # print("Printing Entire Post Request")
    # print(response.json())


if __name__ == "__main__":
    tests_dir = "C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req\\tests"
    test_seq = os.path.join("C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req", "sample_test_seq.txt")
    post_request_from_config(tests_dir=tests_dir, test_seq=test_seq)