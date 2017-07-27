#!/bin/bash

for f in ${1}-* ; do python3 countTheWords.py "$f" `cat $f` \& ; done
