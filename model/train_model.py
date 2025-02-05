import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset from the specified path
# Adjust path as necessary
data = pd.read_csv(
    'C:/Users/DELL/OneDrive/Desktop/Phising Link scanner/model/dataset_phishing.csv')

# Display the first few rows of the dataset and its columns to understand its structure
print(data.head())  # This shows the first few rows of data
print(data.columns)  # This prints out all column names

# Extract features and labels (adjust these according to your dataset structure)
# Replace with actual feature columns based on what you see from data.columns
# Example placeholder; adjust as needed
X = data[['length_url', 'length_hostname', 'nb_dots']]
# Assuming 'status' is your label column (adjust if necessary)
y = data['status']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'trained_model.pkl')

# Optionally evaluate the model on the test set and print accuracy
accuracy = model.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')
