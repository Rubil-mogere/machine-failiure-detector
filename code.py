
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the sensor data from the CSV file
data = pd.read_csv('sensor_data.csv')

# Feature selection: Assuming all columns are relevant for simplicity
selected_features = data.columns[:-1]
data_selected = data[selected_features]

# Handling missing data and outliers: Using mean imputation and winsorization for simplicity
data_selected.fillna(data_selected.mean(), inplace=True)
data_selected.clip(lower=data_selected.quantile(0.05), upper=data_selected.quantile(0.95), axis=1, inplace=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data_selected, data['equipment_failure'], test_size=0.2, random_state=42)

# Train the decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Simulate monitoring performance
temperature = 75.2  # Example temperature in Fahrenheit
processing_speed = 3.2  # Example processing speed in GHz
processing_power = 90  # Example processing power usage in watts

# Check for updates (example: assuming a version number)
current_version = "1.0"
latest_version = "2.0"

if current_version != latest_version:
    print("Update available! Consider updating your model to version", latest_version)

# Integration into the manufacturing process (example based on the first row of the test set)
if model.predict(X_test.iloc[0:1])[0] == 1:
    print("Warning: Equipment failure predicted. Schedule maintenance.")
else:
    print("No immediate equipment failure predicted.")

# Display performance metrics
print(f"Temperature: {temperature} °F")
print(f"Processing Speed: {processing_speed} GHz")
print(f"Processing Power: {processing_power} watts")
