# author: Trevor Kwan, Polina Romanchenko, Monique Wong
# date: 2020-01-18

'''This script downloads Restaurant & consumer data Data Set from UCI Machine Learning Repository


Usage: scr/viz_script.py --data_path=<data_path> --file_path=<file_path>

Options:

--data_path=<data_path> name of data file that should be fetched
  
--file_path=<file_path>  name of the folder, where you want plots to be saved 

'''
import numpy as np
import pandas as pd
import requests
import os
import altair as alt
from docopt import docopt
from selenium import webdriver

opt = docopt(__doc__)

def main(data_path, file_path):
# to run this: python vz_report.py --data_path=<your_data_location with name> --file_path=<name of the folder>

    data = pd.read_csv(f"{data_path}", index_col=0)

    #First plot
    number_of_properties_by_price = alt.Chart(data).mark_bar(clip = True).encode(
        alt.X('price:Q',
             scale=alt.Scale(domain=(0, 1000)),
             bin=alt.Bin(extent=[0, 1000], step=25),
             title='Nightly price'),
        alt.Y('count()', title='No. of properties')
    ).properties(width=600, height = 300, title = 'Number of properties by nightly price (between $0 and $1000)')
    
    number_of_properties_by_price.save(file_path + '/number_of_properties_by_price.png', 
    webdriver = 'chrome', scale_factor=10.0)
    
    
    #Piece of wrangling for next 2 plots. Assigning labels to columns 
    
    price_data_labels = data[['price', 'neighbourhood_cleansed', 'property_type']]
    price_data_labels['label'] = pd.cut(price_data_labels['price'], bins=[0, 100, 300, 500, 13000], 
                               include_lowest=True, labels=['low', 'mid', 'high', 'exceptional'])
  
    
    #Second plot
    Neighborhoods = alt.Chart(price_data_labels).mark_rect().encode(
        alt.X('neighbourhood_cleansed:N', title="Neighborhoods"),
        alt.Y('price:Q', bin=alt.Bin(extent=[0, 1000], step=50), title="Nightly price ($ CAD)"),
        alt.Color('count()')
    )
    
    Neighborhoods.save(file_path + '/neighborhoods.png', webdriver = 'chrome', scale_factor=10.0)
    
    #Third plot
    
    price_by_property_type = alt.Chart(price_data_labels).mark_rect().encode(
          alt.X('property_type:N', title="Property Type"),
          alt.Y('price:Q', bin=alt.Bin(extent=[0, 1000], step=50), title="Nightly price ($ CAD)"),
          alt.Color('count()')
      )
    price_by_property_type.save(file_path + '/price_by_property_type.png', webdriver = 'chrome', scale_factor=10.0)


if __name__ == "__main__":
    main(opt["--data_path"], opt["--file_path"])
