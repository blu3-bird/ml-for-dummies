from pathlib import Path
import os

CURRENT_DIR = Path(__file__)

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

#Define the datasets and notebooks dir

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

#loading the datasets for notebooks
ADS_BUDGET_PROFIT = DATASETS_DIR / 'ads_budget_profit.csv'
HORSE_POWER = DATASETS_DIR / 'horse-power.csv'
POSITION_SALARIES = DATASETS_DIR / 'Position_Salaries.csv'
TEMP_AND_ICE = DATASETS_DIR / 'temp_and_ice.csv'
TEMP_POWER_USAGE = DATASETS_DIR / 'temp_power_usage.csv'
EXPERIENCE_PRODUCTIVITY = DATASETS_DIR / 'experience_productivity.csv'
COFFEE_COOLING = DATASETS_DIR / 'coffee-cooling.csv'
DRUG_RESPONSE = DATASETS_DIR / 'drug_response.csv'
ENGINE_EFFICIENCY = DATASETS_DIR /  'engine-efficiency.csv'
ELECTRIC_MOTOR_PERFORMANCE = DATASETS_DIR / 'electric-motor-performance.csv'
COFFEE_BREW = DATASETS_DIR / 'coffee-brew.csv'
USED_CAR = DATASETS_DIR / 'used_car.csv'