import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate sample training data
np.random.seed(42)
X_train = np.random.rand(100, 7)  # 7 features as per app.py
y_train = np.random.randint(100, 1000, size=100)  # Random visit counts

# Train a simple model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl has been created successfully!")
