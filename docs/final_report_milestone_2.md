Milestone 2 Final Report
================

## Summary

In this project, we build a predictive model to help new AirBnB hosts
set the nightly price of their Vancouver AirBnB. Our predictive model
predicts the market price of an AirBnb given the property, host and
booking characteristics which we believe is given the the optimal price
for both the host and AirBnB guests.

At this stage, we have trained a variety of machine learning models
based on property-, host- and book-related characteristics of existing
Vancouver AirBnBs. Examples of characteristics include property type,
neighborhood, the number of people who can be accommodated, the ability
to instant book the property, the booking’s cancellation policy and the
responsiveness of the host.

Surprisingly, our linear regression predictor exceeded the performance
of more complex machine learning models that were evaluated (e.g.,
random forest regressor). This model, however, tends to consistently
overestimate the price of AirBnB’s below $200/night and underestimate
the price of AirBnB’s above $300/night. Further work should involve
feature engineering to model interactions between features (e.g.,
neighborhood and property type) as well as fitting more complex linear
models (e.g., that better model pricing behaviour above $300/night).

## Introduction

Becoming an AirBnB host is becoming a popular way to allow property
owners to run a small business that can supplement their income and help
with mortgage payments in an expensive housing market like Vancouver.
One of the key decisions that an AirBnB host has to make is setting the
price for the nightly rate of their property.

The AirBnB booking process is like any effective marketplace. Hosts need
to set a competitive and fair rate for the use of their property. Guests
will compare the quality of the property and the overall booking
experience as well as the price against alternatives. A tool that
predicts the market price of a property that a host intends to list will
inform a host’s pricing decision.

This project intends to build a predictive machine learning model to
help new AirBnB hosts set the nightly price of their Vancouver AirBnB.
The following characteristics will be used in the machine learning
model:

  - **Property-related characteristics**: property type, the
    neighborhood, number of people who can be accommodated, number of
    bathrooms, bedrooms and beds.
  - **Host-related characteristics**: host response rate to requests,
    whether the host is a superhost, whether the host identity has been
    verified.
  - **Booking-related characteristics**: whether the property can be
    instantly booked, the cancellation policy To answer this overarching
    question, we would need to understand the following:

## Methods

### Dataset and Source

We have chosen a dataset that outlines Vancouver AirBnB listings. The
dataset can be found [here](http://insideairbnb.com/get-the-data.html)
under the Vancouver, British Columbia section. A direct link to download
the dataset is
[here](http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz).
This data was compiled November 9 2019.

There are 6181 AirBnB listings in this dataset.

### Analysis

Our research question requires us to build a model that predicts a
continuous variable (price) based on property-, host- and
booking-related characteristics which a combination of categorical and
continuous variables. Types of models that would be appropriate for this
task include linear regression, KNN regressor, SVM regressor, and random
forest regressor.

In this project, we want to identify a model that is, relatively
speaking, more accurate, less computationally intensive and easily
interpretable. Accuracy, especially for a range of property types, is
important so that hosts can rely on this model. Less computationally
intensive models will also be favoured so that the model can be updated
frequently based on changing AirBnB data. Being able to interpret the
model parameters would be helpful since it would be helpful for hosts to
be able to understand how the market price of their property would
change if they changed features that were within their control (e.g.,
relax the cancellation policy).

Our methodology evaluates the models suggested above for accuracy,
computational intensity and interpretability. We will train 4 models
(linear regression, KNN regressor, SVM regressor, and random forest
regressor) to shortlist 2-3 that we will tune hyperparameters for. The
tuned models will be compared against each other before deciding on one
final model.

The R and Python programming languages (R Core Team 2019; Van Rossum and
Drake 2009) and the following R and Python packages were used to perform
the analysis: pandas (McKinney and others 2010), numpy (Oliphant 2006),
requests (Chandra and Varanasi 2015), os (Van Rossum and Drake 2009),
docopt (de Jonge 2018), tidyverse (Wickham 2017), testthat (Wickham
2011), checkmate (Lang 2017), altair (Lyttle 2018), and sklearn
(Pedregosa et al. 2011).

## Results and Discussion

### Exploring our data

To begin our analysis, we wanted to understand a) the range and
distribution of prices represented in our dataset and b) potential
issues with sparse data for neighborhood and property type categorical
variables.

#### Distribution of AirBnB nightly prices in our dataset

<img src="../output/neighborhoods.png" title="Figure 1: Number of properties by nightly price and by neighborhood" alt="Figure 1: Number of properties by nightly price and by neighborhood" width="60%" height="60%" />

Figure 1: Number of properties by nightly price (CAD) and by
neighborhood

We can see that majority of properties are priced between $50 to $200
per night. There is a long right tail to this distribution reflecting
fewer properties listed at high prices. As we create a model that
suggests / predicts a price of a new AirBnB property, we have to be
conscious of the fact that the training set has had more data to learn
from prices towards the centre of the distribution.

When we examine the distribution of price by neighborhood, we see that
some neighborhoods do not have any properties listed above a certain
price point. For instance, Strathcona and Killarney have no properties
listed above $350/night. Most neighborhoods do not have any properties
listed above $600/night. This lack of training examples for properties
of certain prices in certain neighborhoods has implications on our
model’s ability to predict properties in these “edge cases”. Downtown
and Kitsilano have some of the highest priced properties, with listings
almost consistently up to $
1000/night.

#### Understanding Price by Property Type

<img src="../output/price_by_property_type.png" title="Figure 3: Number of properties by price and property type" alt="Figure 3: Number of properties by price and property type" width="60%" height="60%" />

Figure 3: Number of properties by price (CAD) and property type

Other than houses, condos and apartments, other categories have very
sparse data, especially across price points. In particular, Aparthotel,
Bed and breakfast, Boat, Boutique hotel, Cabin, Cottage, Hotel,
Timeshare and Tinyhouse are problematic. The model we develop would be
able to best predict on unseen house, apartment and condo properties
since there is the most data to learn from across price points.

#### Preprocessing Our Data

Prior to fitting various machine learning models, we preprocessed our
data to standardize scaling to improve the performance of models that
rely on distance such as the KNN regressor. We also engineered the
neighborhood feature, grouping neighborhoods into “Downtown”, “Vancouver
West” and “Vancouver East” to reduce class imbalance and sparsity of
data for various neighborhoods. Missing numeric values were replaced
with median values for the feature; missing categorical values were
denoted as “missing”.

### Building our model

The first step in identifying the most appropriate model was to evaluate
four different machine learning models for accuracy and computational
complexity. Mean squared error (MSE) was used as the accuracy metric
since we are using regression
techniques.

| Models                            | Train MSE | Validation MSE | Computation time (s) |
| :-------------------------------- | --------: | -------------: | -------------------: |
| Linear Regression                 |    70,542 |         72,763 |                  0.0 |
| kNN Regressor                     |    62,294 |         85,796 |                  0.6 |
| Support Vector Machine Regression |    77,553 |         78,726 |                  1.5 |
| Random Forest Regressor           |    19,928 |        125,435 |                  5.2 |

Table 1: Baseline performance for four models

The linear regressor and support vector machine (SVM) regressor
performed the best in terms of accuracy on the validation set. While the
kNN regressor performed poorly, it has clearly overfit since
hyperparameters had not been tuned yet. We will shortlist these three
models for further analysis. As we can see, the random forest regressor
was not only computationally intensive, but also performed poorly.
Combined with the poor interpretability of random forest models, we have
removed this model from our consideration set.

We tuned `n_neighbors` and `gamma` hyperparameters for our kNN and SVM
regressors respectively. The following table shows our findings along
with the results for our linear
regressor.

| Models                  | Train MSE | Validation MSE | Computation time (s) |
| :---------------------- | --------: | -------------: | -------------------: |
| Linear Regression       |    70,542 |         72,763 |                  0.0 |
| Optimized kNN           |    60,158 |         91,772 |                  0.6 |
| Optimized SVM Regressor |    84,757 |         85,335 |                  1.3 |

Table 2: Performance of optimized models

To our surprise, our linear regressor performed the best on both
accuracy and computational complexity. Linear regression is also the
most interpretable. As a result, our linear regressor was selected as
the best model at this stage of our analysis.

### Evaluating our model: performance and limitations

To understand how our model performs on a variety of price ranges, we
created the following residual plot showing the difference in predicted
value compared to the actual price against actual
prices.

<img src="../output/residual_plot.png" title="Figure 4: Residuals by true price for linear regression model" alt="Figure 4: Residuals by true price for linear regression model" width="60%" height="60%" />

As we can see, our model tends to overestimate the price of AirBnB’s
below $200/night and underestimate the price of AirBnB’s above
$300/night. Since we fitted a linear model, this could indicate a
non-linear relationship between our features and price. Right now, our
model performs the best for properties that should be priced between
$200 and $300/night, a limitation that should be taken account if a user
were to use this model.

### Future directions

There are several ways to continue to improve our model performance that
we list below:

1)  **Further feature engineering:** We selected a subset of features
    from a large dataset to train our model on based on our knowledge of
    AirBnB. Interviewing AirBnB hosts and frequent guests could reveal
    other important features that impact pricing. For instance,
    interactions between features (e.g., a property that accommodates
    many people in downtown Vancouver would be valued compared to one in
    the suburbs) could significantly improve the performance of the
    model. Engineering our features to group property types that behave
    similarly but have few data points could also improve the
    performance of edge cases and imbalanced classes.

2)  **Fitting more complex linear models:** Our results suggest a
    non-linear relationship between price and our features. We can
    explore improving model performance by assuming different model
    distributions that better reflect the long tail of higher priced
    properties.

Before our model is deployed for use, we also suggest pressure testing
our model against a range of input values to identify the types of
properties and bookings for which our model can make reliable
predictions.

# References

<div id="refs" class="references">

<div id="ref-chandra2015python">

Chandra, Rakesh Vidya, and Bala Subrahmanyam Varanasi. 2015. *Python
Requests Essentials*. Packt Publishing Ltd.

</div>

<div id="ref-docopt">

de Jonge, Edwin. 2018. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-checkmate">

Lang, Michel. 2017. “checkmate: Fast Argument Checks for Defensive R
Programming.” *The R Journal* 9 (1): 437–45.
<https://journal.r-project.org/archive/2017/RJ-2017-028/index.html>.

</div>

<div id="ref-lyttle2018introducing">

Lyttle, Ian. 2018. “Vegawidget: Introducing Altair.”
<https://vegawidget.rbind.io/posts/2018-05-20-introducing-altair/>.

</div>

<div id="ref-mckinney2010data">

McKinney, Wes, and others. 2010. “Data Structures for Statistical
Computing in Python.” In *Proceedings of the 9th Python in Science
Conference*, 445:51–56. Austin, TX.

</div>

<div id="ref-oliphant2006guide">

Oliphant, Travis E. 2006. *A Guide to Numpy*. Vol. 1. Trelgol Publishing
USA.

</div>

<div id="ref-scikit-learn">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-R">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-Python">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-testthat">

Wickham, Hadley. 2011. “Testthat: Get Started with Testing.” *The R
Journal* 3: 5–10.
<https://journal.r-project.org/archive/2011-1/RJournal_2011-1_Wickham.pdf>.

</div>

<div id="ref-tidyverse">

———. 2017. *Tidyverse: Easily Install and Load the ’Tidyverse’*.
<https://CRAN.R-project.org/package=tidyverse>.

</div>

</div>
