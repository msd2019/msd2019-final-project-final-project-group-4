all:
	./01_get_original_data.sh 
	./02_clean_original_data.sh

clean:
	rm -rf ./data/*.txt
