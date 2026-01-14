# ============================================
# SIMPLE LINEAR REGRESSION TEMPLATE
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ============================================
# STEP 1: LOAD DATA
# ============================================
df = pd.read_csv('YOUR_FILE.csv')
print("Data shape:", df.shape)
print(df.head())
print(df.describe())

# ============================================
# STEP 2: VISUALIZE
# ============================================
plt.figure(figsize=(10, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], color='blue', alpha=0.6)
plt.xlabel('X (Feature)')
plt.ylabel('y (Target)')
plt.title('Data Visualization')
plt.show()

# ============================================
# STEP 3: PREPARE DATA
# ============================================
X = df.iloc[:, 0:1].values  # First column (2D array)
y = df.iloc[:, 1].values    # Second column

# ============================================
# STEP 4: SPLIT DATA
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================================
# STEP 5: TRAIN MODEL
# ============================================
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# ============================================
# STEP 6: MODEL EQUATION
# ============================================
print("\n" + "="*50)
print("MODEL EQUATION")
print("="*50)
print(f"Intercept (b₀): {regressor.intercept_:.4f}")
print(f"Slope (b₁): {regressor.coef_[0]:.4f}")
print(f"\ny = {regressor.intercept_:.2f} + {regressor.coef_[0]:.4f} × x")

# ============================================
# STEP 7: PREDICTIONS
# ============================================
y_pred = regressor.predict(X_test)

# ============================================
# STEP 8: EVALUATION
# ============================================
print("\n" + "="*50)
print("MODEL EVALUATION")
print("="*50)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.4f}")
print(f"RMSE: {rmse:.4f}")

# ============================================
# STEP 9: VISUALIZE RESULTS
# ============================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Training set
axes[0].scatter(X_train, y_train, color='red', alpha=0.6)
axes[0].plot(X_train, regressor.predict(X_train), color='blue')
axes[0].set_title('Training Set')
axes[0].set_xlabel('X')
axes[0].set_ylabel('y')

# Test set
axes[1].scatter(X_test, y_test, color='red', alpha=0.6)
axes[1].plot(X_train, regressor.predict(X_train), color='blue')
axes[1].set_title('Test Set')
axes[1].set_xlabel('X')
axes[1].set_ylabel('y')

plt.tight_layout()
plt.show()

# ============================================
# STEP 10: NEW PREDICTIONS
# ============================================
print("\n" + "="*50)
print("NEW PREDICTIONS")
print("="*50)

new_values = [100, 200, 300]  # UPDATE THESE
for val in new_values:
    pred = regressor.predict([[val]])[0]
    print(f"X = {val} → Predicted y = {pred:.2f}")