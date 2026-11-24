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

## Environment Setup
_Dependencies_
requires-python = ">=3.10"
dependencies = [
    "numpy>=2.2.6",
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
