# AI Opportunity Report – TenantEase AI

## 1. Executive Summary

TenantEase AI is a proof-of-concept application that demonstrates how artificial intelligence and machine learning can help property management teams identify tenants who may be at risk of making late rent payments.

The solution uses historical-style tenant payment information to estimate the likelihood of a late payment in the following month. It classifies tenants into Low, Medium, and High risk categories and presents the results through an interactive dashboard.

The objective is to demonstrate how predictive analytics can support earlier intervention, improve visibility into payment patterns, and help property managers make more informed decisions.

## 2. Problem Statement

Late rent payments can create challenges for property management operations, including:

- Uncertainty in expected rental income.
- Additional time spent following up on overdue payments.
- Difficulty identifying tenants who may need early attention.
- Limited visibility into patterns that could indicate payment risk.

A proactive approach to identifying potential late payments could help property management teams prioritize follow-ups and plan their operations more effectively.

## 3. Proposed AI Solution

TenantEase AI uses a supervised machine learning approach to estimate whether a tenant may make a late rent payment in the following month.

The proof of concept includes:

- A tenant payment dataset.
- A Random Forest classification model.
- Individual tenant risk predictions.
- Low, Medium, and High risk categories.
- A dashboard showing overall risk distribution.
- A downloadable tenant risk report.
- Recommendations based on predicted risk.

## 4. Potential Business Value

### Improved visibility

The dashboard provides a consolidated view of tenant payment risk, helping property managers identify accounts that may require attention.

### Proactive follow-ups

High-risk predictions can help teams prioritize communication before a payment becomes overdue.

### Better operational planning

Risk summaries may support planning for payment follow-ups and rental income monitoring.

### Reduced manual effort

Automated risk classification can reduce the need to review every tenant record manually.

These are potential benefits that would need to be validated through a real-world pilot.

## 5. AI/ML Approach

The proof of concept uses a Random Forest Classifier.

The model is trained using tenant-related input features and a target variable named `late_next_month`.

The workflow includes:

1. Dataset generation.
2. Data preparation.
3. Feature and target separation.
4. Training and testing split.
5. Model training.
6. Model evaluation.
7. Saving the trained model.
8. Using the model for predictions in the Streamlit application.

## 6. Proof-of-Concept Results

The current experiment uses 1,000 synthetically generated tenant records.

The dataset contains:
- 755 records labelled as not late.
- 245 records labelled as late.

The model achieved approximately 65% accuracy on its test split.

These results are preliminary and are not evidence of real-world performance. The dataset is synthetic and must be replaced or supplemented with authorized historical payment data before business deployment.

## 7. Future AI Opportunities

The solution could be extended through:

- Integration with authorized rent payment records.
- More advanced feature engineering.
- Model comparison and hyperparameter tuning.
- Explainable AI to clarify prediction factors.
- Automated reminders and follow-up workflows.
- Model monitoring and periodic retraining.
- Integration with property management systems.

## 8. Risks and Considerations

- Synthetic data may not reflect actual tenant behaviour.
- Predictions can produce false positives and false negatives.
- Tenant information must be handled securely.
- Predictions should support human decision-making, not automatically determine tenant eligibility or trigger punitive action.
- The model should be tested for fairness, reliability, and performance before production use.

## 9. Conclusion

TenantEase AI demonstrates how machine learning can be applied to rent payment risk prediction. The proof of concept provides a foundation for exploring proactive tenant payment monitoring and data-driven property management.

A production-ready solution would require real, authorized data, further validation, privacy safeguards, and continuous model monitoring.
