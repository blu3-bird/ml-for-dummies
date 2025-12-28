from pathlib import Path
import os

CURRENT_DIR = Path(__file__)

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

#Define the datasets and notebooks dir

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

#defining the dateset files 

ADS_BUDGET_PROFIT = DATASETS_DIR / 'ads_budget_profit.csv'

HORSE_POWER = DATASETS_DIR / 'horse-power.csv'

TEMP_POWER_USAGE = DATASETS_DIR / 'temp_power_usage.csv'

POSITION_SALARIES = DATASETS_DIR / 'Position_Salaries.csv'

TEMP_AND_ICE = DATASETS_DIR / 'temp_and_ice.csv'