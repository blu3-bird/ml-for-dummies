# ============================================
# MULTIPLE LINEAR REGRESSION TEMPLATE
# ============================================

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ============================================
# STEP 1: LOAD DATA
# ============================================
df = pd.read_csv('YOUR_FILE.csv')
print("Shape:", df.shape)
print(df.head())

# ============================================
# STEP 2: SEPARATE X AND y
# ============================================
X = df.iloc[:, :-1].values  # All except last column
y = df.iloc[:, -1].values   # Last column

# ============================================
# STEP 3: ENCODE CATEGORICAL (if any)
# ============================================
# Find which column(s) are categorical
# categorical_index = [5]  # UPDATE THIS

ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(drop='first'), [5])  # UPDATE INDEX
    ],
    remainder='passthrough'
)
X = np.array(ct.fit_transform(X))

print(f"X shape after encoding: {X.shape}")

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
# STEP 6: MODEL COEFFICIENTS
# ============================================
print("\n" + "="*50)
print("MODEL COEFFICIENTS")
print("="*50)
print(f"Intercept (b₀): {regressor.intercept_:.2f}")

# UPDATE feature names based on your data
feature_names = ['Feature1', 'Feature2', 'Feature3', ...]
print("\nCoefficients:")
for name, coef in zip(feature_names, regressor.coef_):
    print(f"  {name}: {coef:.4f}")

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
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# ============================================
# STEP 9: COMPARE PREDICTIONS VS ACTUAL
# ============================================
print("\n" + "="*50)
print("PREDICTIONS VS ACTUAL")
print("="*50)

comparison = pd.DataFrame({
    'Predicted': y_pred,
    'Actual': y_test,
    'Error': y_test - y_pred
})
print(comparison)

# ============================================
# STEP 10: PREDICT FOR NEW DATA
# ============================================
print("\n" + "="*50)
print("NEW PREDICTIONS")
print("="*50)

# Example: UPDATE based on your features
# new_data = [[feature1, feature2, feature3, ...]]
new_data = [[1, 0, 2000, 4, 2, 10, 2]]  # UPDATE THIS
prediction = regressor.predict(new_data)
print(f"Predicted value: {prediction[0]:.2f}")