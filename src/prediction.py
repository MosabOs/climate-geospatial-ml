
from functools import lru_cache

from src.data_loader import load_model
from src.feature_engineering import create_prediction_features


@lru_cache(maxsize=1)
def get_model():
    """
    Load and cache the trained model.
    """

    return load_model()


def predict_temperature(latitude, longitude, date, hour):
    """
    Predict temperature using the trained Extra Trees model.
    """

    model = get_model()

    features = create_prediction_features(
        latitude,
        longitude,
        date,
        hour
    )

    prediction = model.predict(features)

    return float(prediction[0])
