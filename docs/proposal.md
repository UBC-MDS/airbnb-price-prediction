# AirBnB: How to price my new Vancouver AirBnB? 
## Proposal for machine learning based prediction
#### By: Monique Wong, Polina Romanchenko, Trevor Kwan

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
- Under what range of parameter values (e.g., price, charactistics of properties) would our model perform reliably?

### Plan for exploratory data analysis
One of the goals of our exploratory data analysis is to evaluate the composition of our data to understand whether any preprocessing is needed before we try fitting our models. This will also help us understand the range of parameters that our model would perform reliably on. To do this, the following are some examples of tables and figures we will create to support this analysis:
- A histogram for continuous variables nightly price and number of properties, to understand the range and skewness of those parameters, and depict their relationship with one another
- Heatmaps showing the number of listings at various price points by neighborhood and by property type
- Tables showing summary statistics for all variables (from Pandas Profiling) showing the distinct count, percentage of missing values and the range of each variable

### Plan for analysis
Our research question requires us to build a model that predicts a continuous variable (price) based on property-, host- and booking-related characteristics which a combination of categorical and continuous variables. Types of models that would be appropriate for this task include KNN regressor, SVM regressor, linear regression, and random forest regressor.

Specifically, the steps we have to take are as follows:
1. **Understand and pre-process the data**: We want to understand our dataset better by understanding the composition of AirBnB listings in our dataset. We will have to identify strategies to address missing values as well as select and/or engineer features that would improve the robustness of the model we will develop. 
2. **Select and test baseline models**: We will begin by trying a wide range of machine learning models such as those mentioned above. We selected a wide variety of models based on the expectation of computational time and ability to model complexity. For instance, even though linear regression is a simple model, we wanted to see if it could achieve acceptable accuracy levels due to the high interpretability and low computational complexity. We also wanted to try a random forest regressor to see if a more complex model woudl yield a more accurate model. We will shortlist models that we will do hyperparameter optimization on based on computational time and accuracy levels, measured by MSE. We will select models that are quick to run and have high scores. 
3. **Tune the hyperparameters for a subset of models**: We will optimize the hyperparameters for the shortlisted models from the previous step. We plan to optimize hyperparameters for the shortlisted models using RandomizedSearchCV. The parameters of the estimator will be optimized by cross-validated search over parameter settings. Compared to GridSearchCV, RandomizedSearchCV does not try all out parameter values and selects only random combinations to train. We chose to implement RandomizedSearchCV because it allows for satisfactory hyperparameter selection while minmizing the runtime. After optimizing hyperparamters of these shortlisted models, we compared the optimized models with each other in terms of time and accuracy.
4. **Select model with the best performance**: The model we choose will be based on a combination of accuracy, computational intensiveness and interpretability. And finally, we will compute the residuals of the best performing model, showing the differences between the best model's price predictions and the actual price values. We will plot these residuals on the Y-axis and their corresponding prices on the X-axis, showing the model's accuracy at predicting at each given price in the range 0$ to 800$.

We will report our analysis results with tables that compares the models we tested based on accuracy, computational time (time to fit and predict) as well as our assessment of interpretability. We will also report a residual plot figure that shows the predicted prices compared to the actual prices on our train and test sets to demonstrate the accuracy of our chosen model in a visual way.