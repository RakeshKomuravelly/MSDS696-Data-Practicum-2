# MSDS696-Data-Practicum-2

# Air Quality Forecasting Project

## Project Overview
This project aims to develop a data-driven system for forecasting daily air quality (PM2.5 concentration) across multiple cities using machine learning models. By leveraging historical air quality data, meteorological forecasts, and geospatial information, the project predicts PM2.5 levels to support public health management, environmental policy-making, and urban planning.

The final model uses **XGBoost Regressor** with a preprocessing pipeline and optional feature engineering for enhanced prediction performance.

---

## Data Sources

### 1. Historical Air Quality Data (PM2.5)
- **Source:** European Environment Agency (EEA) and U.S. Environmental Protection Agency (USEPA)  
- **Content:** Daily PM2.5 concentration data collected from monitoring stations across Europe and the U.S. This data serves as the primary target variable and historical baseline for training models.  
- **Links:**  
  - [EEA](https://www.eea.europa.eu)  
  - [USEPA](https://www.epa.gov/outdoor-air-quality-data)

---

### 2. Meteorological Forecast Data
- **Source:** Open-Meteo API  
- **Content:** Daily weather parameters including temperature, humidity, wind speed, and precipitation. These serve as predictive features that influence pollution dispersion and formation.  
- **Link:** [Open-Meteo](https://open-meteo.com/)

---

## Project Components

1. **Data Preprocessing**
   - Handling missing values and log transformations of skewed variables.
   - Encoding categorical variables (e.g., city names) using `OneHotEncoder`.
   - Scaling numeric features (optional, depending on the model).

2. **Feature Engineering**
   - Addition of temporal features such as month, day-of-week.
   - (Optional) Lag features for previous days’ PM2.5 values.

3. **Modeling**
   - RandomForest Regressor (baseline)
   - Gradient Boosting Regressor (intermediate)
   - XGBoost Regressor (final model with pipeline)

4. **Evaluation**
   - Metrics: RMSE, R² Score, MAE.
   - Cross-validation and hyperparameter tuning for improved performance.

5. **Deployment**
   - Interactive dashboard using Streamlit.
   - Model saved with `joblib` for fast predictions.

---

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/RakeshKomuravelly/MSDS696-Data-Practicum-2
```
---

### 1. Create and Activate the Virtual Environment

Its highly recommended to use a **virtual environment** (`airquailty_env`) to manage the project dependencies (like Streamlit, XGBoost, and Scikit-learn) and prevent conflicts with other Python projects.

1.  **Create the environment:**
    ```bash
    python -m venv airquailty_env
    ```

2.  **Activate the environment:**
    ```bash
    # For Windows:
    airquailty_env\Scripts\activate

    # For Linux/macOS:
    source airquailty_env/bin/activate
    ```

3.  **Install dependencies:**
    Install all required packages listed in the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

---

### 2. Run the Streamlit Dashboard

Once the environment is active and all dependencies are installed, you can launch the application.

```bash
streamlit run app.py
