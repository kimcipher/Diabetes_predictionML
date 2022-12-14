# -*- coding: utf-8 -*-
"""Copy of Diabetesprediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11GuM-xSnaHqXSeddRdktLB-pzTqN2SRu
"""

import pandas 
data = pandas.read_csv("https://modcom.co.ke/data/datasets/pima.csv")
data

data.shape

data.head(10)

data.tail(10)

data.describe()

array = data.values

# features
X = array[:, 0:8]
X

Y = array[:, 8]
Y

from sklearn import model_selection # split the whole data into training sets(70%) and testing sets(30%)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.30, random_state=42)

X_train

Y_train

X_test

Y_test

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB 
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

model = GradientBoostingClassifier() 

model.fit(X_train, Y_train)

predictions = model.predict(X_test)
print("The model predicted", predictions)

print("The correct answers are", Y_test)

from sklearn.metrics import accuracy_score

print("Model accuracy is : ", accuracy_score(predictions, Y_test)*100)

data.head(3)

diabetes_features = [[4, 100, 59, 30, 129.0000, 34.7, 0.567, 24]]
diabetes_predicted = model.predict(diabetes_features)
print("you are likely to be:", diabetes_predicted)

if diabetes_predicted == "Diabetic":
  print("Please visit your nearest health facility for more consultation..")
else:
  print("You're safe from diabetes, please continue maintaining your healthy diabetic life")