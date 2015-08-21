#!/usr/bin/python

class letterCounter(object):
    def __init__(self,aString):
        self.a_string = aString
    def countEachLetter(self, aChar):
        return self.a_string.count(aChar)

def countLetters(a_word):
    a_word = a_word.lower()
    lc = letterCounter(a_word)
    count = list(map(lc.countEachLetter,a_word))
    return (max(count))

print countLetters("coffee tuffee")
