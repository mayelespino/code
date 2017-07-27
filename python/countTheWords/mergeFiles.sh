#!/bin/bash

rm merged*.json

python3 mergeDictionaries.py m0 big.txt-?.json big.txt-??.json
for (( i=1; i <= 43; i++ ))
do
  python3 mergeDictionaries.py m${i} big.txt-${i}??.json
done
echo "now merging the merge files."
python3 mergeDictionaries.py GrandTotal merged-m*.json > granTotal.txt
echo "done"
