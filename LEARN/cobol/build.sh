#!/bin/bash
if [ ! -z "$1" ]; then
cobc -free -x -o $1 $1.cob
fi
