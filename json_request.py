import json
import click
import requests
import os



def post_request_from_config(tests_dir, test_seq):

    step_list = []

    #LOADING TEST SEQ
    try:
        with open(test_seq) as seq:
            for line in seq:
                line = line.rstrip('\n')
                step_list.append(str(line))
    except FileNotFoundError as fnfe:
        print(str(fnfe))
        exit(1)

    print(step_list)

    #EXECUTING SEQ
    for step in step_list:
        step_file = os.path.join(tests_dir, step+".txt")
        print(step_file)
        exist = os.path.exists(step_file)
        print(exist)

        if not exist:
            print("file not found !!")
            exit(1)

        try:
            with open(step_file) as f:
                request = json.load(f)
        except FileNotFoundError as fnfe:
            print(str(fnfe))
            exit(1)

        print(request)


        response = requests.post('http://192.168.0.90/axis-cgi/papi/commands', json = request)

        print("Status code: ", response.status_code)
        print("Printing Entire Post Request")
        print(response.json())

        #zrobic pliki konfiguracyjne co oznacza pass dla danego kroku i sprawdzanie tego w kodzie


if __name__ == "__main__":
    tests_dir = "C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req\\tests"
    test_seq = os.path.join("C:\\Users\\oberdad\\OneDrive - Jabil\\Dawid\\TE\\Axis\\json_req", "sample_test_seq.txt")
    post_request_from_config(tests_dir=tests_dir, test_seq=test_seq)