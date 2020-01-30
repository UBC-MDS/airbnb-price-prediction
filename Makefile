# Driver script
# Monique Wong, Polina Romanchenko, Trevor Kwan, Jan 2020
#
# This driver script completes exploratory data analysis by creating 4 figures
# showing the relationship between airbnb prices and features, and completes 
# machine learning analysis by creating 2 tables comparing performance between 
# several models. This script takes no arguments.
#

# usage: make all

# run all analysis
all: docs/final_report_milestone_2.md 

# download data from URL
data/listings.csv.gz: src/download_data.py
	python src/download_data.py --data_url 'http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz' --file_path data

# clean data into train csv and test csv
data/train_data.csv data/test_data.csv: src/clean_data.R data/listings.csv.gz
	Rscript src/clean_data.R --data_path data/listings.csv.gz --file_path_clean data

# create figures
output/neighborhoods.png: src/explore_data.py data/train_data.csv
	python src/explore_data.py --data_path data/train_data.csv --file_path output

output/number_of_properties_by_price.png: src/explore_data.py data/train_data.csv
	python src/explore_data.py --data_path data/train_data.csv --file_path output

output/price_by_property_type.png: src/explore_data.py data/train_data.csv
	python src/explore_data.py --data_path data/train_data.csv --file_path output
	
output/residual_plot.png: src/explore_data.py data/train_data.csv
	python src/explore_data.py --data_path data/train_data.csv --file_path output

# create analysis tables
output/baseline_results.csv: src/analyze_data.py data/train_data.csv data/test_data.csv
	python src/analyze_data.py --training_file_path data/train_data.csv --test_file_path data/test_data.csv --output_file_path output

output/optimized_results.csv: src/analyze_data.py data/train_data.csv data/test_data.csv
	python src/analyze_data.py --training_file_path data/train_data.csv --test_file_path data/test_data.csv --output_file_path output
	
# render report
docs/final_report_milestone_2.md: docs/final_report_milestone_2.Rmd output/neighborhoods.png output/number_of_properties_by_price.png output/price_by_property_type.png output/residual_plot.png output/baseline_results.csv output/optimized_results.csv
	Rscript -e "rmarkdown::render('docs/final_report_milestone_2.Rmd')"

# clean up intermediate and results files
clean: 
	rm -f data/listings.csv.gz
	rm -f data/*.csv
	rm -f output/*.png
	rm -f output/*.csv
	rm -f docs/final_report_milestone_2.md 