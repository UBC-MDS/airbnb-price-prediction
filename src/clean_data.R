# author: Polina Romanchenko, Monique Wong, Trevor Kwan
# date: 2020-01-21
#
"This script cleans raw data by selecting the features and reformating columns, 
output can be used in further Airbnb locations analysis.

Usage: clean_data.R --data_path=<data_path> --file_path_clean=<file_path_clean>

Options:
--data_path=<data_path> path where data can be found
--file_path_clean=<file_path_clean>  Path (including filename) to save the cleaned train and test csv file.
" -> doc

# to run file: Rscript src/clean_data.R --data_path data/listings.csv.gz --file_path_clean data

library(tidyverse, quietly = TRUE)
library(docopt, quietly = TRUE)
library(testthat, quietly = TRUE)
library(checkmate, quietly = TRUE)

opt <- docopt(doc)

main <- function(data_path, file_path_clean){
  
  # Read in data
  data <- read.csv(data_path)
  
  #Leave only selected features
  selected <- as.vector(c('id', 'host_id', 'host_response_rate', 'host_is_superhost', 'property_type', 
                          'host_identity_verified', 'neighbourhood_cleansed', 'instant_bookable', 'cancellation_policy', 
                          'accommodates', 'bathrooms', 'bedrooms', 'beds', 'price'))
  
  #Change price and host_response_rate to numeric
  data_selected <- data[,selected] %>%
    mutate(price = as.numeric(gsub('[$,]', '', price)),
           host_response_rate = as.numeric(gsub('[%]', '', host_response_rate))/100)

  #Split the data to train and test
  set.seed(522)
  
  n = nrow(data_selected)
  trainIndex = sample(1:n, size = round(0.7*n), replace=FALSE)
  train = data_selected[trainIndex,]
  test = data_selected[-trainIndex,]
  
  #Export train and test data files
  write.csv(train, file = paste0(file_path_clean, "/train_data.csv"), row.names = FALSE)
  write.csv(train, file = paste0(file_path_clean, "/test_data.csv"), row.names = FALSE)
}

#Check if the output files were created
test_output <- function(){
  test_that("Error. Output data csv file wasn't created", {
    expect_equal(checkFileExists(x = file_path_clean), TRUE)
  })
  
}

test_output

main(opt[["--data_path"]],opt[["--file_path_clean"]])

