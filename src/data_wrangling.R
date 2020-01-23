 # author: Trevor Kwan, Polina Romanchenko, Monique Wong
# date: 2020-01-21
#
"This script wrangles input data into format, ready for machine learning.

Usage: data_wrangling.R --data_path=<data_path> --file_path_train=<file_path_train> --file_path_test=<file_path_test> 

Options:
--data_path=<data_path> path where data can be found
--file_path_train=<file_path_train>  Path (including filename) to save the train set csv file.
--file_path_test=<file_path_test>  Path (including filename) to save the test set csv file.
" -> doc

# to run file: Rscript src/data_wrangling.R --data_path data/listings.csv.gz --file_path_train data/training.csv --file_path_test data/test.csv

library(tidyverse, quietly = TRUE)
library(docopt, quietly = TRUE)

opt <- docopt(doc)

main <- function(data_path, file_path_train, file_path_test){
  
  # read in data
  data <- read.csv(data_path)
  
  #Leaving only selected features
  selected <- as.vector(c('id', 'host_id', 'host_response_rate', 'host_is_superhost', 'property_type', 
                          'host_identity_verified', 'neighbourhood_cleansed', 'instant_bookable', 'cancellation_policy', 
                          'accommodates', 'bathrooms', 'bedrooms', 'beds', 'price'))
  
  data_selected <- data[,selected]
  
  #Fixing price column formating
  
  data_selected <- data_selected %>%
    mutate(price = str_replace(price, '$', ''), price = str_replace(price, ',', ''))
  
  data_selected$price <- as.numeric(data_selected$price)
  
  #Changing format of host response rate column
  data_selected <- data_selected %>%
    mutate(host_response_rate = str_replace(host_response_rate, '%', ''))
  
  
  data_selected$host_response_rate <- as.numeric(data_selected$host_response_rate)
  data_selected$host_response_rate <- data_selected$host_response_rate/100.0
  
  #Split the data
  
  set.seed(522)
  
  n = nrow(data_selected)
  trainIndex = sample(1:n, size = round(0.7*n), replace=FALSE)
  train = data_selected[trainIndex ,]
  test = data_selected[-trainIndex ,]
  
  #Export data
  write.csv(train, file = file_path_train, row.names = FALSE)
  write.csv(test, file = file_path_test, row.names = FALSE)
}

main(opt$data_path, opt$file_path_train, opt$file_path_test)

