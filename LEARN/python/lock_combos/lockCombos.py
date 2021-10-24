#from PyDictionary import PyDictionary

r1=['L','N','B','D','M','J','P','R','S','T']
r2=['L','H','A','E','I','O','U','Y','R','T']
r3=['L','N','A','C','D','E','O','R','S','T']
r4=['L','N','E','D','H','K','Y','R','S','T']

#dictionary=PyDictionary()

with open('wordsEn.txt', 'r') as f:
    words = f.readlines()

dict_words = []
for w in words:
    if len(w) == 5:
        w=w.strip().upper()
        dict_words.append(w)

for l1 in r1:
    for l2 in r2:
        for l3 in r3:
            for l4 in r4:
                word = "{}{}{}{}".format(l1,l2,l3,l4)
                if word in dict_words:
                    print(word)


