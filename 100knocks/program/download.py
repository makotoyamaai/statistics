###############
# download.py #
###############

import os
import wget

# In here, download data.csv
url = "https://raw.githubusercontent.com/The-Japan-DataScientist-Society/100knocks-preprocess/master/docker/work/data/store.csv"

# Set output path
output_path = "./data/"

# Make filename
file = "store.csv"

# Download .csv file to our output path.
path = os.path.join("./data/", file)
download = wget.download(url, path)
