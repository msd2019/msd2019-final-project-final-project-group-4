# Final Project for Modeling Social Data, 2019

SAMEER JAIN (sj2736) 
BAILEY PIERSON (bp2471) 
TANMAY CHOPRA (tc2897)

This repository has code to attempt to replicate and extend the results in [Predicting Positive and Negative Links in Online Social Networks](www.arxiv.org/abs/1003.2429) by Jure Leskovec, Daniel Huttenlocher, and Jone Kleinberg, WWW 2010: ACM WWW International conference on World Wide Web, 2010.

A complete report of our results is in `05_final_report.pdf`, which can be generated by cloning this repository and running `make` to execute the commands in the `Makefile` file. All data are in `data/` and any original source code provided by the authors is in `authors_original_code/`.

The repository is structured as follows:

1. `01_get_original_data.sh` gets the original data used by the authors and places a copy in `data/`
2. `02_clean_original_data.sh` cleans this data and saves the relevant dataframe(s) in `data/original_data_clean.Rdata`
3. `03_get_new_data.sh` gets new data used to extend the original results of this paper and places a copy in `data/`
4. `04_clean_new_data.sh` cleans this data and saves the relevant dataframe(s) in `data/new_data_clean.Rdata`
5. `05_final_report.Rmd` analysis both the original and new data to replicate and extend the results of the original paper, and produces the final report `05_final_report.pdf`

----

Notes:

The exact structure of the repository may vary from group to group. For instance, you might have a different number of files, some might be `.R` scripts instead of `.sh` scripts, etc., but follow the basic template and edit this README accordingly so that others can run your code and reproduce _your_ results with one command that executes your entire analysis from start to a finished report. You don't necessarily have to use make for your "run all" command, but it can be quite helpful, especially if the process of getting or cleaning the data takes much longer than running the final analysis and generating the report. Whatever the "run all" command is, it should be clearly noted so that others know what it is and how to execute it. If the data files you are using are small enough, add a copy directly to your repository. If a file is too large to add to the repository, include a URL that points to a copy of the data so that others can access it. 

(Delete these notes in your copy of the repository.)

Downloading new Wikipedia data and generating the features for the machine learning model requires the following package installations: 

Python NetworkX
Python Pandas
Python collections
Python bs4 
Python Requests
Python lxml

Each of these packages can be installed via pip. We utilized Python 3 for new data collection and computation of triad features for the machine learning model. 
