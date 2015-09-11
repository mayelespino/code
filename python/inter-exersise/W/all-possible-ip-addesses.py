#!/usr/bin/python
"""
Return all possible valid IP addresses given a string containing only digits.
E.g. '255255101124' ['255.255.10.124', '255.255.101.24']

Author: Mayel Espino
"""

def normalizeAndComplete(inPart):
        parts = inPart.split('.')
        octav = []
        for part in parts:
            number = part.rjust(3,'0')
            if int(number) > 255:
                number = 'ERR'
            octav.append(number)
        missingParts = 4 - len(parts)
        for index in xrange(missingParts):
            octav.append("000")
        result = '.'.join(octav)
        return result

def normalize(inPart):
        parts = inPart.split('.')
        octav = []
        for part in parts:
            number = part.rjust(3,'0')
            if int(number) > 255:
                number = 'ERR'
            octav.append(number)
        result =  '.'.join(octav)
        return result


def parseString(inString):
    stringLength = len(inString)

    if stringLength % 5 == 0:
        while stringLength > 0:
            result = []
            result.append(inString[:2])
            result.append(inString[2:])
            result = '.'.join(result)
            print normalizeAndComplete(result)
            result = []
            result.append(inString[:3])
            result.append(inString[3:])
            result = '.'.join(result)
            print normalizeAndComplete(result)
            inString = inString[5:]
            stringLength = len(inString)
            return

    result = '.'.join(inString[i:i+3] for i in range(0, stringLength, 3))
    print normalizeAndComplete(result)

    result = '.'.join(inString[i:i+2] for i in range(0, stringLength, 2))
    print normalizeAndComplete(result)

    if len(inString) == 4:
        result = '.'.join(inString[i:i+1] for i in range(0, stringLength, 1))
        print normalizeAndComplete(result)

def parse255String(inString):
    inString = inString.replace('255','255.')
    parts = inString.split('.')
    finalResult = []
    partialResult = []
    for part in parts:
        stringLength = len(part)
        tmpPart = part
        if part == '255':
            finalResult.append(part)
            continue
        if stringLength % 5 == 0:
            while stringLength > 0:
                result = []
                result.append(part[:2])
                result.append(part[2:])
                result = '.'.join(result)
                partialResult.append(normalize(result))
                result = []
                result.append(part[:3])
                result.append(part[3:])
                result = '.'.join(result)
                partialResult.append(normalize(result))
                part = part[5:]
                stringLength = len(part)

        part = tmpPart
        stringLength = len(part)
        if stringLength % 3 == 0:
            result = '.'.join(inString[i:i+3] for i in range(0, stringLength, 3))
            partialResult.append(normalize(result))

        if stringLength % 2 == 0:
            result = '.'.join(inString[i:i+2] for i in range(0, stringLength, 2))
            partialResult.append(normalize(result))

        if len(inString) == 4:
            result = '.'.join(inString[i:i+1] for i in range(0, stringLength, 1))
            partialResult.append(normalize(result))
    firstHalf = '.'.join(finalResult)
    for pr in partialResult:
        print firstHalf + '.' + pr

    return





def allPossibleIPAddresses(inString):
    print "\n[",inString,"]\n"
    stringLength = len(inString)
    if stringLength < 4 or stringLength > 12:
        print "Invalid lenght"
        return False

    if '255' in inString:
        if inString.find('255') == 0:
            parse255String(inString)
        else:
            print "IP String formated incorrectly."
    else:
        parseString(inString)


allPossibleIPAddresses("25525510124")
allPossibleIPAddresses("10124")
allPossibleIPAddresses("0000")
allPossibleIPAddresses("002550")
allPossibleIPAddresses("001230")
allPossibleIPAddresses("1234")
