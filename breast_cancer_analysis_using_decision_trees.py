# -*- coding: utf-8 -*-
"""Breast Cancer analysis using Decision Trees.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YSgizFoS_81uYyd0IMredOafSzYOfE8E

## California Dataset
+ We will be attempting to predict the median values in california using the given dataset.
"""

#Julius Nyambok - 104865
#Dennis Gikonyo - 113233
#David Adeola   - 091803
#Cynthia Musindi- 113450
#Ryan Williams  - 104811

# Importing the necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import sklearn.datasets
import numpy as np

# reading the file
breastData = sklearn.datasets.load_breast_cancer()

"""Data Analysis"""

# Converting the data provided into a to dataframe 
cancerData = pd.DataFrame(breastData.data,columns=breastData.feature_names)
cancerData.head()

cancerData.describe()

# selection of features
attributes = ['mean radius',	'mean texture',	'mean perimeter',	'mean area',	'mean smoothness',	'mean compactness',	'mean concavity',	'mean concave points',	'mean symmetry',	'mean fractal dimension',	'radius error',	'texture error',	'perimeter error',	'area error',	'smoothness error',	'compactness error',	'concavity error',	'concave points error',	'symmetry error',	'fractal dimension error',	'worst radius',	'worst texture',	'worst perimeter','worst area',	'worst smoothness'	,'worst compactness',	'worst concavity'	,'worst concave points'	,'worst symmetry'	,'worst fractal dimension']
X = cancerData[attributes]

"""Building of the model"""

# we will use the DecisionTreeRegressor
cancerModel = DecisionTreeRegressor(max_leaf_nodes=450,random_state=7)

# Splitting the training of the data and validation data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# Training the model
cancerModel.fit(train_X,train_y)

# Running predictions with the model
predictions = cancerModel.predict(val_X)
print(predictions[0:11])

# using mean absolute error to validate the model
print(mean_absolute_error(val_y, predictions))
