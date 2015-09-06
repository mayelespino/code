def openFileAndLocateEnd(inPath, inNumberOfLines):
    file = open(inPath,'r')

    offset = 1
    while index in xrange(inNumberOfLines):
            aLine =findALIne(file,offset)
            print aLine
            offset = len(aLine)+1


def findALine(inFile, offset):
    tempLine = []
    aChar = file.seek(offset,2)
    while aChar is not '\n':
        file.seek(offset,2)
        aChar = file.read(1)
        tempLine.append(aChar)
        offset +=1
    return tempLine.reverse()


openFileAndLocateEnd('/path/to/file.log',10)
