<img src="./src/assets/snare.png" width="200" />

Welcome to the snare student evaluator. This tool has been trained on a dataset of students which consists of their academic performance, extracirricular activities, and academic/parental support systems.

---

For this solution, we employed the use of 4 different classification models: **Logistic Regression**, **Random Forest**, **XGBoost**, and a deep leraning model with the **CORAL** method. The models were trained on the training dataset and evaluated on the validation dataset, and the best model was selected based on the evaluation metrics.

# Development

This project uses [Poetry](https://python-poetry.org/) for dependency management and [Dash](https://dash.plotly.com/) for the web application framework.

1. First, install poetry:

Linux, macOS, Windows (WSL)
```
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (Powershell)
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
2. `poetry install` to install defined dependencies
3. `python src/snare.py` or `poetry run python src/snare.py` to run dash app on `0.0.0.0:8050`
