
# ==========================================
# TENANTEASE AI - MACHINE LEARNING MODEL
# ==========================================

import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load dataset
print("Loading tenant dataset...")

df = pd.read_csv("data/tenant_payments.csv")

# 2. Select input features
features = [
    "late_payment_count",
    "average_delay_days",
    "outstanding_balance",
    "missed_payments",
    "on_time_payment_rate"
]

X = df[features]

# 3. Select target variable
y = df["late_next_month"]

# 4. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 5. Create Random Forest model
print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    random_state=42,
    class_weight="balanced"
)

# 6. Train the model
model.fit(X_train, y_train)

# 7. Make predictions
predictions = model.predict(X_test)

# 8. Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("\n========== MODEL RESULTS ==========")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# 9. Save trained model
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/rent_risk_model.pkl")

# 10. Save feature names
joblib.dump(features, "models/features.pkl")

print("\nModel saved successfully!")
print("Location: models/rent_risk_model.pkl")
