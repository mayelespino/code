from functools import cmp_to_key

def compare(a, b):
    return(len(a)-len(b))


myList = ["123","12","1","a",""]
for element in sorted(myList, key=cmp_to_key(compare)):
    print(element)
