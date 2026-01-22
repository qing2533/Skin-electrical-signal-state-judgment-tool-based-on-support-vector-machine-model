# Skin-electrical-signal-state-judgment-tool-based-on-support-vector-machine-model
Built on SVM algorithm, this tool extracts features from electrodermal activity (EDA) data to identify 3 emotional states (baseline/pleasure/stress), and supports custom binary/ternary classification for personalized needs.

## Environment Requirements
### Hardware
- Processor: Intel Core i5+/AMD Ryzen 5+
- Memory: ≥8GB RAM
- Storage: ≥20GB free space (x86 architecture)

### Software
- OS: Windows 7+/macOS 10.15+/Linux (x86_64)
- Runtime: PyCharm + Python 3.12
- Dependencies: scikit-learn/pandas/numpy (install via `requirements.txt`)

## Core Workflow
1. Extract feature vectors from raw EDA CSV data
2. Preprocess features and train SVM model (retrain optional)
3. Batch predict new EDA data and output recognition results

## Custom Classification Setup
1. Place custom EDA CSV data into `data` folder
2. Modify `eda_svm.py` to replace default emotional labels
3. For binary classification: Delete the 3rd category's code/config
4. Re-run model training to apply changes

## Quick Start
### Model Training
1. Put training CSV files into `data` folder
2. Run `eda_svm.py` (model saved automatically)

### Emotion Prediction
1. Rename EDA CSV to `1.csv` and put into `han_experiment_test`
2. Run `main.py` for batch prediction
3. Check results in `result` folder

## Notes
- Refer to the user manual and demonstration video in the project for detailed guidance
- Ensure prediction data is CSV (same structure as training data)
- Avoid Chinese/special characters in file paths/names
- For binary classification: Remove the 3rd class config to prevent training errors

