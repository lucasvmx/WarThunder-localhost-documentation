#
# Python script to get localhost JSON data and transform into markdown fields
#

import json
import os
import os.path
import urllib
import urllib.request
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
	"STATE": { "URL": state_url, "FILE": state_file }
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

	return [wt_data_types[data_type]["URL"], wt_data_types[data_type]["FILE"]]

def get_wt_data(data_type: str):

	data: bytes = b''

	output_folder = "OUTPUT"

	try:
		os.mkdir(output_folder)
	except:
		pass

	# Extract data
	try:
		global url, filename
		url, filename = get_url_and_filename(data_type)
	except Exception as e:
		print("could not get url and filename: {}".format(e))
		exit(1)

	data: bytes = b''

	# Do HTTP request
	try:
		with urllib.request.urlopen(url) as f:
			print("requesting {}".format(url))
			data += f.read()
	except:
		print("failed to get resource: {}".format(url))
		return

	payload = data.decode('utf-8')
	json_info = list[str](json.loads(payload))

	# Write result to markdown
	dest_file = os.path.join(output_folder, filename)

	with open(dest_file, "w") as file:
		index = 0
		for k in json_info:
			datatype = str(type(json_info[index]))
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
			index+=1

def get_all_wt_data():

	for key in wt_data_types.keys():
		get_wt_data(key)


if __name__ == "__main__":
	get_all_wt_data()
