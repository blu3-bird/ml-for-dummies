from pathlib import Path
import os
import sys

CURRENT_DIR = Path.cwd()

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

#defining the dataset file

CAR_PRICE = DATASETS_DIR / 'car-price.csv'

COFFEE_SALES = DATASETS_DIR / 'coffee_sales.csv'

CROP_YIELD = DATASETS_DIR / 'crop-yield.csv'

DELIVERY_TIME = DATASETS_DIR / 'delivery_time.csv'

HOUSE_PRICES = DATASETS_DIR / 'house-prices.csv'

SALARY_DATA = DATASETS_DIR / 'Salary_Data.csv'

STUDENT_STUDY = DATASETS_DIR / 'student_study.csv'

WEBSITE_REVENUE = DATASETS_DIR / 'website-revenue.csv'

S_LN = DATASETS_DIR / 's-ln.csv'

LN_P = DATASETS_DIR / 'ln-p.csv'

