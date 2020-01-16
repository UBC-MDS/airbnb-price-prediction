# author: Trevor Kwan, Polina Romanchenko, Monique Wong
# date: 2020-01-18

'''This script downloads Restaurant & consumer data Data Set from UCI Machine Learning Repository

Usage: data.py --data_url=<data_url> --file_path=<file_path> 

Options:
--data_url=<data_url> URL where data can be downloaded from
--file_path=<file_path>  Path (including filename) to save the csv file.
'''

import pandas as pd
import numpy as np
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from docopt import docopt

opt = docopt(__doc__)

def main(data_url, file_path):
    ## to run this: python data.py --data_url 'https://archive.ics.uci.edu/ml/machine-learning-databases/00232/RCdata.zip' --file_path ../data

    # read in data
    resp = urlopen(data_url)
    zf = ZipFile(BytesIO(resp.read()))

    zf.extractall(file_path)

if __name__ == "__main__":
    main(opt["--data_url"], opt["--file_path"])