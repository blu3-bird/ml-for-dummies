from pathlib import Path 

CURRENT_DIR = Path.cwd()

PROJECT_ROOT = CURRENT_DIR.parent.absolute()

DATASETS_DIR = PROJECT_ROOT / 'practiceDatasets'

NOTEBOOK_DIR = PROJECT_ROOT / 'practiceExercises'

DT = DATASETS_DIR / 'dt.csv'
DT2_FEATURE_IMPORTANCES = DATASETS_DIR / 'dt2-feature-importances.csv'
DS_DTR = DATASETS_DIR / 'ds-dtr.csv'