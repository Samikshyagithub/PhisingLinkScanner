# Phishing Link Scanner Project

## Overview

This project is a phishing link scanner that uses machine learning to detect whether a given URL is likely to be a phishing attempt or a safe link. The project comprises a frontend web interface, a backend Flask server with an API endpoint for scanning URLs, and a trained machine learning model that makes predictions.

![Phishing Link Scanner Screenshot](images/image1.png)

## Project Structure


## How It Works

1.  **Frontend**: Provides a user interface where users can input a URL. When the user clicks the "Scan" button, the frontend sends a request to the backend.

2.  **Backend**: Receives the URL, extracts relevant features, and uses the pre-trained machine learning model to predict whether the URL is a phishing attempt or a safe link.

3.  **Machine Learning Model**: Trained on a dataset of phishing and legitimate URLs, the model learns patterns and features indicative of phishing attempts.


## How It Detects Phishing Links

The machine learning model detects phishing links by analyzing patterns and features extracted from the URLs. During the training phase, the model learns to associate certain features with phishing or legitimate URLs. When a new URL is submitted, the model extracts the same features and uses its learned knowledge to predict whether the URL is likely to be a phishing attempt.

The key to accurate detection lies in the quality of the training data and the relevance of the extracted features. Continuously updating the training data and refining the feature extraction process can improve the model's performance over time.







