import json
from pprint import pprint
json_data=open('./richcitationexample.json')
jdata = json.load(json_data)
pprint (jdata)
json_data.close()