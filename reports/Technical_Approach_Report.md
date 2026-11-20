# Technical Approach Report – TenantEase AI

## 1. Introduction

TenantEase AI is a machine learning proof of concept designed to estimate the likelihood of a tenant making a late rent payment in the following month.

The application uses a supervised classification approach and provides an interactive Streamlit dashboard for viewing tenant risk levels and generating individual predictions.

The current implementation uses synthetic data and is intended for demonstration and evaluation purposes.

## 2. System Architecture

The solution follows a simple machine learning pipeline:

1. Synthetic data generation.
2. Data preparation and feature selection.
3. Model training.
4. Model evaluation.
5. Model serialization and storage.
6. Prediction through a Streamlit application.
7. Risk visualization and report generation.

### Main Components

- `generate_dataset.py`: Generates the synthetic tenant payment dataset.
- `model_training.py`: Trains and evaluates the machine learning model.
- `models/rent_risk_model.pkl`: Stores the trained model.
- `models/features.pkl`: Stores the feature information required by the application.
- `app.py`: Loads the model, accepts tenant information, generates predictions, and displays the dashboard.
- `data/tenant_payments.csv`: Contains the generated dataset.

## 3. Data Pipeline

### Data Generation

A synthetic dataset containing 1,000 tenant records was generated for the proof of concept.

The target variable is:

`late_next_month`

It represents whether a tenant is labelled as likely to make a late payment in the following month.

The generated dataset contains:

- 755 records labelled as not late.
- 245 records labelled as late.

### Data Preparation

The dataset is loaded using Pandas. Input features are separated from the target variable before model training.

The dataset is divided into:

- 80% training data.
- 20% testing data.

This allows the model to be evaluated on records that were not used during training.

## 4. Model Selection

### Random Forest Classifier

A Random Forest Classifier was selected for this proof of concept.

It is an ensemble learning algorithm that combines predictions from multiple decision trees.

Reasons for selecting this model include:

- Suitable for classification problems.
- Can learn relationships between multiple input features.
- Handles nonlinear patterns.
- Provides feature importance information.
- Offers a practical baseline for tabular data.

The model predicts the target class based on the tenant-related input features.

## 5. Model Training and Evaluation

The model is trained using the generated tenant dataset.

The training workflow includes:

1. Loading the dataset.
2. Separating features and target.
3. Splitting the data into training and testing sets.
4. Training the Random Forest Classifier.
5. Generating predictions on the test data.
6. Evaluating model performance.
7. Saving the trained model using Joblib.

### Evaluation Results

The current experiment achieved approximately 65% test accuracy.

The confusion matrix was:

| Actual / Predicted | Not Late | Late |
| ------------------ | -------: | ---: |
| Not Late           |      110 |   41 |
| Late               |       29 |   20 |

These results indicate that the model is an initial experimental baseline and requires further improvement.

Because the dataset is synthetic, these results must not be interpreted as real-world performance.

## 6. Application Architecture

The Streamlit application provides two main capabilities.

### Dashboard

The dashboard displays:

- Total tenant count.
- High-risk tenant count.
- Medium-risk tenant count.
- Low-risk tenant count.
- Risk distribution chart.
- Tenant risk report.
- Risk filtering.
- CSV report download.

### Individual Tenant Prediction

The individual prediction interface accepts tenant-related input values and uses the trained model to estimate late-payment risk.

The application displays:

- Predicted risk category.
- Prediction probability.
- Risk-based recommendations.
- Feature importance information.

The risk categories are intended to support review and prioritization rather than automatic decision-making.

## 7. Prompt Engineering and AI Architecture

The current proof of concept uses a traditional supervised machine learning model rather than a Large Language Model (LLM).

Therefore, no generative AI prompt engineering or LLM-based response generation is implemented in the current version.

The prediction workflow is based on structured input features passed to the trained Random Forest model.

### Potential Future Extension

A future version could introduce an LLM-based assistant to:

- Explain model predictions in plain language.
- Summarize tenant risk reports.
- Generate draft follow-up messages for property managers.
- Answer questions about aggregate dashboard information.

Any such extension would require carefully designed prompts, access controls, privacy safeguards, and human review.

## 8. Execution Instructions

### Prerequisites

- Python installed.
- pip package manager.
- Project dependencies listed in `requirements.txt`.

### Installation

Clone the repository:

```bash
git clone https://github.com/Aravindavenge/Cynbit-AI-ML-Assignment.git
cd Cynbit-AI-ML-Assignment
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the dataset:

```bash
python generate_dataset.py
```

Train the model:

```bash
python model_training.py
```

Start the application:

```bash
streamlit run app.py
```

The dashboard will be available at:

`http://localhost:8501`

## 9. Limitations

- The current dataset is synthetic.
- Model performance has not been validated using real tenant payment records.
- The model may produce false-positive and false-negative predictions.
- The current implementation does not integrate with live payment systems.
- Risk predictions should not be used as the sole basis for decisions affecting tenants.

## 10. Future Improvements

1. Evaluate the model using authorized historical payment data.
2. Compare Random Forest with other classification algorithms.
3. Perform hyperparameter tuning and feature engineering.
4. Improve model evaluation using precision, recall, F1-score, and ROC-AUC.
5. Introduce explainability techniques.
6. Add secure data integration and access controls.
7. Deploy the application to a cloud platform.
8. Monitor model performance and data drift over time.

## 11. Conclusion

TenantEase AI demonstrates an end-to-end machine learning workflow for rent payment late-risk prediction.

The proof of concept combines synthetic data generation, Random Forest classification, model evaluation, and an interactive Streamlit dashboard.

It provides a foundation for further experimentation and could be extended into a more comprehensive property management intelligence solution after validation with appropriate real-world data.

**Project:** TenantEase AI  
**Assessment:** Cynbit AI/ML Engineer Intern  
**Author:** Aravind Bommena
