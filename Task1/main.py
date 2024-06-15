import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.datasets import load_iris

iris = load_iris()

iris_var1 = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_var1['species'] = iris.target

print(iris_var1)

print(iris_var1.describe())

import seaborn as sns
sns.pairplot(iris_var1, hue='species')
plt.show()

X = iris.data
y = iris.target  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', conf_matrix)

class_report = classification_report(y_test, y_pred, target_names=iris.target_names)
print('Classification Report:\n', class_report)

