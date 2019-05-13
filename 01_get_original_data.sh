#!/bin/bash

# All data downloaded from these scripts are placed in the ./data directory 
# Data is downloaded in a compressed format
# 02_clean_original_data.sh will decompress the data and clean it for R analysis

# Downloads Slashdot data referenced by the paper
curl http://snap.stanford.edu/data/soc-sign-Slashdot090221.txt.gz --output ./data/soc-sign-Slashdot090221.txt.gz 

# Downloads Epinions data referenced by the paper
curl http://snap.stanford.edu/data/soc-sign-epinions.txt.gz --output ./data/soc-sign-epinions.txt.gz 

# Downloads wikipedia data referenced by the paper
curl http://snap.stanford.edu/data/wikiElec.ElecBs3.txt.gz --output ./data/wikiElec.ElecBs3.txt.gz
