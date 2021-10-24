#!/bin/bash

# arp -a | grep -v incomplete > pilist.tmp
# rm pilist.txt
# grep b8:27:eb:4e:3:86 pilist.tmp| head -1| cut -d' ' -f2 | tr -d "()" >> pilist.txt
# grep b8:27:eb:15:9d:10 pilist.tmp| head -1| cut -d' ' -f2 | tr -d "()" >> pilist.txt
# grep b8:27:eb:76:be:e0 pilist.tmp| head -1| cut -d' ' -f2 | tr -d "()" >> pilist.txt
# grep b8:27:eb:a1:c7:84 pilist.tmp| head -1| cut -d' ' -f2 | tr -d "()" >> pilist.txt
# rm pilist.tmp
# csshX --login pi --host pilist.txt


arp -a | grep -v incomplete > pilist.tmp
rm pilist.txt
for addr in "b8:27:eb:4e:3:86" "b8:27:eb:15:9d:10" "b8:27:eb:76:be:e0" "b8:27:eb:a1:c7:84" 
do 
  grep ${addr} pilist.tmp | head -1| cut -d' ' -f2 | tr -d "()" >> pilist.txt
done
rm pilist.tmp
csshX --login pi --host pilist.txt