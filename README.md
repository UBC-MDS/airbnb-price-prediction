# AirBnB: How to price my new Vancouver AirBnB? 
#### DSCI 522 Group_3
#### By: Monique Wong, Polina Romanchenko, Trevor Kwan

## Instructions to reproduce results
- Fork and clone this repo to your local machine
- Load the data by running data.py in your terminal from the root of the project
  - You can try the following command: 
  `python src/data.py --data_url 'http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz' --file_path data`

## Project proposal
### Dataset and source
We have chosen a dataset that outlines Vancouver AirBnB listings. The dataset can be found [here](http://insideairbnb.com/get-the-data.html) under the Vancouver, British Columbia section. A direct link to download the dataset is [here](http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz). Data was compiled November 9 2019. 

### Research question
Our research question is: "At what nightly price should we list our Vancouver AirBnB?" This research question is predictive. Given the dataset, we want to build a machine learning model that can predict an appropriate nightly price for a new AirBnB property. An appropriate price would be one that is competitive compared to existing listings given the property, host and booking specific characteristics. Examples of these characteristics are below:

- Property-related characteristics: property type, the neighborhood, number of people who can be accommodated, number of bathrooms, bedrooms and beds
- Host-related characteristics: host response rate to requests, whether the host is a superhost, whether the host identity has been verified
- Booking-related characteristics: whether the property can be instantly booked, the cancellation policy

To answer this overarching question, we would need to understand the following:
- Which features from the raw dataset would be most predictive of nightly price?
- Which machine learning model at which hyperparameter settings can best predict nightly price?
- Under what range of parameter values (e.g., charactistics of properties) would our model perform reliably?

### Plan for analysis
Our research question requires us to build a model that predicts a continuous variable (price) based on property-, host- and booking-related characteristics which a combination of categorical and continuous variables. Types of models that would be appropriate for this task include KNN regressor, SVM regressor, linear regression, and random forest regressor.

Specifically, the steps we have to take are as follows:
1. **Understand and pre-process the data**: We want to understand our dataset better by understanding the composition of AirBnB listings in our dataset. We will have to identify strategies to address missing values as well as select and/or engineer features that would improve the robustness of the model we will develop. 
2. **Select and test baseline models**: We can begin by trying a wide range of machine learning models such as those mentioned above. We can shortlist those we will do hyperparameter optimization on based on computational time and preliminary scoring (e.g., MSE). We want to select models that are quick to run and have high scores. 
3. **Tune the hyperparameters for a subset of models**: We can optimize the hyperparameters for the shortlisted models from the previous step. 
4. **Select model with the best performance**: The model we choose will be based on accuracy, computational intensiveness and interpretability. 

We will report our analysis results with a table that compares the models we tested based on accuracy, time to fit, time to predict and our assessment of interpretability. We will also report a figure that shows the predicted prices compared to the actual prices on our train and test sets to demonstrate the accuracy of our chosen model in a visual way. 

### Plan for exploratory data analysis
One of the goals of our exploratory data analysis is to evaluate the composition of our data to understand whether any preprocessing is needed before we try fitting our models. This will also help us understand the range of parameters that our model would perform reliably on. To do this, the following are some examples of tables and figures we will create to support this analysis:
- Histograms for all continuous variables to understand the range and skewness of those parameters
- Heatmaps showing the number of listings at various price points by neighborhood and by property type
- Tables showing summary statistics for all variables (from Pandas Profiling) showing the distinct count, percentage of missing values and the range of each variable