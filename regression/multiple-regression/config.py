from pathlib import Path


CURRENT_DIR = Path.cwd()

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOKS_DIR = PROJECT_ROOT / 'practiceExercises'

#loading dataset files

STARTUPS = DATASETS_DIR / '50_Startups.csv'

EMPOLYEE_PRODUCTIVITY = DATASETS_DIR / 'empolyee_productivity.csv'

HOTEL_BOOKING = DATASETS_DIR / 'hotel_booking.csv'

HOUSE_PRICE_DATASET = DATASETS_DIR / 'house-prices-dataset.csv'

HOUSE_PRICES = 'house-prices.csv'

MARKETING_ROI = DATASETS_DIR / 'marketing_roi.csv'

RESTAURANT_SALES = DATASETS_DIR / 'restaurant-sales.csv'

STARTUP_VALUATION = DATASETS_DIR / 'startup_valuation.csv'

S_ML = DATASETS_DIR / 's-ml.csv'

MLR_P = DATASETS_DIR / 'mlr-p.csv'