# Predicting Toxicity of Agrochemicals to Honey Bees 🧪🐝
# che1147-bees 

## Data Source
**ApisTox: a new benchmark dataset for the classification of small molecules toxicity on honey bees**
*Jakub Adamczyk, Jakub Poziemski & Pawel Siedlecki*
[(Nature, 2025)](https://www.nature.com/articles/s41597-024-04232-w)

## Project Description
Our project reproduces and builds upon previous work using machine learning (ML) models to
classify toxicity of agrochemicals to bees. Machine learning (ML) models have been applied for
binary classification on the ApisTox dataset.[(Adamczyk, 2026)](https://www.sciencedirect.com/science/article/pii/S0147651326001983#sec4) Our analysis draws inspiration from this article, as we
train and evaluate ternary classification models for the same dataset. Random forest, kernel SVC and XGBoost were trained on three splits of the dataset to evaluate model performance on simple and more realistic and challenging tasks.

## Final Code

The 'final-analysis.ipynb' on the main branch contains commented code with initial eda, data cleaning, featurization, model training, hyperparameter tuning and metric computation. The 'eda.ipynb' file contains some eda which is included in the 'final-analysis.ipynb' file, as well as code for generating the UMAP projections seen in the report appendix and on the poster.

## Environment Setup

If uv is installed, a virtual environment with dependencies installed can be created by running the 'uv sync' command in the VSCode terminal. This should create a jupyter kernel titled 'bee-tox'.

_Dependency information from .toml file_
requires-python = ">=3.10"
dependencies = [
    "bokeh>=3.9.2",
    "datashader>=0.19.1",
    "holoviews>=1.23.2",
    "ipykernel>=7.3.0",
    "numba>=0.68.1",
    "numpy>=2.2.6",
    "umap-learn>=0.6.0",
]

[build-system]
requires = ["uv_build>=0.12.17,<0.13.0"]
build-backend = "uv_build"

[dependency-groups]
dev = [
    "matplotlib>=3.10.9",
    "pandas>=2.3.3",
    "rdkit>=2026.9.2",
    "scikit-learn>=1.7.2",
    "seaborn>=0.13.2",
    "xgboost>=3.2.0",
]
