import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


data = {
    "sqft": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 4],
    "bathrooms": [1, 2, 2, 3, 3],
    "price": [200000, 300000, 350000, 450000, 500000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["sqft", "bedrooms", "bathrooms"]]
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Custom prediction
sample = [[1800, 3, 2]]
prediction = model.predict(sample)

print("\nSample Input:", sample)
print("Predicted Price:", prediction[0])