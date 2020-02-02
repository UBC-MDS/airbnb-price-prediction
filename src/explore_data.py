# author: Monique Wong, Polina Romanchenko, Trevor Kwan
# date: 2020-01-23

'''This script creates visualisations regarding the distribution of prices, nightly price 
variation by neighborhoods and property type for Airbnb properties in Vancouver area. 
Output is used for creating of the final report. 

Usage: src/explore_data.py --data_path=<data_path> --file_path=<file_path>

Options:

--data_path=<data_path> name of data file that should be fetched
  
--file_path=<file_path>  name of the folder, where you want visualisations to be saved 

'''
import numpy as np
import pandas as pd
import requests
import os
import altair as alt
from docopt import docopt

opt = docopt(__doc__)

def main(data_path, file_path):

    data = pd.read_csv(f"{data_path}", index_col=0)

    #First plot
    number_of_properties_by_price = alt.Chart(data).mark_bar(clip = True).encode(
        alt.X('price:Q',
             scale=alt.Scale(domain=(0, 1000)),
             bin=alt.Bin(extent=[0, 1000], step=25),
             title='Nightly price'),
        alt.Y('count()', title='No. of properties')
    ).properties(width=600, height = 300, title = 'Number of properties by nightly price (between $0 and $1000)')
    
    number_of_properties_by_price.save(os.path.join(file_path, 'number_of_properties_by_price.png'))
    
    
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
    
    Neighborhoods.save(os.path.join(file_path, 'neighborhoods.png'))
    
    #Third plot
    
    price_by_property_type = alt.Chart(price_data_labels).mark_rect().encode(
          alt.X('property_type:N', title="Property Type"),
          alt.Y('price:Q', bin=alt.Bin(extent=[0, 1000], step=50), title="Nightly price ($ CAD)"),
          alt.Color('count()')
      )
      
    price_by_property_type.save(os.path.join(file_path, 'price_by_property_type.png'))
    
# Check if images were saved
def test_images_created():
    main('data/train_data.csv', 'output')
    assert os.path.isfile('output/number_of_properties_by_price.png'), "properties by price image wasn't created."
    assert os.path.isfile('output/neighborhoods.png'), "neighborhoods by price image wasn't created."
    assert os.path.isfile('output/price_by_property_type.png'), "property type by price image wasn't created."
    
test_images_created()

if __name__ == "__main__":
    main(opt["--data_path"], opt["--file_path"])
