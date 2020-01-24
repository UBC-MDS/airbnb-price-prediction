Milestone 2 Final Report
================

  - [Introduction](#introduction)
  - [Dataset and Source](#dataset-and-source)
  - [Findings and Results](#findings-and-results)
  - [Interpretation of Results](#interpretation-of-results)
  - [Critique of the Analysis](#critique-of-the-analysis)
  - [Statement of Future Directions](#statement-of-future-directions)
  - [References](#references)

## Introduction

Our research question is: “At what nightly price should we list our
Vancouver AirBnB?”

This research question is predictive. Given the dataset, we want to
build a machine learning model that can predict an appropriate nightly
price for a new AirBnB property. An appropriate price would be one that
is competitive compared to existing listings given the property, host
and booking specific characteristics.

Examples of these characteristics are below:

Property-related characteristics: property type, the neighborhood,
number of people who can be accommodated, number of bathrooms, bedrooms
and beds.

Host-related characteristics: host response rate to requests, whether
the host is a superhost, whether the host identity has been verified.

Booking-related characteristics: whether the property can be instantly
booked, the cancellation policy To answer this overarching question, we
would need to understand the following:

Which features from the raw dataset would be most predictive of nightly
price? Which machine learning model at which hyperparameter settings can
best predict nightly price? Under what range of parameter values (e.g.,
charactistics of properties) would our model perform reliably?

## Dataset and Source

We have chosen a dataset that outlines Vancouver AirBnB listings. The
dataset can be found here under the Vancouver, British Columbia section.
A direct link to download the dataset is here. Data was compiled
November 9 2019.

## Findings and Results

Which machine laerning model can best predict nightly price?

| Model | Train MSE | Validation MSE | Time in seconds |
| :---- | --------: | -------------: | --------------: |
| lr    |  69770.76 |       73207.93 |          0.0200 |
| kNN   |  56795.11 |       99535.03 |          0.6007 |
| svr   |  77902.28 |       79010.28 |          1.3355 |
| rfr   |  22322.66 |       98606.53 |          6.1811 |

Table 1 shows the baseline training and validation mean squared errors
and training and validation learning time.

| Model          | Train MSE | Validation MSE | Time in seconds |
| :------------- | --------: | -------------: | --------------: |
| lr             | 69770.758 |       73207.93 |          0.0208 |
| kNN\_optimized |  4895.638 |       93072.14 |          0.5994 |
| svr\_optimized | 84757.310 |       85335.84 |          1.2896 |

Table 2 shows the optimized training and validation mean squared errors
and training and validation learning time.

Understanding Price by Neighborhood ![alt
tag](../output/neighborhoods.png)

![alt tag](../output/number_of_properties_by_price.png)

Understanding Price by Property Type ![alt
tag](../output/price_by_property_type.png)

![alt tag](../output/residual_plot.png)

## Interpretation of Results

## Critique of the Analysis

## Statement of Future Directions

## References
