from pathlib import Path 

CURRENT_DIR = Path.cwd()

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

DT = DATASETS_DIR / 'dt.csv'