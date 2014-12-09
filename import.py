import json
from pprint import pprint
json_data=open('./richcitationexample.json')
jdata = json.load(json_data)
# pprint (jdata)

# titles = [element["title"] for element in jdata]
#print "url is "+ str(jdata[0]["bibliographic"]["subject"])
text = [group["context"]["text_before"] for group in jdata[0]["citation_groups"]]
textstr=str(text)


target = "million"

print textstr.find(target)

#Use .find(target,beg,end) to specify where to begin and end searching. 

for n in range(len(jdata[0]["citation_groups"])):
    text = [group["context"]["text_before"] for group in jdata[0]["citation_groups"]][n]
    target = "cancer"
    if text.find(target) > 0:
        jdata[0]["citation_groups"][n]['flags'] = 'pos'
        print "I added something to your JSON at citation number : ", n + 1
    else:
        pass

#Writing out as JSON

with open('data.txt', 'w') as outfile:
    json.dump(jdata, outfile)