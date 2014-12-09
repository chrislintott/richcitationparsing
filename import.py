import json
from pprint import pprint
json_data=open('./richcitationexample.json')
jdata = json.load(json_data)
# pprint (jdata)

# titles = [element["title"] for element in jdata]
#print "url is "+ str(jdata[0]["bibliographic"]["subject"])
text = [group["context"]["text_before"] for group in jdata[0]["citation_groups"]]
textstr=str(text)

#print textstr

target = "million"

print textstr.find(target)

#Use .find(target,beg,end) to specify where to begin and end searching. 
