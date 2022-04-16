#
# Python script to get localhost JSON data and transform into markdown fields
#

import urllib
import urllib.request
import json

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
    "GAMECHAT": 1,
    "HUDMSG": 2,
    "INDICATORS": 3,
    "MAPOBJECTS": 4,
    "MAPINFO": 5,
    "MISSION": 6,
    "STATE": 7
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

def get_url_and_filename(data_type: int):
    url = ''
    filename = ''
    
    if data_type == wt_data_types['GAMECHAT']:
        url = gamechat_url
        filename = gamechat_file
    elif data_type == wt_data_types['HUDMSG']:
        url = hudmsg_url
        filename = hudmsg_file
    elif data_type == wt_data_types['INDICATORS']:
        url = indicators_url
        filename = indicators_file
    elif data_type == wt_data_types['MAPOBJECTS']:
        url = mapobjects_url
        filename = mapobjects_file
    elif data_type == wt_data_types['MAPINFO']:
        url = mapinfo_url
        filename = mapinfo_file
    elif data_type == wt_data_types['MISSION']:
        url = mission_url
        filename = mission_file
    elif data_type == wt_data_types['STATE']:
        url = state_url
        filename = state_file
    else:
        raise('Invalid parameter')
    
    return [url, filename]

def get_wt_data(data_type: int):

    # Extract data
    url, filename = get_url_and_filename(data_type)
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


