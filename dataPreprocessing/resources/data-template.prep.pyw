# ============================================
# DATA PREPROCESSING TEMPLATE
# ============================================

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# ============================================
# STEP 1: LOAD DATA
# ============================================
df = pd.read_csv('YOUR_FILE.csv')

print("="*50)
print("DATA EXPLORATION")
print("="*50)
print(f"Shape: {df.shape}")
print(f"\nFirst 5 rows:\n{df.head()}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nTotal missing: {df.isnull().sum().sum()}")

# ============================================
# STEP 2: HANDLE MISSING TARGET (if applicable)
# ============================================
# If target has missing values, DROP those rows
# df = df.dropna(subset=['TARGET_COLUMN'])

# ============================================
# STEP 3: SEPARATE X AND y
# ============================================
X = df.drop(['ID_COLUMN', 'TARGET_COLUMN'], axis=1)
y = df['TARGET_COLUMN']

# ============================================
# STEP 4: IDENTIFY COLUMN TYPES
# ============================================
categorical_columns = ['col1', 'col2', 'col3']  # UPDATE THESE
numerical_columns = ['col4', 'col5', 'col6']    # UPDATE THESE

# ============================================
# STEP 5: IMPUTE MISSING VALUES
# ============================================
# Categorical
cat_imputer = SimpleImputer(strategy='most_frequent')
X[categorical_columns] = cat_imputer.fit_transform(X[categorical_columns])

# Numerical
num_imputer = SimpleImputer(strategy='mean')
X[numerical_columns] = num_imputer.fit_transform(X[numerical_columns])

print(f"\nMissing after imputation: {X.isnull().sum().sum()}")

# ============================================
# STEP 6: ENCODE CATEGORICAL VARIABLES
# ============================================
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(drop='first'), categorical_columns)
    ],
    remainder='passthrough'
)
X = np.array(ct.fit_transform(X))

# If y is categorical (classification), encode it too:
# le = LabelEncoder()
# y = le.fit_transform(y)

print(f"\nX shape after encoding: {X.shape}")

# ============================================
# STEP 7: TRAIN-TEST SPLIT
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ============================================
# STEP 8: FEATURE SCALING
# ============================================
# Find number of numerical columns
num_cols = len(numerical_columns)

sc = StandardScaler()
X_train[:, -num_cols:] = sc.fit_transform(X_train[:, -num_cols:])
X_test[:, -num_cols:] = sc.transform(X_test[:, -num_cols:])

# ============================================
# STEP 9: FINAL VERIFICATION
# ============================================
print("\n" + "="*50)
print("PREPROCESSING COMPLETE!")
print("="*50)
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train sample: {y_train[:5]}")
print(f"y_test sample: {y_test[:5]}")