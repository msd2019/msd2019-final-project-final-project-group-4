# target to make the file report
all: 05_final_report.html

scripts:
	./01_get_original_data.sh 
	./02_clean_original_data.sh
	./03_get_new_data.sh
	./04_clean_new_data.sh

clean:
	rm -rf ./data/*.txt
	rm -rf ./data/soc-sign-bitcoinotc.csv

05_final_report.html: 
	Rscript -e "rmarkdown::render('05_final_report.Rmd')"
