#!/bin/bash

gunzip -k ./data/soc-sign-Slashdot090221.txt.gz
gunzip -k ./data/soc-sign-epinions.txt.gz
gunzip -k ./data/wikiElec.ElecBs3.txt.gz

mv ./data/wikiElec.ElecBs3.txt ./data/wikiElec.ElecBs3.txt

sed 1,4d ./data/soc-sign-epinions.txt > ./data/epinions.txt 
sed 1,4d ./data/soc-sign-Slashdot090221.txt > ./data/slashdot.txt
sed 1,6d ./data/wikiElec.ElecBs3.txt > ./data/wiki.txt

iconv -c -t UTF-8 <./data/wiki.txt> ./data/wiki-utf.txt

rm ./data/soc*
rm ./data/wikiElec.ElecBs3.*

sed -i '' 's/\"(/ /' nodes_features_epinions.csv 
sed -i '' 's/)\"//' nodes_features_epinions.csv

sed -i '' 's/\"(/ /' nodes_features_slashdot.csv 
sed -i '' 's/)\"//' nodes_features_slashdot.csv

echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_epinions.csv > temp && mv temp nodes_features_epinions.csv
echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_slashdot.csv > temp && mv temp nodes_features_slashdot.csv
