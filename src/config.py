# config.py
import os
from pathlib import Path

# epochs to train on
# EPOCHS = 10

# paths
ROOT_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))
RAW_FILE_PATH = ROOT_DIR / "data" / "raw"
INT_FILE_PATH = ROOT_DIR / "data" / "int"
TRAIN_FILE_PATH = ROOT_DIR / "data" / "final"
MODEL_OUTPUT_PATH = ROOT_DIR / "models"
NOTEBOOKS_PATH = ROOT_DIR / "notebooks"
REPORTS_PATH = ROOT_DIR / "reports" / "figures"

# visualisations
DEFAULT_FIGSIZE = (16, 10)
DEFAULT_AXIS_FONT_SIZE = 12
DEFAULT_PLOT_LINESTYLE = ":"
DEFAULT_PLOT_LINEWIDTH = 1
DEFAULT_DASHES = (1, 5)

# ML
RANDOM_STATE = 123
N_JOBS = -1
