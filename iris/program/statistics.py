#################
# statistics.py #
#################
# Show iris.csv analytic data onto terminal.
# Note that data using in seaborn must be pandas DataFrame object.

import pandas as pd
import seaborn as sns

# Load .csv file (your file path)
iris = "../data/iris.csv"

# Set data as pandas DataFrame
data = pd.read_csv(iris)
# Set data as a group
data_groups = data.groupby("variety")

###############################################
# "Count" each number of rows in the dataset. #
###############################################
print(data.count())

##########################################################
# "Maximum value" of each number of cols in the dataset. #
##########################################################
print(data.max())

##########################################################
# "Minimum value" of each number of cols in the dataset. #
##########################################################
print(data.min())

##############################################
# "Mean" for every numeric column.           #
##############################################
# Mean = \bar{x}                             #
# \bar{x} = \frac{1}{n} \sum^{n}_{i=1} x_{i} #
##############################################
print(data.mean())
#print(data_groups.mean()) # Show results as a table.

#############################################################################
# "Median" for every numeric column.                                        #
#############################################################################
# Median = \tilde{x}                                                        #
# \tilde{x} = \begin{cases}                                                 #
# 	x_{\left( \frac{n+1}{2} \right)} & if n is odd\\                    #
# 	\frac{1}{2} \left( x_{\left( \frac{n}{2} \right)}                   #
#		+ x_{\left( \frac{n}{2} + 1 \right)} \right) & if n is even #
# 	\end{cases}                                                         #
#############################################################################
print(data.median())
#print(data_groups.median()) # Show results as a table.

##############################################################
# "Variance" for every numeric column.                       #
##############################################################
# Variance = s^{2}                                           #
# s^{2} = \frac{1}{n-1} \sum^{n}_{i=1} (x_{i} - \bar{x})^{2} #
##############################################################
print(data.var())
#print(data_groups.var()) # Show results as a table.

#################################################
# "Standard deviance" for every numeric column. #
#################################################
# Standard deviance = s                         #
# s = \sqrt{s^{2}}                              #
#################################################
print(data.std())

###################################################################################
# "p-th percentile" for every numeric column.                                     #
# "p-th percentile" is the number in the dataset such that roughly p% of the data #
# is less than this number.                                                       #
###################################################################################
# 10% = quantile(.1)                                                              #
# 25% = quantile(.25)                                                             #
# 75% = quantile(.75)                                                             #
# 95% = quantile(.95)                                                             #
###################################################################################
print(data.quantile(.1))
print(data.quantile(.25))
print(data.quantile(.75))
print(data.quantile(.95))

################
# .describes() #
################
print(data.describe())
print(data_groups.describe())
