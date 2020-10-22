#
# Python script to get localhost JSON data and transform into markdown fields
#

import urllib
import urllib.request
import json

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

            _type = datatype[start+1:end:]
            name = k

            if _type == "str":
                _type = "string"

            markdown = f"""
    - name: **{name}**
        * contains: {_type}
        * description:
    """

            file.write(markdown)
