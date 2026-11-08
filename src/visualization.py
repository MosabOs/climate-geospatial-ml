import matplotlib.pyplot as plt


def plot_geographical_distribution(df, save_path=None):
    """
    Plot the geographical distribution of weather locations
    using latitude and longitude.
    """

    # Keep one coordinate pair per geographical location
    locations = df[
        ["country", "location_name", "latitude", "longitude"]
    ].drop_duplicates(
        subset=["country", "location_name"]
    )

    # Create scatter plot
    plt.figure(figsize=(14, 7))

    plt.scatter(
        locations["longitude"],
        locations["latitude"],
        alpha=0.6,
        s=18
    )

    plt.title("Geographical Distribution of Weather Locations")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.xlim(-180, 180)
    plt.ylim(-90, 90)

    plt.grid(alpha=0.3)
    plt.tight_layout()

    # Save figure if a path is provided
    if save_path is not None:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()




def plot_locations_per_country(locations_per_country, save_path=None):
    """
    Plot the top 15 countries by number of geographical locations.
    """
    top_countries = locations_per_country.head(15).sort_values()

    plt.figure(figsize=(12, 7))
    top_countries.plot(kind="barh")
    plt.title("Top 15 Countries by Number of Weather Locations")
    plt.xlabel("Number of Locations")
    plt.ylabel("Country")
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()