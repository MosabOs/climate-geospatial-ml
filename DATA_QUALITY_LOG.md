# Data Quality Log

## Project

**Climate & Geospatial ML --- World Weather Repository**

**Source dataset:** `GlobalWeatherRepository.csv`\
**Original dataset shape:** 170,928 rows × 41 columns\
**Processed spatial dataset:** `weather_spatial_features.csv`\
**Processed dataset shape:** 170,928 rows × 44 columns

This file records data quality observations discovered during dataset
understanding, geospatial EDA, feature engineering, and baseline model
preparation.

The log distinguishes confirmed issues from observations that still
require investigation. No value should be changed or removed solely
because it looks unusual; every cleaning decision must have a reason and
be documented.

------------------------------------------------------------------------

## 1. Dataset Integrity

  ---------------------------------------------------------------------------
  Check                   Observation                 Status / Decision
  ----------------------- --------------------------- -----------------------
  Missing values          `df.isnull().sum().sum()`   No pandas null values
                          returned 0 in the initial   detected in the
                          inspection.                 original dataset. This
                                                      does not rule out
                                                      encoded sentinel
                                                      values.

  Duplicate rows          `df.duplicated().sum()`     No fully duplicated
                          returned 0.                 rows detected.

  Original dimensions     170,928 rows × 41 columns.  Recorded as the
                                                      original dataset
                                                      dimensions.

  Spatially processed     170,928 rows × 44 columns.  Three spatial features
  dimensions                                          were added without
                                                      changing the row count.

  Timestamp coverage      2024-05-16 to 2026-10-13.   Dataset spans
                                                      approximately 880 days.

  Unique timestamps       28,420.                     Multiple
                                                      locations/records share
                                                      timestamps.

  Unique dates            880\.                       Recorded during dataset
                                                      understanding.
  ---------------------------------------------------------------------------

**Important:** A dataset can contain zero pandas nulls and still contain
invalid or sentinel values, such as `-9999`.

## 2. Country and Location Naming Inconsistencies

### 2.1 Country names

Some country names appear to refer to the same country but use different
labels. Examples include:

-   `USA United States of America`
-   `United States of America`

This can split one country's records into multiple groups and distort
country-level counts, joins, and grouped analysis.

**Decision:** Country names have not yet been standardized. A consistent
country-name mapping should be considered before further country-level
analysis or reporting.

### 2.2 Location names

Some location names appear malformed or inconsistent. Examples observed
during dataset understanding include:

-   `-Kingdom`
-   `Ivory Ivory Ban`
-   `Krasnyy Turkmenistan`
-   `Morocco City`

**Decision:** These names have not been manually corrected. They should
be reviewed before relying on location-name grouping, joining, or
location-level reporting.

### 2.3 Unique location counts

The dataset contains:

-   286 unique `(country, location_name)` combinations.
-   211 distinct country labels.
-   176 country labels with only one location (about 83.4%).
-   An average of 1.36 unique location names per country label.

The country-level counts may be affected by the inconsistent country
labels described above.

## 3. Geographical Coordinate Observations

### 3.1 Coordinate validity

The initial coordinate checks found:

-   0 records with latitude outside `[-90, 90]`.
-   0 records with longitude outside `[-180, 180]`.
-   0 records with missing latitude or longitude.
-   469 unique latitude/longitude pairs across all observations.

### 3.2 Multiple coordinate pairs per named location

A total of 203 `(country, location_name)` groups were found to contain
more than one coordinate pair.

Most observed coordinate variations were small. Niamey, Niger, was a
notable case with three coordinate pairs and a large spread.

The approximate 40.03 km figure previously calculated for Niamey is
based on the distance between opposite corners of the latitude/longitude
bounding ranges. It is a bounding-box estimate, not a verified maximum
distance between observed coordinate pairs.

The three Niamey coordinate pairs appeared in consecutive observation
periods:

-   May--October 2024: 138 records.
-   October 2024--August 2025: 322 records.
-   August 2025--October 2026: 418 records.

This may reflect changes in measurement locations or geographical
metadata. The dataset alone does not establish the cause.

**Decision:** Original coordinates are preserved. No coordinate records
have been removed or overwritten. Coordinate variation is documented as
a potential consistency issue.

## 4. Temporal Consistency and Observation Gaps

Timestamps were converted to datetime and sorted by country, location
name, and timestamp before calculating time gaps.

Observed results:

-   One zero or negative time gap.
-   1,191 time gaps greater than 48 hours.
-   Maximum observed gap: 17,010 hours (approximately 709 days).
-   The median time gap across observations was approximately 24 hours.

Some locations therefore have irregular observation intervals or long
periods without observations.

**Decision:** No observations were removed because of these gaps.
Temporal splitting and validation must respect timestamps. Any lag-based
or rolling features must be calculated within the correct location group
and using past observations only.

## 5. Extreme and Potentially Invalid Weather Values

### 5.1 Temperature

Initial target inspection found:

-   Minimum temperature: `-29.8°C`.
-   Maximum temperature: `79.3°C`.
-   102 records below `-20°C`.
-   One record above `50°C`.

The 102 low-temperature records were associated with cold-region
locations and countries, including Mongolia, Kazakhstan, Russia,
Belarus, Canada, and Finland. They were retained because the available
evidence did not establish that they were invalid.

The single `79.3°C` observation was recorded in Suva, Fiji, on
2026-04-24. Nearby observations were:

  Date           Temperature   Humidity   Pressure
  ------------ ------------- ---------- ----------
  2026-04-23          26.4°C        89%    1013 mb
  2026-04-24          79.3°C         7%    1013 mb
  2026-04-25          25.4°C       100%    1011 mb

The abrupt temperature and humidity changes, followed by a return to
nearby values, provide strong evidence that this is an anomalous
observation.

**Decision:** The one `79.3°C` row was excluded from the modeling copy
`df_model`. The original raw and processed files were not modified. The
102 records below `-20°C` were retained.

After exclusion, `df_model` contained 170,927 rows and 44 columns, with
no remaining temperature values above `50°C`.

### 5.2 Wind speed

The initial descriptive statistics showed:

-   Maximum `wind_kph`: `2963.2`.
-   Maximum `wind_mph`: `1841.2`.

These values are physically implausible for ordinary weather
observations and require investigation before wind features are used.

**Status:** Potential data quality issue. Not yet corrected or removed.

### 5.3 Atmospheric pressure

The initial descriptive statistics showed pressure values as high as:

-   `3006 mb` in Tegucigalpa, Honduras.
-   `3000 mb` in Tehran, Iran.

These are highly unusual for atmospheric pressure observations and
require investigation before pressure features are used.

**Status:** Potential data quality issue. Not yet corrected or removed.

### 5.4 Air quality

The initial inspection found encoded or invalid-looking values:

-   `air_quality_Carbon_Monoxide`: one value of `-9999`.
-   `air_quality_Sulphur_dioxide`: one value of `-9999`.
-   `air_quality_PM10`: minimum value of `-1848.15`.

The `-9999` values appear to be sentinel values rather than valid
measurements. The negative PM10 value also requires investigation.

**Status:** Do not use these fields in modeling until sentinel and
invalid values are investigated and handled.

## 6. Spatial Feature Engineering

Three spatial features were created:

-   `abs_latitude`
-   `is_northern_hemisphere`
-   `is_eastern_hemisphere`

Validation results:

-   Original shape: 170,928 × 41.
-   Spatially processed shape: 170,928 × 44.
-   No missing values in the three new features.
-   `abs_latitude` ranged from 0.1395 to 65.30.
-   Approximately 78.27% of observations were in the Northern
    Hemisphere.
-   Approximately 72.03% of observations were in the Eastern Hemisphere.

The original latitude and longitude columns were preserved.

The processed file was saved as:

`data/processed/weather_spatial_features.csv`

## 7. Baseline Modeling Decisions

The initial target is `temperature_celsius`.

The first baseline feature set uses:

-   `latitude`
-   `longitude`
-   `month_sin`
-   `month_cos`
-   `hour_sin`
-   `hour_cos`
-   `day_sin`
-   `day_cos`

Temporal features are derived from `last_updated`.

The following variables are excluded from the initial feature set
because they directly represent or may reveal the target:

-   `temperature_fahrenheit`
-   `feels_like_celsius`
-   `feels_like_fahrenheit`
-   Other target-derived or potentially target-leaking measurements.

The hemisphere indicators and `abs_latitude` are not included in this
first feature set because they are derived from the original
coordinates. Their additional value can be tested in later experiments.

The current feature matrix has shape `(170927, 8)`, and the target has
shape `(170927,)`. No missing values were found in either.

**Important validation concern:** Records are repeated over time for the
same locations. A random row-level split may place observations from the
same location and nearby time periods in both training and test sets,
producing overly optimistic results. Chronological and spatial
validation must be considered before interpreting model performance.

------------------------------------------------------------------------

## 8. Summary of Decisions and Pending Actions

  -----------------------------------------------------------------------
  Issue                   Current decision        Follow-up
  ----------------------- ----------------------- -----------------------
  Different country       Preserve original       Standardize country
  labels                  labels for now.         names before
                                                  country-level
                                                  aggregation or joins.

  Malformed location      Preserve original       Review if location-name
  names                   values.                 grouping or joins are
                                                  needed.

  Multiple coordinates    Preserve original       Investigate only if
  per location            coordinates.            they materially affect
                                                  spatial validation or
                                                  mapping.

  Long timestamp gaps     Retain records.         Respect time order;
                                                  calculate temporal
                                                  features within
                                                  location groups.

  One `79.3°C`            Excluded from           Keep the raw and
  temperature             `df_model` only.        processed source files
                                                  unchanged.

  102 temperatures below  Retained.               Reassess only if
  `-20°C`                                         further evidence
                                                  indicates invalid
                                                  records.

  Extreme wind speeds     Not corrected.          Investigate before
                                                  using wind features.

  Extreme pressure values Not corrected.          Investigate before
                                                  using pressure
                                                  features.

  `-9999` air-quality     Not corrected.          Treat as sentinel
  values                                          candidates; investigate
                                                  before use.

  Negative PM10           Not corrected.          Investigate before use.

  Spatial/temporal        Not resolved by feature Use appropriate
  leakage                 creation alone.         chronological and
                                                  spatial validation.
  -----------------------------------------------------------------------

## 9. Logging Policy

This log should be updated whenever a new data quality issue is
discovered or a cleaning decision is made.

For every issue, record:

1.  The affected column or records.
2.  The observed evidence.
3.  Whether the issue is confirmed or only suspected.
4.  The action taken, if any.
5.  The reason for the action.

Do not silently overwrite the original raw dataset. Keep cleaning
operations reproducible and apply them to separate working or modeling
DataFrames.
