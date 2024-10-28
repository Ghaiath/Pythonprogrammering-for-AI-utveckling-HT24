# Health Insurance Cost Prediction

This project uses predictive analytics to estimate healthcare costs for insurance customers based on demographic and lifestyle data. Developed in Python, it leverages a machine learning model to provide actionable insights, helping health insurance companies better understand cost determinants and allowing users to anticipate their healthcare expenses.

## Dataset

The primary dataset, `insurance.csv`, includes various features on insured individuals. After training a model on this data, predictions can be validated with a separate `validation_dataset.csv`, which excludes the cost column (`charges`).

### insurance.csv - Column Descriptions

| Column     | Data Type | Description                                                                  |
|------------|-----------|------------------------------------------------------------------------------|
| `age`      | int       | Age of the primary beneficiary.                                              |
| `sex`      | object    | Gender of the insurance contractor (male or female).                         |
| `bmi`      | float     | Body mass index, a standard measure of body fat based on height and weight.  |
| `children` | int       | Number of dependents covered by the insurance plan.                          |
| `smoker`   | object    | Indicates if the beneficiary smokes (yes or no).                             |
| `region`   | object    | The beneficiary's residential area in the U.S. (e.g., northwest, southeast). |
| `charges`  | float     | Individual medical costs billed by health insurance.                         |

## Project Structure

The notebook is organized as follows:
1. **Data Import & Cleaning:** Loads and preprocesses `insurance.csv`.
2. **Exploratory Data Analysis (EDA):** Investigates relationships between features and insurance charges.
3. **Modeling:** Builds a machine learning model to predict healthcare costs.
4. **Validation:** Applies the model to the `validation_dataset.csv` for testing.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `scikit-learn`

Install dependencies:
```bash
pip install pandas numpy scikit-learn
```

### Running the Project
1. Open the Jupyter notebook.
2. Run each cell in sequence to load data, explore, and build the predictive model.
3. Apply the trained model to the validation dataset to generate predictions.

## Future Work
- Improve model accuracy by experimenting with different algorithms.
- Tune hyperparameters for better predictive performance.
- Explore feature engineering and scaling techniques.