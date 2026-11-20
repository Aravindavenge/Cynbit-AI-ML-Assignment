# TenantEase AI – Rent Payment Late-Risk Prediction

## Project Overview

TenantEase AI is a proof-of-concept machine learning application designed to predict the likelihood of a tenant making a late rent payment in the following month.

The application analyzes tenant payment patterns and other relevant features to classify tenants into Low, Medium, and High risk categories. It provides a dashboard for reviewing risk distribution and an individual tenant prediction interface.

## Objectives

- Predict the likelihood of late rent payments.
- Identify tenants who may require early attention.
- Visualize tenant risk distribution through an interactive dashboard.
- Provide downloadable tenant risk reports.
- Demonstrate how machine learning can support proactive property management.

## Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Model:** Random Forest Classifier
- **Data Processing:** Pandas
- **Dashboard:** Streamlit
- **Model Storage:** Joblib
- **Visualization:** Streamlit charts

## Project Structure

```text
Cynbit-AI-ML-Assignment/
│
├── data/
│   └── tenant_payments.csv
│
├── models/
│   ├── features.pkl
│   └── rent_risk_model.pkl
│
├── reports/
│
├── app.py
├── generate_dataset.py
├── model_training.py
├── requirements.txt
└── README.md
```

## Machine Learning Approach

A Random Forest Classifier is used to predict whether a tenant is likely to make a late payment in the next month.

The workflow includes:

1. Generating a synthetic tenant payment dataset.
2. Preparing and processing the dataset.
3. Separating input features and the target variable.
4. Splitting the dataset into training and testing sets.
5. Training the Random Forest model.
6. Evaluating model performance.
7. Saving the trained model for application use.

The target variable is `late_next_month`.

## Dashboard Features

- Overall tenant count and risk summary.
- High, Medium, and Low risk classification.
- Risk distribution visualization.
- Tenant risk report with filtering.
- CSV export of tenant risk reports.
- Individual tenant risk prediction.
- Prediction probability display.
- Recommendations based on predicted risk.
- Feature importance visualization.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aravindavenge/Cynbit-AI-ML-Assignment.git
cd Cynbit-AI-ML-Assignment
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate the dataset

```bash
python generate_dataset.py
```

### 6. Train the model

```bash
python model_training.py
```

### 7. Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your browser at:

`http://localhost:8501`

## Model Evaluation

The model was evaluated using a train-test split.

- Training and testing split: 80:20
- Algorithm: Random Forest Classifier
- Test accuracy: Approximately 65%

**Important:** This is an experimental proof of concept using synthetic data. The reported performance does not represent validated real-world prediction accuracy. Further testing with real, authorized tenant payment data would be required before production use.

## Future Improvements

- Integrate real-time tenant payment data.
- Explore additional machine learning algorithms.
- Improve prediction performance through feature engineering and hyperparameter tuning.
- Add explainable AI to make predictions easier to understand.
- Integrate automated alerts for high-risk tenants.
- Deploy the application to a cloud platform.

## Disclaimer

This project is developed for educational and demonstration purposes. The dataset is synthetic and does not contain actual tenant or customer information.

## Author

**Aravind Bommena**

AI/ML Engineer Intern Assessment Project – Cynbit
