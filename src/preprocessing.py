
from datetime import datetime
import math


def validate_prediction_inputs(latitude, longitude, date, hour):
    """
    Validate inputs before making a temperature prediction.
    """

    # Validate coordinate types
    if not isinstance(latitude, (int, float)):
        raise ValueError("Latitude must be a valid number.")

    if not isinstance(longitude, (int, float)):
        raise ValueError("Longitude must be a valid number.")

    # Validate finite coordinate values
    if not math.isfinite(latitude):
        raise ValueError("Latitude must be a valid number.")

    if not math.isfinite(longitude):
        raise ValueError("Longitude must be a valid number.")

    # Validate coordinate ranges
    if not -90 <= latitude <= 90:
        raise ValueError("Latitude must be between -90 and 90.")

    if not -180 <= longitude <= 180:
        raise ValueError("Longitude must be between -180 and 180.")

    # Validate date
    if not isinstance(date, str):
        raise ValueError("Date must be a string in YYYY-MM-DD format.")

    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")

        if parsed_date.strftime("%Y-%m-%d") != date:
            raise ValueError

    except ValueError:
        raise ValueError("Date must follow YYYY-MM-DD format.")

    # Validate hour type and range
    if not isinstance(hour, int) or isinstance(hour, bool):
        raise ValueError("Hour must be an integer between 0 and 23.")

    if not 0 <= hour <= 23:
        raise ValueError("Hour must be between 0 and 23.")

    return True
