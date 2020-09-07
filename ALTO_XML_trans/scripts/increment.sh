#!/bin/bash
a=1
for i in ../doc/test/*_trans.xml; do
  new=$(printf "%04d.xml" "$a") #04 pad to length of 4
  cp -i -- "$i" "$new"
  let a=a+1 
done