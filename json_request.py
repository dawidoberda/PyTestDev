import json
import click
import requests
import os



def post_request_from_config(self, file):

    try:
        with open(file) as f:
            request = f.read()
    except FileNotFoundError as fnfe:
        print(str(fnfe))
        exit(1)

    print(request)

    # response = requests.post('http://192.168.0.90/papi/index.html', json={'id': 1, 'name': 'Jessa'})
    #
    # print("Status code: ", response.status_code)
    # print("Printing Entire Post Request")
    # print(response.json())

if __name__ == "__main__":
    file = os.path.join("C:\Users\oberdad\OneDrive - Jabil\Dawid\TE\Axis\json_req", "sample.txt")
    post_request_from_config()