#!/bin/bash

gunzip -k ./data/soc-sign-Slashdot090221.txt.gz
gunzip -k ./data/soc-sign-epinions.txt.gz
gunzip -k ./data/wikiElec.ElecBs3.txt.gz

mv ./data/wikiElec.ElecBs3.txt ./data/wiki.txt

sed 1,4d ./data/soc-sign-epinions.txt > ./data/epinions.txt 
sed 1,4d ./data/soc-sign-Slashdot090221.txt > ./data/slashdot.txt

rm ./data/soc*
rm ./data/wikiElec.ElecBs3.txt.gz
