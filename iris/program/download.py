###############
# download.py #
###############
# Download .csv file

import wget
import os
import pandas as pd
import seaborn as sns

# In here, download iris.csv from https://gist.github.com/netj/8836201#file-iris-csv
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# Set output path
output_path = "../data/"

# Make filename
file = "iris.csv"

# Download .csv file to our output path.
path = os.path.join("../data/", file)
download = wget.download(url, path)

# Load .csv file
iris = "../data/iris.csv"

# Set data as pandas DataFrame
data = pd.read_csv(iris)

# Plot and save figure
sns.pairplot(data,
	hue = "variety",
	hue_order = None,
	palette = None,
	vars = None,
	x_vars = None,
	y_vars = None,
	kind = 'scatter',
	diag_kind = 'auto',
	markers = None,
	height = 2.5,
	aspect = 1,
	dropna = True,
	plot_kws = None,
	diag_kws = None,
	grid_kws = None,
	size = None).savefig("../data/iris.png")
