# author: Monique Wong, Polina Romanchenko, Trevor Kwan
# date: 2020-01-18

'''This script downloads open data from an input URL. And saves it in a specified directory.  

Usage: data.py --data_url=<data_url> --file_path=<file_path> 

Options:
--data_url=<data_url> URL where data can be downloaded from
--file_path=<file_path>  Path (including filename) to save the csv file.
'''

import pandas as pd
import numpy as np
import requests
import os
from docopt import docopt

opt = docopt(__doc__)

def main(data_url, file_path):
    ## to run this: python data.py --data_url 'http://data.insideairbnb.com/canada/bc/vancouver/2019-11-09/data/listings.csv.gz' --file_path data

    filename = os.path.join(file_path, data_url.split("/")[-1])
    with open(filename, "wb") as f:
        r = requests.get(data_url)
        f.write(r.content)
        
#Check if the file was created
def test_function(file_path):
    assert check_file(file_path), "File wasn't downloaded."

if __name__ == "__main__":
    main(opt["--data_url"], opt["--file_path"])
