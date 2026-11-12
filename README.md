# Climate & Geospatial ML

**Spatial Temperature Estimation Using Machine Learning**

## 1. Project Overview

This project investigates the use of Machine Learning to estimate air temperature based on geographical coordinates and temporal features.

It focuses on evaluating how well ML models generalize to geographically unseen locations, rather than relying only on conventional random train-test splitting.

The project explores geographical feature engineering, spatial validation, model comparison, feature importance, hyperparameter optimization, and location-level error analysis.

**Project Type:** Regression / Geospatial Machine Learning

**Main Framework:** Scikit-learn

**Programming Language:** Python

## 2. Problem Statement

Temperature varies across geographical locations and time. A model trained on observations from certain locations may perform poorly when applied to locations that were not represented during training.

This project investigates:

- How geographical coordinates and temporal features contribute to temperature estimation.
- Whether additional geographical feature transformations improve predictive performance.
- How model performance changes when training and testing locations are geographically separated.
- Which locations experience the highest and lowest prediction errors.

**Important:** This project focuses on spatial temperature estimation using location and time features. It is not a future weather forecasting system.

## 3. Dataset

**Dataset:** World Weather Repository

**Source:** [Kaggle - Global Weather Repository](https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository)

The original dataset contains:

- 170,928 observations.
- 41 original columns.
- 286 unique country-location combinations.
- Geographical coordinates (latitude and longitude).
- Temperature measurements.
- Temporal information.
- Weather conditions and additional meteorological measurements.
- Air quality indicators.

The processed dataset includes three additional spatial features:

- `abs_latitude`
- `is_northern_hemisphere`
- `is_eastern_hemisphere`

The modeling workflow excludes one extreme temperature observation identified during data quality investigation. The raw dataset remains unchanged.

## 4. Project Workflow

The project is organized into the following stages:

1. **Dataset Understanding:** Investigating the dataset structure, data types, distributions, and data quality.
2. **Geospatial EDA:** Examining geographical coverage, coordinate distributions, and location consistency.
3. **Spatial Feature Engineering:** Creating geographical features from latitude and longitude.
4. **Baseline Modeling:** Establishing an initial Random Forest regression baseline.
5. **Spatial Validation:** Evaluating generalization to geographically held-out locations.
6. **Model Improvement:** Comparing alternative models, performing feature analysis, and optimizing hyperparameters.

## 5. Spatial Validation Strategy

A key component of this project is the use of geographical group-based validation.

Instead of randomly splitting individual observations, locations are grouped using their country and location names.

The experiments include:

- `GroupShuffleSplit` for spatial train-test separation.
- `GroupKFold` with five folds for spatial cross-validation.
- Consistent training and validation groups across model comparisons.

This approach reduces geographical overlap between training and validation data.

**Limitation:** Group separation depends on the consistency of the source dataset's country and location labels. It does not guarantee that every geographically distinct physical site is perfectly identified.

## 6. Models and Experiments

The project evaluates the following regression algorithms:

- Dummy Regressor
- Random Forest Regressor
- Extra Trees Regressor
- HistGradientBoosting Regressor

Additional experiments include:

- Geographical feature transformations.
- Feature importance analysis.
- Permutation importance.
- Feature ablation experiments.
- Randomized hyperparameter search.
- Location-level error analysis.
- Residual analysis.

### Selected Final Model

The final model is an **Extra Trees Regressor** using six features:

- `latitude`
- `longitude`
- `hour_sin`
- `hour_cos`
- `day_sin`
- `day_cos`

The selected configuration retains the original Extra Trees baseline hyperparameters because hyperparameter optimization did not produce a meaningful improvement.

## 7. Final Model Results

The final model was evaluated on the spatially held-out test subset.

| Metric | Result |
|---|---:|
| MAE | 3.4102 °C |
| RMSE | 5.1357 °C |
| R² | 0.6494 |
| Training Time | 1.51 seconds |

**Test observations:** 31,337

The final model achieved an MAE of approximately 3.41 °C on the held-out spatial subset.

### Spatial Cross-Validation Results

Five-fold GroupKFold cross-validation on the training subset produced the following mean results:

| Metric | Mean CV Result |
|---|---:|
| MAE | 2.9152 °C |
| RMSE | 4.0276 °C |
| R² | 0.8119 |

The difference between cross-validation and test performance highlights the variability of model generalization across geographical locations.

**Evaluation note:** The held-out test subset was examined during model development and feature analysis. Therefore, the final test results should not be interpreted as an entirely untouched independent evaluation.

## 8. Location-Level Error Analysis

Model performance varied substantially across geographical locations.

### Best-Performing Locations

| Location | MAE |
|---|---:|
| Saint John's, Antigua and Barbuda | 0.65 °C |
| Kingstown, Saint Vincent and the Grenadines | 0.67 °C |
| Tarawa, Kiribati | 0.75 °C |
| Paramaribo, Suriname | 0.75 °C |

### Worst-Performing Locations

| Location | MAE |
|---|---:|
| Thimphu, Bhutan | 16.75 °C |
| Khartoum, Sudan | 8.59 °C |
| Addis Ababa, Ethiopia | 8.09 °C |
| Kathmandu, Nepal | 7.41 °C |
| Baghdad, Iraq | 6.89 °C |
| Ottawa, Canada | 6.49 °C |

These findings demonstrate that the model performs considerably better in some geographical locations than others.

Potential explanations include differences in local climate, elevation, and topography. These factors require further investigation and should not be treated as confirmed causes.

## 9. Visualizations

The project includes the following visualizations:

| Visualization | File |
|---|---|
| Geographical Distribution | `geographical_distribution.png` |
| Locations per Country | `locations_per_country.png` |
| Actual vs Predicted | `actual_vs_predicted.png` |
| Residual Distribution | `residual_distribution.png` |

All figures are stored in `outputs/figures/`.

## 10. Project Structure

```text
Climate_Geospatial_ML/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_dataset_understanding.ipynb
│   ├── 02_geospatial_eda.ipynb
│   ├── 03_spatial_feature_engineering.ipynb
│   ├── 04_baseline_model.ipynb
│   ├── 05_spatial_validation.ipynb
│   └── 06_model_improvement.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── train.py
│   └── evaluation.py
│
├── models/
├── outputs/
│   ├── figures/
│   └── results/
│
├── config.py
├── main.py
├── requirements.txt
├── DATA_QUALITY_LOG.md
└── README.md
```

## 11. Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## 12. Installation and Usage

### Clone the Repository

```bash
git clone https://github.com/MosabOs/climate-geospatial-ml.git

cd climate-geospatial-ml
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Prepare the Dataset

Download the Global Weather Repository dataset from Kaggle and place the original CSV file in:

```text
data/raw/GlobalWeatherRepository.csv
```

### Run the Notebooks

Launch Jupyter:

```bash
jupyter notebook
```

Execute the notebooks in numerical order, beginning with dataset understanding.

## 13. Limitations and Future Improvements

Current limitations:

- Geographical coverage is uneven across locations.
- Country and location naming inconsistencies may affect geographical grouping.
- The current feature set does not include elevation or detailed topographical information.
- Model performance varies significantly across geographical locations.
- The final held-out test subset was used during development and is not completely untouched.

Potential future improvements:

- Integrating elevation and topographical datasets.
- Incorporating climate zone information.
- Investigating additional geographical and meteorological predictors.
- Performing repeated spatial cross-validation.
- Evaluating the model on a new, untouched geographical test set.
- Developing a prediction interface for interactive experimentation.

## 14. Author

**Mosab Osman**


GitHub: [MosabOs](https://github.com/MosabOs)

