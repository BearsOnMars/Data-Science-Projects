# [Road Safety in GB](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/6.%20Road%20Safety%20in%20GB)
**In this project, `Road Safety Data - Accidents 2019` published by Department of Transport is explored. The goal is to build a model that can predict whether an accident would be fatal or not, and to identify the most important features which contribute to a fatal accident. More information on the dataset can be found on [data.gov.uk](https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data) webpage.**

**Key objectives of this Project:**

1. Explore the accidents data
2. Apply the Random Forest Classification algorithm to identify most important features which contribute to a fatal accident
3. Design a [Tableau Dashboard](https://public.tableau.com/app/profile/anuj.kumar8584/viz/RoadSafety2019/RoadSafety2019). Click on the link to access it.


* **SITUATION**: `Predict` whether an accident on British Roads is fatal or not and identify key attributes.
* **TASK**: Formulate ML Solution, Exploratory Data Analysis, `Positive/Negative Class`, Resample data (`Under-/Over-Sampling`)
* **ML APPROACH**: `Ensemble Model`, `Random forest Classifier`, `Confusion Matrix`, `CrossValidation`, `Hyperparameter Grid Search`, `Accuracy Score`
* **RESULT**: Random Forest Model failed to predict effectively whether an acident was fatal or not. Perhaps another ML Classification Model would be a better fit. The number of False Negatives was very high. However, we still were able to identify the Key Features which are most often associated with Fatal Accidents. Therein lies the utility of this model.
