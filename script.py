#
# Python script to get localhost JSON data and transform into markdown fields
#

import urllib
import urllib.request
import json

def get_correct_typename(typename: str):
    v = {
        "str": "string",
        "bool": "boolean",
        "int": "integer",
        "float": "decimal"
    }

    for k in v.keys():
        if k == typename:
            return v[f'{k}']
    
    return typename

def get_state_field():
    data: bytes = b''

    with urllib.request.urlopen('http://localhost:8111/state') as f:
        data += f.read()

    payload = data.decode('utf-8')
    json_info = json.loads(payload)

    with open("state.md", "w") as file:
        for k in json_info.keys():
            datatype = str(type(json_info[f'{k}']))
            start = datatype.find('\'')
            end = datatype.find('\'', start + 1)
            if end == -1:
                print('error')
                continue

            _type = get_correct_typename(datatype[start+1:end:])
            name = k

            markdown = f"""
    - name: **{name}**
        * contains: {_type}
        * description:
    """

            file.write(markdown)
 
def get_indicators_field():
    data: bytes = b''

    with urllib.request.urlopen('http://localhost:8111/indicators') as f:
        data += f.read()

    payload = data.decode('utf-8')
    json_info = json.loads(payload)

    with open("file.md", "w") as file:
        for k in json_info.keys():
            datatype = str(type(json_info[f'{k}']))
            start = datatype.find('\'')
            end = datatype.find('\'', start + 1)
            if end == -1:
                print('error')
                continue

            _type = get_correct_typename(datatype[start+1:end:])
            name = k

            markdown = f"""
    - name: **{name}**
        * contains: {_type}
        * description:
    """

            file.write(markdown)

get_state_field()
