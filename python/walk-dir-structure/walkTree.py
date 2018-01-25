#!/usr/local/bin/python3
import os

for currentDir, subDirs, files in os.walk('.'):
    print('\nCurrent directory: %s' % currentDir)
    print('files:')
    for file in files:
        print('\t%s' % file)
    print('subdirectories:')
    for subDir in subDirs:
        print('\t%s' % subDir)
    print('----------')
