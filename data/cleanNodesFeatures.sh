#!/bin/bash

# removes unnecessary characters and fixes data for proper CSV format

#sed -i '' 's/\"(/ /' nodes_features_epinions.csv 
#sed -i '' 's/)\"//' nodes_features_epinions.csv

#sed -i '' 's/\"(/ /' nodes_features_slashdot.csv 
#sed -i '' 's/)\"//' nodes_features_slashdot.csv

#sed -i '' 's/\"(/ /' nodes_features_oldwiki.csv 
#sed -i '' 's/)\"//' nodes_features_oldwiki.csv

#sed -i '' 's/\"(/ /' nodes_features_newwiki.csv 
#sed -i '' 's/)\"//' nodes_features_newwiki.csv

#sed -i '' 's/\"(/ /' nodes_features_bitcoin.csv 
#sed -i '' 's/)\"//' nodes_features_bitcoin.csv

# add column names to nodes_features CSV files for R Analysis
#echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_epinions.csv > temp && mv temp nodes_features_epinions.csv
#echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_slashdot.csv > temp && mv temp nodes_features_slashdot.csv
#echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_oldwiki.csv > temp && mv temp nodes_features_oldwiki.csv
#echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_newwiki.csv > temp && mv temp nodes_features_newwiki.csv

#echo 'node_id, total_out, total_in, pos_in, neg_in, pos_out,neg_out' | cat - nodes_features_bitcoin.csv > temp && mv temp nodes_features_bitcoin.csv
