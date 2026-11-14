
import joblib

from config import FINAL_MODEL_PATH


def load_model():
    """
    Load the trained Extra Trees model.
    """

    if not FINAL_MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {FINAL_MODEL_PATH}"
        )

    model = joblib.load(FINAL_MODEL_PATH)

    return model
