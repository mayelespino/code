#
# I got some of these examples: https://youtu.be/9N6a-VLBa2I
# I got the api from: https://jsonplaceholder.typicode.com

import json
from urllib2 import urlopen

json_string = '{ "name":"John", "age":30, "city":"New York"}'

json_string = ''' { "people" :
    [
        {
            "first_name": "john",
            "last_name": "smith"
        },
        {
            "first_name" : "jane",
            "last_name" : "doe"
        }
    ]
}
'''

jsonDict = json.loads(json_string)


for person in jsonDict['people']:
    print(person)
    print(person['first_name'])

jsonDict['people'].append('{"first_name" : "pete", "last_name": "pan"}')

indentedJson = json.dumps(jsonDict, indent=2)
print(indentedJson)


with open('wwj.json', 'w') as f:
    f.write(indentedJson)

with open('wwj2.json', 'w') as f:
    json.dump(jsonDict, f, indent=4)


response = urlopen("https://jsonplaceholder.typicode.com/todos/1")
data = response.read()

newDict = json.dumps(data)
print(newDict)
print(json.dumps(newDict, indent=4))
