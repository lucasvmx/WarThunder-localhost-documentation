#
# Python script to get localhost JSON data and transform into markdown fields
#

import urllib
import urllib.request
import json
from sys import exit

# URL constants
base_url = 'http://localhost:8111'
gamechat_url = f'{base_url}/gamechat'
hudmsg_url = f'{base_url}/hudmsg'
indicators_url = f'{base_url}/indicators'
mapobjects_url = f'{base_url}/map_obj.json'
mapinfo_url = f'{base_url}/map_info.json'
mission_url = f'{base_url}/mission.json'
state_url = f'{base_url}/state'

# Filename constants
gamechat_file = 'gamechat.md'
hudmsg_file = 'hudmsg.md'
indicators_file = 'indicators.md'
mapobjects_file = 'mapobjects.md'
mapinfo_file = 'mapinfo.md'
mission_file = 'mission.md'
state_file = 'state.md'

# Type constants
wt_data_types = {
    "GAMECHAT": { "URL": gamechat_url, "FILE": gamechat_file},
    "HUDMSG": { "URL": hudmsg_url, "FILE": hudmsg_file},
    "INDICATORS": { "URL": indicators_url, "FILE": indicators_file },
    "MAPOBJECTS": { "URL": mapobjects_url, "FILE": mapobjects_file },
    "MAPINFO": { "URL": mapinfo_url, "FILE": mapinfo_file },
    "MISSION": { "URL": mission_url, "FILE": mission_file },
    "STATE": { "url": state_url, "FILE": state_file }
}

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

def get_url_and_filename(data_type: str):
    if not data_type in wt_data_types.keys():
        raise("invalid key")

    return [wt_data_types[data_type]["URL"], wt_data_types[data_type]["URL"]]

def get_wt_data(data_type: str):

    # Extract data
    try:
        global url, filename, data
        url, filename = get_url_and_filename(data_type)
    except Exception as e:
        print("could not get url and filename: {}".format(e))
        exit(1)

    data: bytes = b''

    # Do HTTP request
    with urllib.request.urlopen(url) as f:
        data += f.read()

    payload = data.decode('utf-8')
    json_info = json.loads(payload)

    # Write result to markdown
    with open(filename, "w") as file:
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

def get_all_wt_data():

    for key in wt_data_types.keys():
        get_wt_data(key)

