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
random forest regressor). This current model, however, tends to
consistently overestimate the price of AirBnB’s below $200/night and
underestimate the price of AirBnB’s above $300/night. Further work
should involve feature engineering to model interactions between
features (e.g., neighborhood and property type) as well as fitting more
complex linear models (e.g., that better model pricing behaviour above
$300/night).

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
model: - **Property-related characteristics**: property type, the
neighborhood, number of people who can be accommodated, number of
bathrooms, bedrooms and beds. - **Host-related characteristics**: host
response rate to requests, whether the host is a superhost, whether the
host identity has been verified. - **Booking-related characteristics**:
whether the property can be instantly booked, the cancellation policy To
answer this overarching question, we would need to understand the
following:

## Methods

### Dataset and Source

We have chosen a dataset that outlines Vancouver AirBnB listings. The
dataset can be found [here](http://insideairbnb.com/get-the-data.html)
under the Vancouver, British Columbia section. A direct link to download
the dataset is
[here](http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz).
Data were compiled November 9 2019.

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

<img src="../output/number_of_properties_by_price.png" title="Figure 1: Number of properties by nightly price" alt="Figure 1: Number of properties by nightly price" width="60%" height="60%" />

We can see that majority of properties are priced between $50 to $200
per night. There is a long right tail to this distribution reflecting
fewer properties listed at high prices. As we create a model that
suggests / predicts a price of a new AirBnB property, we have to be
conscious of the fact that the training set has had more data to learn
from prices towards the centre of the
distribution.

#### Understanding Price by Neighborhood

<img src="../output/neighborhoods.png" title="Figure 2: Number of properties by price and neighborhood" alt="Figure 2: Number of properties by price and neighborhood" width="60%" height="60%" />
Some neighborhoods do not have any properties listed above a certain
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
Other than houses, condos and apartments, other categories have very
sparse data, especially across price points. In particular, Aparthotel,
Bed and breakfast, Boat, Boutique hotel, Cabin, Cottage, Hotel,
Timeshare and Tinyhouse are problematic. The model we develop would be
able to best predict on unseen house, apartment and condo properties
since there is the most data to learn from across price points.

### Building our model

The first step in identifying the most appropriate model was to evaluate
four different machine learning models for accuracy and computational
complexity. Mean squared error (MSE) was used as the accuracy metric
since we are using regression techniques.

    ## # A tibble: 4 x 5
    ##   X1    `Train MSE` `Validation MSE` `Time in second… row_names$`"Lin…
    ##   <chr>       <dbl>            <dbl>            <dbl> <chr>           
    ## 1 lr         69771.           73208.           0.0245 Linear Regressi…
    ## 2 kNN        56795.           99535.           0.660  Linear Regressi…
    ## 3 svr        77902.           79010.           1.41   Linear Regressi…
    ## 4 rfr        17023.          110384.           6.32   Linear Regressi…
    ## # … with 3 more variables: $`"kNN Regressor"` <chr>, $`"Support Vector
    ## #   Machine Regression"` <chr>, $`"Random Forest Regressor"` <chr>

| X1  | Train MSE | Validation MSE | Time in seconds |
| :-- | --------: | -------------: | --------------: |
| lr  |  69770.76 |       73207.93 |          0.0245 |
| kNN |  56795.11 |       99535.03 |          0.6603 |
| svr |  77902.28 |       79010.28 |          1.4141 |
| rfr |  17022.82 |      110384.43 |          6.3249 |

Table 1: Baseline results for four
models

| X1               |    Train MSE |    Validation MSE |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Time in seconds |
| :--------------- | -----------: | ----------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| lr               |    69770.758 |          73207.93 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.0233 |
| kNN\_optimized   |     4889.878 |          65284.75 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.6332 |
| svr\_optimized   |    84757.310 |          85335.84 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   1.3071 |
| Without hyperpar | amter optimi | zation, we shortl | isted the models: linear regression (lr), KNeighborsRegressor (kNN), and support vector regression (SVR), because they performed better in terms of accuracy and time. After hyperparameter optimization, we compared the optimized time and accuracy of SVR and kNN with linear regression, and decided that linear regression overall was the better machine learning model to predict price given our data performing well on the 3 categories: accuracy, time, and interpretability. |

Table 2 shows the optimized training and validation mean squared errors
and training and validation learning time.

![alt tag](../output/residual_plot.png)

The above plot shows the residuals of the best model plotted against the
true prices. The residuals indicate the difference in predicted value of
the linear regression model and the actual price value. In this case, we
can see how well our linear regression model predicted prices at any
given price within the range of 0 to 800.

To further improve our solution to the question “At what nightly price
should we list our Vancouver AirBnB?”, there are several remedies for
future researchers whom choose to take on this project. First, we would
suggest consulting domain experts in the field of Airbnb when deciding
which features to select for model training usage. Our preliminary
decision to select features was based solely off of our common
collective knowledge of hostel prices. Second, we would suggest
optimizing more hyperparamters within the parameter grid. This could
allow for more accurate and time efficient models due to their optimized
hyperparameters. And lastly, an ideal answer to our research question
would include the ideal range of parameter values for each
characteristic/feature in which our model performs reliably, but due to
time constraints we were not able to obtain this.

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
