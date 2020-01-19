Our dataset is coming from the URL: http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz. The name of the article containing the dataset is "Inside Airbnb. Adding data to the debate." and our dataset is under the Vancouver, British Columbia, Canada section, date compiled being November 9th, 2019 with the file name being "listings.csv.gz".

The main research question that we will attempt to answer is: "Given a new airbnb with certain features, what should we set the price of it to be?" This research question is predictive.

Sub-questions we would need to address are listed below.

Which features in the raw dataset would be useful in predicting price?
Which machine learning model would be best to predict price? (We want to minimize variance and bias.)
Which hyperparameters should we be optimizing in the machine learning model we choose to use?

We will analyze the data using several methods that all involve using categorical/continous features to predict a continuous variable (price), such as KNN, SVM, linear regression, or random forest regression. In particular, we are aware that linear regressors are easier to interpret.

One exploratory data analysis table we will create is a table for total count of Airbnb listings per price category in a neighbourhood. 
Another is a table containing all the features we are interested in predicting the continuous variable price. 

One exploratory data analysis figure we will create is a figure showing the total number of Airbnb's across neighbourhoods in Vancouver per price category. Another is a heatmap, which is a correlation matrix showing the relationship between feature varaibles and individual feature variables with the predictor price.

We will share the results of our analysis using the suggested tables and figures above. 