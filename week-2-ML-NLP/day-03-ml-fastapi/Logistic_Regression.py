import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "passed": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df[["hours_studied"]]
y = df["passed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))

# Probability prediction
sample = [[4.5]]
prob = model.predict_proba(sample)

print("\nSample Input:", sample)
print("Probability of Passing:", prob[0][1])