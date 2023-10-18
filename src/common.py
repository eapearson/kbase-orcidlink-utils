import json
import sys

import requests

line_count = 0

def print_line(line):
    global line_count
    line_count += 1
    print(f'{line_count:02}: {line}')

def info(msg):
    print_line(f' 🔵 {msg}')

def error(msg):
    print_line(f' ❗ {msg}')

def success(msg):
    print_line(f' ✅ {msg}')

def json_rpc(url, method, params=None, auth=None):
    rpc_request = {
        "jsonrpc": "2.0",
        "id": "123",
        "method": method
    }

    if params is not None:
        rpc_request['params'] = params

    header = {}

    if auth is not None:
        header = {
            "authorization": auth
        }

    try:
        response = requests.post(url, data=json.dumps(rpc_request), headers=header)
    except Exception as err:
        error('JSON-RPC request error')
        error(str(err))
        sys.exit(1)

    rpc_response = json.loads(response.text)
    if 'error' in rpc_response:
        message = rpc_response['error']['message']
        code = rpc_response['error']['code']
        raise Exception(f"{code}: {message}")

    return rpc_response['result']