import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
try:
    data = pd.read_csv(
        'C:/Users/DELL/OneDrive/Desktop/Phising Link scanner/model/dataset_phishing.csv')
except FileNotFoundError:
    print("Error: The dataset file was not found. Please check the file path.")
    exit()

# Display dataset structure
print(data.head())
print(data.columns)

# Extract features and labels
X = data.drop(columns=['status'])  # Use all columns except the target
y = data['status']  # Target column

# Encode categorical labels
le = LabelEncoder()
y = le.fit_transform(y)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model using cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print(
    f'Cross-validation accuracy: {cv_scores.mean():.2f} (± {cv_scores.std():.2f})')

# Evaluate the model on the test set
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(f'Test set accuracy: {accuracy_score(y_test, y_pred):.2f}')

# Save the trained model and label encoder
joblib.dump(model, 'trained_model.pkl')
joblib.dump(le, 'label_encoder.pkl')
print("Model and label encoder saved successfully.")
