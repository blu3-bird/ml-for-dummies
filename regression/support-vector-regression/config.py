from pathlib import Path
import os

CURRENT_DIR = Path(__file__)

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

#Define the datasets and notebooks dir

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

DS1 = DATASETS_DIR / 'ds1.csv'
EXPERIENCE_SALARY = DATASETS_DIR / 'experience_salary.csv'
DS02 = DATASETS_DIR / 'ds02.csv'
DS03 = DATASETS_DIR / 'ds03.csv'