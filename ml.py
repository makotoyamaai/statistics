#########
# ml.py #
#########

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load .csv file (your file path)
iris = "../data/iris.csv"

# Set data as pandas DataFrame
data = pd.read_csv(iris)
# Set data as groups
data_groups = data.groupby("variety")
# Set data as numpy array
df = np.loadtxt(iris, skiprows=1, delimiter=",", usecols=[0,1,2,3])
#print(df.shape) # (150, 4)

X = df           # Feature data
y = data.variety # Label data

#######################
# Logistic Regression #
#######################
# Split training-data and test-data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Logistic regression model
# LogisticRegression(solver = optimization method (default: lbfgs),
#                    multi_class = classification method (default: auto))
model = LogisticRegression(solver='lbfgs',  multi_class='auto')
# Fit model to training-data
model.fit(X_train, y_train)
# Estimate labels by test-data
y_predicted=model.predict(X_test)

# Evaluate accuracy                        ######################
print(accuracy_score(y_test, y_predicted)) # 0.9777777777777777 #
                                           ######################

#####################
# Linear Regression #
#####################
# In here, consider "petal_length" and "petal_width".
X_petal_length = data[['petal.length']].values
y_petal_width = data['petal.width'].values
plt.scatter(X_petal_length, y_petal_width)
#plt.show()

# Split training-data and test-data
X_train, X_test, y_train, y_test = train_test_split(X_petal_length,
                                                    y_petal_width,
                                                    test_size=0.3,
                                                    random_state=1)

# Linear regression model
model_linear_regression = LinearRegression()
# Fit train-data to model
model_linear_regression.fit(X_train, y_train)
# Estimate by test-data
y_predicted = model_linear_regression.predict(X_test)
# Evaluate predict-error (mean squared error)
evaluation = mean_squared_error(y_test, y_predicted)
                  ########################
print(evaluation) # 0.039618634662187076 #
                  ########################

# Plot data
x_plot = np.linspace(1, 7)
X_plot = x_plot[:, np.newaxis]
y_plot = model_linear_regression.predict(X_plot)
plt.scatter(X_petal_length, y_petal_width)
plt.plot(x_plot, y_plot)
plt.title("Linear Regression")
plt.savefig("../data/linear_regression.png")
plt.show()

##############
# Clustering #
# K-means    #
##############
# In here, consider "petal_length" and "petal_width".
X_iris = data[['petal.length', 'petal.width']].values

# K-Means model
model_k_means = KMeans(n_clusters=3) # 3 class
# Fit model to data
model_k_means.fit(X_iris)
# Estimate the cluster
y_k_means = model_k_means.predict(X_iris)

# Plot data
data['cluster'] = y_k_means
data.plot.scatter(x='petal.length', y='petal.width', c='cluster', colormap='viridis')
plt.title("Clustering: K-means")
plt.savefig("../data/k-means.png")
plt.show()

##############
# Clustering #
# Meanshift  #
##############
# In here, consider "petal_length" and "petal_width".
X_iris = data[['petal.length', 'petal.width']].values

# Meanshift model
model_meanshift = MeanShift()
# Fit model to data
model_meanshift.fit(X_iris)
# Estimate the cluster
y_meanshift = model_meanshift.predict(X_iris)

# Plot data
data['cluster'] = y_meanshift
data.plot.scatter(x='petal.length', y='petal.width', c='cluster', colormap='viridis')
plt.title("Clustering: Meanshift")
plt.savefig("../data/meanshift.png")
plt.show()

#######################
# Clustering          #
# Spectral clustering #
#######################
# In here, consider "petal_length" and "petal_width".
X_iris = data[['petal.length', 'petal.width']].values

# Spectral clustering model
model_sc = SpectralClustering(n_clusters=3, # 3 class
                              assign_labels='discretize', 
                              random_state=0)
# Fit model to data
model_sc.fit(X_iris)

# Plot data
data.plot.scatter(x='petal.length', y='petal.width', c='cluster', colormap='viridis')
plt.title("Clustering: Spectral clustering")
plt.savefig("../data/spectral-clustering.png")
plt.show()

############################
# Dimensionality reduction #
# PCA                      #
############################
X_iris_pca = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values

# PCA model
model_pca = PCA(n_components=2) # 2D data
# Fit model to data
model_pca.fit(X_iris_pca)
# Dimensionality reduction
X_2d = model_pca.transform(X_iris_pca)

# Plot data
data['pca1'] = X_2d[:, 0]
data['pca2'] = X_2d[:, 1]
sns.lmplot(x='pca1', y='pca2', hue='variety', data=data, fit_reg=False).set(title="PCA of IRIS dataset").savefig("../data/pca.png")

############################
# Dimensionality reduction #
# LDA                      #
############################
X_iris_lda = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values

# LDA model
model_lda = LinearDiscriminantAnalysis(n_components=2) # 2D data
# Fit model to data
model_lda.fit(X_iris_lda, y)
# Dimensionality reduction
X_2d = model_lda.transform(X_iris_lda)

# Plot data
data['lda1'] = X_2d[:, 0]
data['lda2'] = X_2d[:, 1]
sns.lmplot(x='lda1', y='lda2', hue='variety', data=data, fit_reg=False).set(title="LDA of IRIS dataset").savefig("../data/lda.png")
