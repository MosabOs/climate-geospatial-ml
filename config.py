from pathlib import Path

# Project Directories

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
MODELS_DIR = PROJECT_ROOT / "models"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
RESULTS_DIR = OUTPUTS_DIR / "results"

# Dataset Paths

RAW_DATA_PATH = RAW_DATA_DIR / "GlobalWeatherRepository.csv"

PROCESSED_DATA_PATH = (
    PROCESSED_DATA_DIR / "weather_spatial_features.csv"
)

# Model Configuration

RANDOM_STATE = 42
TEST_SIZE = 0.20