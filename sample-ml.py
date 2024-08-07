import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class SimpleMLModel:
    def __init__(self):
        self.model = LinearRegression()
    
    def load_data(self, data):
        """
        Load and preprocess the data.
        
        :param data: Pandas DataFrame containing the data.
        """
        self.X = data.iloc[:, :-1].values
        self.y = data.iloc[:, -1].values
    
    def split_data(self, test_size=0.2, random_state=42):
        """
        Split the data into training and testing sets.
        
        :param test_size: Proportion of the data to use as test set.
        :param random_state: Random seed for reproducibility.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state)
    
    def train(self):
        """Train the linear regression model on the training data."""
        self.model.fit(self.X_train, self.y_train)
    
    def evaluate(self):
        """Evaluate the model on the test data."""
        self.y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, self.y_pred)
        r2 = r2_score(self.y_test, self.y_pred)
        return mse, r2
    
    def predict(self, X_new):
        """
        Make predictions on new data.
        
        :param X_new: Array-like, shape (n_samples, n_features).
        """
        return self.model.predict(X_new)
    
    def get_model(self):
        """Return the trained model."""
        return self.model

# Example usage
if __name__ == "__main__":
    # Create a simple dataset
    data = pd.DataFrame({
        'Feature1': np.random.rand(100),
        'Feature2': np.random.rand(100),
        'Target': np.random.rand(100) * 100
    })

    ml_module = SimpleMLModel()
    ml_module.load_data(data)
    ml_module.split_data()
    ml_module.train()
    
    mse, r2 = ml_module.evaluate()
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    
    # Make predictions on new data
    X_new = np.array([[0.5, 0.5], [0.2, 0.8]])
    predictions = ml_module.predict(X_new)
    print(f"Predictions: {predictions}")
