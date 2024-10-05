from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

# Function to train the model
def train_model(features, target):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize a linear regression model
    model = LinearRegression()

    # Train the model using training data
    model.fit(X_train, y_train)

    # Calculate the score on test data (R-squared)
    score = model.score(X_test, y_test)
    print(f"Model trained. Test R-squared: {score:.4f}")

    return model

# Function to predict future estimates
def predict(model, new_data):
    # Assuming new_data is a DataFrame with the same columns as the features used to train the model
    predictions = model.predict(new_data)
    return predictions

