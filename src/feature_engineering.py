
import numpy as np
import pandas as pd


def create_spatial_features(df):
    """
    Create additional spatial features from geographical coordinates.
    """
    df = df.copy()

    df["abs_latitude"] = df["latitude"].abs()

    df["is_northern_hemisphere"] = (
        df["latitude"] > 0
    ).astype(int)

    df["is_eastern_hemisphere"] = (
        df["longitude"] > 0
    ).astype(int)

    return df



def create_prediction_features(latitude, longitude, date, hour):
    """
    Create the exact features required by the trained model.
    """

    date = pd.to_datetime(date)
    day_of_year = date.dayofyear

    features = pd.DataFrame([{
        "latitude": latitude,
        "longitude": longitude,
        "hour_sin": np.sin(2 * np.pi * hour / 24),
        "hour_cos": np.cos(2 * np.pi * hour / 24),
        "day_sin": np.sin(2 * np.pi * day_of_year / 365.25),
        "day_cos": np.cos(2 * np.pi * day_of_year / 365.25)
    }])

    return features
