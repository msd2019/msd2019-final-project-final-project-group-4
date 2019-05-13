#!/bin/bash

# All data processed in this script are placed in the ./data directory 
# Only processes old data

# decompress the data 
gunzip ./data/soc-sign-Slashdot090221.txt.gz
gunzip ./data/soc-sign-epinions.txt.gz
gunzip ./data/wikiElec.ElecBs3.txt.gz

#mv ./data/wikiElec.ElecBs3.txt ./data/wikiElec.ElecBs3.txt

# Deletes unnecessary lines in the beginning of each file
sed 1,4d ./data/soc-sign-epinions.txt > ./data/epinions.txt 
sed 1,4d ./data/soc-sign-Slashdot090221.txt > ./data/slashdot.txt
sed 1,6d ./data/wikiElec.ElecBs3.txt > ./data/wiki.txt

# removes non UTF-8 characters from wikipedia data
# does not affect overall results, but necessary for 
# file reading by python scripts
iconv -c -t UTF-8 <./data/wiki.txt> ./data/wiki-utf.txt

rm ./data/soc*
rm ./data/wikiElec.ElecBs3.*
