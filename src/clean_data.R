# author: Trevor Kwan, Polina Romanchenko, Monique Wong
# date: 2020-01-21
#
"This script cleans raw data by selecting the features that will be used in analysis

Usage: clean_data.R --data_path=<data_path> --file_path_clean=<file_path_clean>

Options:
--data_path=<data_path> path where data can be found
--file_path_train=<file_path_train>  Path (including filename) to save the cleaned csv file.
" -> doc

# to run file: Rscript src/clean_data.R --data_path data/listings.csv.gz --file_path_clean data/data_cleaned.csv

library(tidyverse, quietly = TRUE)
library(docopt, quietly = TRUE)

opt <- docopt(doc)

main <- function(data_path, file_path_clean){
  
  # read in data
  data <- read.csv(data_path)
  
  #Leaving only selected features
  selected <- as.vector(c('id', 'host_id', 'host_response_rate', 'host_is_superhost', 'property_type', 
                          'host_identity_verified', 'neighbourhood_cleansed', 'instant_bookable', 'cancellation_policy', 
                          'accommodates', 'bathrooms', 'bedrooms', 'beds', 'price'))
  
  # change price and host_response_rate to numeric
  data_selected <- data[,selected] %>%
    mutate(price = as.numeric(gsub('[$,]', '', price)),
           host_response_rate = as.numeric(gsub('[%]', '', host_response_rate))/100)
  
  #Export data
  write.csv(data_selected, file = file_path_clean, row.names = FALSE)
}

main(opt$data_path, opt$file_path_clean)

