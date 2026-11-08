



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



