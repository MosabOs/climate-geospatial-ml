
from src.prediction import predict_temperature
from src.preprocessing import validate_prediction_inputs


def read_float(prompt, field_name):
    """
    Read and convert a numeric input to float.
    """

    value = input(prompt).strip()

    try:
        return float(value)
    except ValueError:
        raise ValueError(
            f"{field_name} must be a numeric value."
        ) from None


def read_integer(prompt, field_name):
    """
    Read and convert an input to integer.
    """

    value = input(prompt).strip()

    try:
        return int(value)
    except ValueError:
        raise ValueError(
            f"{field_name} must be an integer."
        ) from None


def get_user_inputs():
    """
    Collect and convert user inputs.
    """

    latitude = read_float("Enter latitude: ", "Latitude")
    longitude = read_float("Enter longitude: ", "Longitude")

    date = input("Enter date (YYYY-MM-DD): ").strip()

    hour = read_integer("Enter hour (0-23): ", "Hour")

    return latitude, longitude, date, hour


def main():
    print("=" * 45)
    print("       CLIMATE GEOSPATIAL ML")
    print("          Temperature Prediction")
    print("=" * 45)

    try:
        # Collect inputs
        latitude, longitude, date, hour = get_user_inputs()

        # Validate inputs
        validate_prediction_inputs(
            latitude,
            longitude,
            date,
            hour
        )

        # Generate prediction
        prediction = predict_temperature(
            latitude,
            longitude,
            date,
            hour
        )

        # Display result
        print("\n" + "=" * 45)
        print(f"Predicted Temperature: {prediction:.2f} °C")
        print("=" * 45)

    except ValueError as error:
        print(f"\nInput Error: {error}")

    except FileNotFoundError as error:
        print(f"\nModel Error: {error}")

    except KeyboardInterrupt:
        print("\n\nPrediction cancelled by user.")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")


if __name__ == "__main__":
    main()
