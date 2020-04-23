import json
from pprint import pprint as pp

with open('test.json','r') as fi:
    #paul = json.loads('{"Name": "Paul"}')
    text = fi.read()
    paul = json.loads(text)

pp(paul)
print(paul["Name"])
print(paul["Age"])

paul["Age"] = 48
#pp(paul)
#print(json.dumps(paul))

with open('test.json','w') as fi:
    fi.write(json.dumps(paul))

