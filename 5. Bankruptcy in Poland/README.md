# 5. Bankruptcy in Poland
**In this project, data collected by a team of Polish economists studying bankruptcy is explored. The goal is to build a model that can predict whether a company will go bankrupt or not. More information on the dataset can be found on [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data) webpage.**
**KEY objectives of Project:**
1. Navigating a file system from the Linux command line
2. Loading and saving files using Python
3. Addressing imbalanced data using resampling techniques
4. Evaluating a model using classification metrics like precision and recall


* **SITUATION**: `Predict` whether a company will go bankrupt or not.
* **TASK**: Formulate ML Solution, `Command Line` and `Context Handler` to decompress `.gz file`, Read-Explore-Inspect data from `JSON`file, `Positive/Negative Class`, Resample data (`Under-/Over-Sampling`), Save to, and Load model from `.pkl` Pickle file
* **ML APPROACH**: `Ensemble Model`, `Random forest Classifier`, `Gradient Boosting`, `Confusion Matrix`, `CrossValidation`, `Hyperparameter Grid Search`, `Accuracy Score`, `Recall Score`, `Precision Score`, `Classification Report`, `Predictor Module`
* **RESULT**: Random Forest Model and Gradient Boosting delivered better performance than a single Decision tree predictor. It was observed that a Confusion Matrix provided more information on model performance than Accuracy Score. Furthermore, Precision Score and Recall Score were seen to be immensely useful depending on the purpose of model: if more confidence in predictions is sought, it was better to focus on Precision Score; if it is imperative to identify all potential positive classes then focus must be on Recall Score.
