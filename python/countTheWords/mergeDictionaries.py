"""
Merges the files passed in on the command line.
Takes at least 2 parameters:
- first paramerer is a string to be added to the name of the file which containes the results of the merge.
- second and onward: the name of the file(s) which contain the JSON dictionary to merge.
writes a JSON file with the data from the resulting dicionary.

Author: Mayel Espino.
Jul 22,2017
"""
import sys
import json
import operator

if len(sys.argv) < 2:
    print("usage: megedFileName file1.json file2.json ....")
    sys.exit(1)

dictionary = {}

for file in sys.argv[2:] :
    print("Processing: {}".format(file))
    with open(file, 'r') as jsonFile:
         dict = json.loads(jsonFile.read())
         for key in dict.keys():
             if key not in dictionary:
                dictionary[key] = dict[key]
             else:
                dictionary[key] += dict[key]

mergedFileName = "merged-{}.json".format(sys.argv[1])
print("\nGrand Totals, writting file {}\n".format(mergedFileName))
with open(mergedFileName, 'w') as mergedFile:
    json.dump(dictionary, mergedFile)

#for key in dictionary.keys():
#    print("{}: {}".format(key, dictionary[key]))

print("\nTop 10\n")
sortedList = sorted(dictionary.items(), key=operator.itemgetter(1))

for item in sortedList[:-11:-1]:
    print("{}: {}".format(item[0], item[1]))

# EOF
