#!/bin/bash

# decompress the gz file
gunzip ./data/soc-sign-bitcoinotc.csv.gz

# remove time column
# only columns remaining are SNAP, TARGET, RATING
cut -d, -f1-3 ./data/soc-sign-bitcoinotc.csv > ./data/bitcoinotc.csv

rm ./data/soc-sign-bitcoinotc.csv
mv ./data/bitcoinotc.csv ./data/soc-sign-bitcoinotc.csv 
