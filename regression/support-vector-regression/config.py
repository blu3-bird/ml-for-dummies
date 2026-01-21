from pathlib import Path
import os

CURRENT_DIR = Path(__file__)

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

#Define the datasets and notebooks dir

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

DS1 = DATASETS_DIR / 'ds1.csv'
# print(f'hoipardeep {PROJECT_ROOT}')