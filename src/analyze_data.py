# author: Monique Wong, Polina Romanchenko, Trevor Kwan
# date: January 25, 2020

'''This script performs machine learning analysis and outputs figures used in analysis

Usage: analyze_data.py --training_file_path=<training_file_path> --test_file_path=<test_file_path> --output_file_path=<output_file_path>

Options:
--training_file_path=<training_file_path> file path to training set
--test_file_path=<test_file_path> file path to test set
--output_file_path=<file_path>  path to save output

'''

import numpy as np
import pandas as pd
import time
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import PolynomialFeatures

import requests
import os
from docopt import docopt

opt = docopt(__doc__)

## to run this: python src/analyze_data.py --training_file_path data/train_data.csv --test_file_path data/test_data.csv --output_file_path report

# main function
def main(training_file_path, test_file_path, output_file_path):
  X_train, y_train, X_test, y_test = read_and_split(training_file_path, test_file_path)
  X_train_p, X_test_p = preprocess_features(X_train, X_test)
  X_train_subset, X_valid, y_train_subset, y_valid = test_baseline_models(X_train_p, y_train, output_file_path)
  random_search_svr, random_search_knn = hyperparameter_search(X_train_p, y_train)
  test_final_models(random_search_svr, random_search_knn, X_train_subset, X_valid, y_train_subset, y_valid, output_file_path)
  fit_and_plot_best_model(X_train_p, y_train, X_test_p, y_test, output_file_path)

# supporting functions

def read_and_split(training_file_path, test_file_path):
  """ This function reads in test and train data from the input paths and prepares features and target.
  
  Arguments:
  ---------------
  training_file_path -- str
    input path to the file with traing data
  
  test_file_path -- str
    input path to the file with test data
  
  """
  train = pd.read_csv(training_file_path)
  test = pd.read_csv(test_file_path)

  X_train = train.drop(columns = ['price', 'id', 'host_id'])
  y_train = train[['price']]

  X_test = test.drop(columns = ['price', 'id', 'host_id'])
  y_test = test[['price']]
  
  return X_train, y_train, X_test, y_test
  
def preprocess_features(X_train, X_test):
  """
  This function encodes categorical and numeric features, handles missing data  and outputs prossesed 
  dataframes for future models to use.
  Categorical features handeled with OneHotEncoder and missing data points filled with category "missing".
  Numerical features scaled with StandartScaler and missing data points are filled with median values.
  
  
  Arguments:
  ---------------
    X_train -- pd.DataFrame
      training set containing all features
    
    X_test -- pd.DataFrame
      test set containing all features
  
  """
  
  
  # Identify numeric and categorical features
  numeric_features = ['host_response_rate', 'accommodates', 'bathrooms', 'bedrooms', 'beds']

  categorical_features = ['host_is_superhost','property_type','host_identity_verified', 
                        'neighbourhood_cleansed','instant_bookable','cancellation_policy']

  # Build a pipeline to do data processing
  numeric_transformer = Pipeline(steps=[
                                        ('imputer', SimpleImputer(strategy='median')),
                                        ('scaler', StandardScaler())
                                      ])


  categorical_transformer = Pipeline(steps=[
                                            ('imputer', SimpleImputer(strategy='constant', 
                                                                    fill_value='missing')),
                                            ('onehot', OneHotEncoder(handle_unknown='ignore'))
                                          ])

  preprocessor = ColumnTransformer(
                                  transformers=[
                                      ('num', numeric_transformer, numeric_features),
                                      ('cat', categorical_transformer, categorical_features)
                                  ])

  X_train_p = preprocessor.fit_transform(X_train)
  X_test_p = preprocessor.transform(X_test)
  
  return X_train_p, X_test_p

def test_baseline_models(X_train_p, y_train, output_file_path):
  """
  This function makes a subset of train dataset, trains variety of models, outputs time usage, MSE for train 
  and validation set results to a csv file.
  
  Arguments:
  ---------------
    X_train_p -- pd.DataFrame
      train set with encoded and scaled features(output of preprocess_features function)
    
    y_train -- pd.DataFrame
      train set containing target values
    
    output_file_path -- str
      path for desired output folder
  
  """
  X_train_subset, X_valid, y_train_subset, y_valid = train_test_split(X_train_p, y_train,test_size = 0.2,random_state = 123)
  
#  y_train_subset = np.array(y_train_subset)
  
  results_dict = {}

  models = {
            'lr': LinearRegression(),
            'kNN': KNeighborsRegressor(),
            'svr' : SVR(kernel='rbf'), 
            'rfr' : RandomForestRegressor(), 
           }

  for model_name, model in models.items():
      t = time.time()
      model.fit(X_train_subset, y_train_subset);
      y_train_pred = model.predict(X_train_subset)
      y_valid_pred = model.predict(X_valid)
      tr_mse = mean_squared_error(y_train_subset, y_train_pred)
      valid_mse = mean_squared_error(y_valid, y_valid_pred)
      elapsed_time = time.time() - t
      results_dict[model_name] = [round(tr_mse,3), round(valid_mse,3), round(elapsed_time,4)]
      
  results_df = pd.DataFrame(results_dict).T
  results_df.columns = ["Train MSE", "Validation MSE", "Time in seconds"]
  results_df.to_csv(os.path.join(output_file_path, 'baseline_results.csv'))

  return X_train_subset, X_valid, y_train_subset, y_valid
  

def hyperparameter_search(X_train_p, y_train):
  """
  This function uses random search to tune hyperparameters for 2 best performing models KNN and RBF SVR.
  
  Arguments:
  ---------------
    X_train_p -- pd.DataFrame
      train set with encoded and scaled features(output of preprocess_features function)
    
    y_train -- pd.DataFrame
      train set containing target values  
  
  """
  # for svr
  svr = SVR(kernel='rbf')
  param_grid = {
      "gamma" : np.geomspace(10e-6, 1, 6)
  }
  random_search_svr = RandomizedSearchCV(svr, param_grid, cv=10, scoring = make_scorer(mean_squared_error))
  random_search_svr.fit(X_train_p, y_train)
  
  # for knn
  knn = KNeighborsRegressor()
  param_grid = {
      "n_neighbors" : np.arange(4, 32, 4),
      "weights"     : ['uniform', 'distance']
  }
  
  random_search_knn = RandomizedSearchCV(knn, param_grid, cv=10, scoring = make_scorer(mean_squared_error))
  random_search_knn.fit(X_train_p, y_train)
  
  return random_search_svr, random_search_knn

def test_final_models(random_search_svr, random_search_knn, X_train_subset, X_valid, y_train_subset, y_valid, output_file_path):
  """
  This function tests models with optimized hyperparameters and outputs time usage, MSE for train 
  and validation set results to a csv file.
  
  Arguments:
  ---------------
    random_search_svr -- sklearn.model_selection._search.RandomizedSearchCV
      optimized RBF SVR model
      
    random_search_knn -- sklearn.model_selection._search.RandomizedSearchCV
      optimized KNN model
    
    X_train_subset: pd.DataFrame
      subset of X_train_p with encoded and scaled features used for fitting models
      
    X_valid : pd.DataFrame
      subset of X_train_p with encoded and scaled features used for obtaining validation error
      
    y_train_subset : pd.DataFrame
      subset of y_train with target values
      
    y_valid : pd.DataFrame
      subset of y_train with target values
      
    output_file_path -- str
      path for desired output folder    
  """
  
  
  svr_gamma = random_search_svr.best_params_['gamma']
  knn_weights = random_search_knn.best_params_['weights']
  knn_neighbors = random_search_knn.best_params_['n_neighbors']
  
  best_models_dict = {}

  models = {
            'lr': LinearRegression(),
            'kNN_optimized': KNeighborsRegressor(n_neighbors=knn_neighbors, weights=knn_weights),
            'svr_optimized' : SVR(kernel='rbf', gamma=svr_gamma), 
           }
  
  for model_name, model in models.items():
      t = time.time()  
      model.fit(X_train_subset, y_train_subset);
      y_train_pred = model.predict(X_train_subset)
      y_valid_pred = model.predict(X_valid)
      tr_mse = mean_squared_error(y_train_subset, y_train_pred)
      valid_mse = mean_squared_error(y_valid, y_valid_pred)
      elapsed_time = time.time() - t
      best_models_dict[model_name] = [round(tr_mse,3), round(valid_mse,3), round(elapsed_time,4)]
      
  best_models_df = pd.DataFrame(best_models_dict).T
  best_models_df.columns = ["Train MSE", "Validation MSE", "Time in seconds"]
  best_models_df.to_csv(os.path.join(output_file_path, 'optimized_results.csv'))
  
def fit_and_plot_best_model(X_train_p, y_train, X_test_p, y_test, output_file_path):
  """
  This function computes residuals of the best performing model and outputs a chart with true Airbnb cost in relation 
  to residuals.  
  
  Arguments:
  ---------------
    X_train_p -- pd.DataFrame
      train set with encoded and scaled features(output of preprocess_features function)
    
    y_train -- pd.DataFrame
      train set containing target values  
      
    X_test_p -- pd.DataFrame
      test set with encoded and scaled features(output of preprocess_features function)

    y_test -- pd.DataFrame
      test set containing target values
      
    output_file_path -- str
      path for desired output folder    
  """
  lr = LinearRegression()
  lr.fit(X_train_p, y_train)
  y_train_pred = lr.predict(X_train_p)
  y_test_pred = lr.predict(X_test_p)

  y_test = np.array(y_test).ravel()
  y_test_pred = np.array(y_test_pred).ravel()
  test_residuals = y_test_pred - y_test
  compare_test_predictions_df = pd.DataFrame({'true': y_test, 'predicted': y_test_pred, 'residuals': test_residuals})
  
  residual_plot = alt.Chart(compare_test_predictions_df).mark_circle(size=4).encode(
      alt.X('true',
            scale=alt.Scale(domain=(0, 800)),
            title='true price'),
      alt.Y('residuals',
            scale=alt.Scale(domain=(-800, 800)),
           title='residuals: predicted less actual')
  ).properties(title='Residual plot for linear regression'
  ).interactive()
  
  residual_plot.save(os.path.join(output_file_path, 'residual_plot.png'))

if __name__ == "__main__":
  main(opt["--training_file_path"], opt["--test_file_path"], opt["--output_file_path"])
  
