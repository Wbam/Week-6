# Credit Scoring Model for Bati Bank

This project focuses on building a credit scoring model to categorize customers as high-risk or low-risk based on their transaction data. The project is divided into several tasks, each focusing on a specific aspect of the model development process.

## Table of Contents

1. [Task 1 - Data Collection and Preprocessing](#task-1---data-collection-and-preprocessing)
2. [Task 2 - Exploratory Data Analysis (EDA)](#task-2---exploratory-data-analysis-eda)
3. [Task 3 - Feature Engineering](#task-3---feature-engineering)
4. [Task 4 - Modeling](#task-4---modeling)
5. [Task 5 - Model Serving API Call](#task-5---model-serving-api-call)

## Task 1 - Data Collection and Preprocessing

- Collected transaction data for customers from various sources.
- Performed data cleaning and preprocessing, including handling missing values and normalizing data.

## Task 2 - Exploratory Data Analysis (EDA)

- Conducted exploratory data analysis to understand customer behavior and transaction patterns.
- Generated visualizations to identify trends and correlations in the data.

## Task 3 - Feature Engineering

- Created additional features to enhance model performance.
- Implemented techniques like one-hot encoding for categorical variables and scaled numerical features.

## Task 4 - Modeling

### Model Selection and Training

- **Data Splitting**: Split the dataset into training and testing sets to evaluate model performance.
- **Model Selection**: Chose Logistic Regression and Random Forest as the models for this task.
- **Training**: Trained the models using the training data.

### Hyperparameter Tuning

- Implemented Grid Search for hyperparameter tuning of the Random Forest model to improve performance.

### Model Evaluation

- Evaluated models using the following metrics:
  - **Accuracy**: Ratio of correctly predicted observations to total observations.
  - **Precision**: Ratio of correctly predicted positive observations to total predicted positives.
  - **Recall (Sensitivity)**: Ratio of correctly predicted positive observations to all observations in the actual class.
  - **F1 Score**: Weighted average of Precision and Recall.
  - **ROC-AUC**: Area Under the Receiver Operating Characteristic Curve.

## Task 5 - Model Serving API Call

- **Framework**: Used Flask to create a REST API for serving the trained machine learning models for real-time predictions.
- **Loading the Model**: Loaded the trained Random Forest model using `pickle`.
- **API Endpoints**: Defined endpoints to accept input data and return predictions.
- **Handling Requests**: Implemented logic to receive input data, preprocess it, and make predictions.
- **Deployment**: Prepared the API for deployment on a web server or cloud platform.

## Installation

To set up the project environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
