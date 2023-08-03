# -*- coding: utf-8 -*-
"""ml_lab_ass-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yYVWtWOtqqEivWYq9WljaRs4OodPCxSp
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier object
dt_model = DecisionTreeClassifier()

# Fit the model to the training data
dt_model.fit(X_train, y_train)

# Make predictions on the test data
predictions = dt_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the predictions
print("Predictions:", predictions)

# Print the accuracy
print("Accuracy:", accuracy)

!pip install graphviz
!pip install pydotplus

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
import graphviz
import pydotplus
from IPython.display import Image

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier object
dt_model = DecisionTreeClassifier()

# Fit the model to the training data
dt_model.fit(X_train, y_train)

# Make predictions on the test data
predictions = dt_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the predictions
print("Predictions:", predictions)

# Print the accuracy
print("Accuracy:", accuracy)

# Visualize the decision tree
dot_data = export_graphviz(dt_model, out_file=None, feature_names=iris.feature_names,
                           class_names=iris.target_names, filled=True, rounded=True,
                           special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier object
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test data
predictions = rf_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

# Print the predictions
print("Predictions:", predictions)

# Print the accuracy
print("Accuracy:", accuracy)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier object
dt_model = DecisionTreeClassifier()

# Fit the Decision Tree model to the training data
dt_model.fit(X_train, y_train)

# Make predictions on the test data using the Decision Tree model
dt_predictions = dt_model.predict(X_test)

# Calculate the accuracy of the Decision Tree model
dt_accuracy = accuracy_score(y_test, dt_predictions)

# Print the accuracy of the Decision Tree model
print("Decision Tree Accuracy:", dt_accuracy)

# Create a Random Forest classifier object with 100 trees
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the Random Forest model to the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test data using the Random Forest model
rf_predictions = rf_model.predict(X_test)

# Calculate the accuracy of the Random Forest model
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Print the accuracy of the Random Forest model
print("Random Forest Accuracy:", rf_accuracy)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier object with 100 trees
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the Random Forest model to the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test data using the Random Forest model
rf_predictions = rf_model.predict(X_test)

# Calculate the accuracy of the Random Forest model
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Print the Random Forest model
print("Random Forest Model:")
for idx, estimator in enumerate(rf_model.estimators_):
    print(f"Tree {idx + 1}:")
    tree_predictions = estimator.predict(X_test)
    tree_accuracy = accuracy_score(y_test, tree_predictions)
    print("Tree Accuracy:", tree_accuracy)
    print("Tree Predictions:", tree_predictions)
    print()

# Print the overall accuracy of the Random Forest model
print("Random Forest Accuracy:", rf_accuracy)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

# Random Forest Classifier
# Create a Random Forest classifier object
rf_model = RandomForestClassifier()

# Fit the model to the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test data using the Random Forest model
rf_predictions = rf_model.predict(X_test)

# Calculate the accuracy of the Random Forest model
rf_accuracy = accuracy_score(y_test, rf_predictions)

# Print the Random Forest model and accuracy
print("Random Forest Model:", rf_model)
print("Random Forest Accuracy:", rf_accuracy)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load the iris dataset
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Number of clusters (you can change this according to your requirement)
k = 3

# Run k-means algorithm
kmeans = KMeans(n_clusters=k, random_state=42)
cluster_assignments = kmeans.fit_predict(iris_data)

# Extract cluster centers
cluster_centers = kmeans.cluster_centers_

# Visualize the results (using two features - sepal length and petal length)
plt.scatter(iris_data['sepal length (cm)'], iris_data['petal length (cm)'], c=cluster_assignments, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 2], c='red', marker='X', s=200, label='Cluster Centers')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('K-means Clustering of Iris Data')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Iris dataset
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['Petal.Length'] = iris.target

# Step 3: Split the data into training and testing sets
X = iris_data[['petal width (cm)', 'sepal length (cm)']]
y = iris_data['Petal.Length']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Step 4: Simple Linear Regression
# Fit a model to predict Petal.Length based on petal width (cm)
simple_model = LinearRegression()
simple_model.fit(X_train[['petal width (cm)']], y_train)

# Step 5: Multiple Linear Regression
# Fit a model to predict Petal.Length based on petal width (cm) and sepal length (cm)
multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)

# Step 6: Model Evaluation
# Make predictions on the test data
predictions_simple = simple_model.predict(X_test[['petal width (cm)']])
predictions_multiple = multiple_model.predict(X_test)

# Calculate Mean Squared Error (MSE) for each model
mse_simple = mean_squared_error(y_test, predictions_simple)
mse_multiple = mean_squared_error(y_test, predictions_multiple)

print("Mean Squared Error (MSE) for Simple Linear Regression:", mse_simple)
print("Mean Squared Error (MSE) for Multiple Linear Regression:", mse_multiple)

# Step 7: Visualize the results
plt.figure(figsize=(12, 6))

# Plot 1: Actual vs. Predicted for Simple Linear Regression
plt.subplot(1, 2, 1)
plt.scatter(y_test, predictions_simple, label='Predicted', color='blue')
plt.plot(y_test, y_test, label='Actual', color='red')
plt.xlabel('Actual Petal.Length')
plt.ylabel('Predicted Petal.Length')
plt.title('Simple Linear Regression')
plt.legend()

# Plot 2: Actual vs. Predicted for Multiple Linear Regression
plt.subplot(1, 2, 2)
plt.scatter(y_test, predictions_multiple, label='Predicted', color='blue')
plt.plot(y_test, y_test, label='Actual', color='red')
plt.xlabel('Actual Petal.Length')
plt.ylabel('Predicted Petal.Length')
plt.title('Multiple Linear Regression')
plt.legend()

plt.show()

!pip install mlxtend

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transaction data (list of lists)
transactions = [['Milk', 'Eggs', 'Bread'],
                ['Milk', 'Diaper', 'Beer', 'Eggs'],
                ['Milk', 'Bread', 'Diaper', 'Beer'],
                ['Bread', 'Eggs', 'Diaper'],
                ['Milk', 'Bread', 'Eggs', 'Diaper', 'Beer']]

# Convert the transaction data to a one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
min_support = 0.4  # Minimum support threshold
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

# Print frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# Generate association rules from frequent itemsets
min_confidence = 0.6  # Minimum confidence threshold
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_confidence)

# Print association rules
print("\nAssociation Rules:")
print(rules)