
import pandas as pd
import numpy as np
import os

# 1. Set random seed for reproducible data
np.random.seed(42)

# 2. Generate 1000 sample tenants
n = 1000

tenant_ids = [f"TENANT_{i:04d}" for i in range(1, n + 1)]

# 3. Generate tenant payment information
late_payment_count = np.random.poisson(1.5, n)

average_delay_days = np.random.gamma(
    shape=2,
    scale=3,
    size=n
).round(1)

outstanding_balance = np.random.choice(
    [0, 500, 1000, 2000, 3000, 5000, 8000],
    size=n,
    p=[0.45, 0.10, 0.12, 0.10, 0.08, 0.08, 0.07]
)

missed_payments = np.random.poisson(0.5, n)

on_time_payment_rate = np.clip(
    100 - (late_payment_count * 12)
    - (missed_payments * 15)
    + np.random.normal(0, 8, n),
    0,
    100
).round(1)

# 4. Calculate probability of late payment
risk_score = (
    late_payment_count * 0.12
    + average_delay_days * 0.025
    + (outstanding_balance / 8000) * 0.20
    + missed_payments * 0.15
    - (on_time_payment_rate / 100) * 0.20
)

# Convert score into probability
probability = 1 / (1 + np.exp(-(
    risk_score - 0.65
) * 3))

# 5. Generate target variable
# 0 = No late payment
# 1 = Late payment

late_next_month = np.random.binomial(
    1,
    probability
)

# 6. Create dataset
df = pd.DataFrame({
    "tenant_id": tenant_ids,
    "late_payment_count": late_payment_count,
    "average_delay_days": average_delay_days,
    "outstanding_balance": outstanding_balance,
    "missed_payments": missed_payments,
    "on_time_payment_rate": on_time_payment_rate,
    "late_next_month": late_next_month
})

# 7. Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# 8. Save dataset as CSV
df.to_csv("data/tenant_payments.csv", index=False)

# 9. Display results
print("====================================")
print("TENANT DATASET GENERATED SUCCESSFULLY")
print("====================================")

print("Total tenants:", len(df))
print("\nFirst 10 records:")
print(df.head(10))

print("\nLate payment distribution:")
print(df["late_next_month"].value_counts())

print("\nDataset saved at: data/tenant_payments.csv")
