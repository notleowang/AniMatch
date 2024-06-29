from api.controller import *
from data.build import *
import sys

def run():
    response = handle_request(pageNum=1)
    json = handle_response(response)

    print(json)
    # build_data(json)

if __name__ == '__main__':
    # set stdout pipe to allow utf-8 characters (required for japanese letters)
    sys.stdout.reconfigure(encoding='utf-8')
    run()