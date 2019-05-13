all:
	./01_get_original_data.sh 
	./02_clean_original_data.sh
	./03_get_new_data.sh
	./04_clean_new_data.sh

clean:
	rm -rf ./data/*.txt
	rm -rf ./data/soc-sign-bitcoinotc.csv
