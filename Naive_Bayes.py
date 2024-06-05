from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# load the iris dataset
iris = load_iris()

# store data
X = iris.data   # feature matrix (X)
y = iris.target # response vector (y)

# splitting training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

# training the model 
model = GaussianNB() # gaussian naive bayes function
model.fit(X_train, y_train)

# making predictions
y_pred = model.predict(X_test)

# comparing actual values vs predicted values  ===>  (y_test) vs (y_pred)
score = metrics.accuracy_score(y_test, y_pred)*100
print("Gaussian Naive Bayes model accuracy(in %):", score)
