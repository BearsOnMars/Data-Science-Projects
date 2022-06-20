# Data Science Projects

## [1. Housing in Mexico](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/1.%20Housing%20in%20Mexico)
**In this project, a dataset with 21,000 properties for sale in Mexico is analysed to determine whether sale prices are influenced more by property size or location.**

**Key objectives of this project are:**

1. Organising information using Python data structures.
2. Importing data from CSV files and cleaning it using the pandas library.
3. Creating data visualizations such as scatter and box plots.
4. Examining the relationship between two variables using `correlation`.

* **SITUATION**: Analyse and describe which of the two factors influence House Prices in Mexico more: Location or House Size
* **TASK**: Python Programming, Prepare and Clean Data, Perform `Exploratory Data Analysis (EDA)`, Create `Visualisations` for in-depth analysis
* **APPROACH**: Data Wrangling with `Pandas` library in Python, `Matplotlib` and `Plotly Express` libraries for visualising data
* **RESULT**: It was discovered that house prices per sq.m (i.e. size) is a more realistic representation of housing prices than location
---------------------------------------------------------------------------------------------------------

## [2. Housing in Buenos Aires](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/2.%20Housing%20in%20Buenos%20Aires)
**This project involves creating a `Machine Learning Linear Regression` model that `predicts` apartment prices in Buenos Aires, Argentina -- with a focus on apartments that cost less than $400,000. The model examines how Apartment Size, Location and Neighbourhood influence prices**

**Key objectives of this project are:**

1. Creating a linear regression model using the `scikit-learn library`.
2. Building a data pipeline for `imputing missing values` and `encoding categorical features`.
3. Improving model performance by `reducing overfitting`.
4. Creating a dynamic dashboard for `interacting` with completed model.

* **SITUATION**: Forecast Apartment Prices in Buenos Aires, Argentina for apartments that cost less than $400,000
* **TASK**: Formulate ML solution, Python Programming, Wrangle data from .csv file, Prepare Data, Build-Iterate-Evaluate Model, Impute missing values
* **ML APPROACH**: Linear Regression Modeling, `OneHotEncoding` categorical data, deploying Prediction Function and an interactive dashboard for a `Minimum Viable Product (MVP)`
* **RESULT**: Neighbourhood is much stronger influence in apartment prices than size. The posher the neighbourhood, the higher the apartment price.
---------------------------------------------------------------------------------------------------------

## [3. Air Quality in Nairobi](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/3.%20Air%20Quality%20in%20Nairobi)
**In this project, data is pulled from Africa's largest open data platforms openAfrica. Air quality data is analysed from Nairobi, Lagos, and Dar es Salaam; and a `time-series model is built to predict` PM2.5 readings throughout the day. More information on PM2.5 and its effects on respiratory system can be found on [Taskforce for Lung Health's webpage.](https://www.blf.org.uk/taskforce/data-tracker/air-quality/pm25)**

**Key Big-Picture Objectives of this project are:**

1. Getting data by `querying a MongoDB database`.
2. Preparing timeseries data for analysis.
3. Building an `autoregression` model.
4. Improving a model by tuning its hyperparameters.

* **SITUATION**: `Forecast` hourly PM 2.5 reading for Nairobi based on data collected from sensors
* **TASK**: Formulate ML solution, Python Programming, Wrangle `NoSQL data` from MongoDB, Prepare for timeseries analysis,
* **ML APPROACH**: Autoregression (AR)/`ARIMA Modeling`, `Walk-Forward Validation`, `Hyperparameter Tuning`, Visualization with Plotly Express
* **RESULT**: `Mean Absolute Error` in final predictions was brought down from 3.89 to at Baseline to 1.96 on test data. ARMA model, although resource intesive, performed much better than vanilla Linear Regression
---------------------------------------------------------------------------------------------------------

## [4. Earthquake Damage in Nepal](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/4.%20Earthquake%20Damage%20in%20Nepal)
**This project involves building a `Classification model` to predict building damage from the Nepal 2015 Earthquake using data from Open Data Nepal.**

**Key Objectives of this Project:**

1. Getting data by `querying a SQL database`. Exploring SQL commands e.g.(`SELECT`, `LIMIT`, `COUNT`, `JOIN` etc.)
2. Building a `logistic regression model` for `classification`
3. Building a `decision tree model` for classification
4. Incorporating `ethical considerations` into model building


* **SITUATION**: `Predict` building damage by the 2015 Earthquake in Nepal's Gorkha district.
* **TASK**: Formulate ML Solution, `Query SQL database`, `Sqlite` to import data to Python, `Docstrings`, Drop `Leaky Features`, `Binary Classfication`, Explore `Majority/Minority Classes`, `Pivot Tables`, examine `Multicollinearity`, `Randomised Train-Test Split`, `Validation set`, 
* **ML APPROACH**: `Logistic Regression`, `Extracting Feature Importances`, `Odds Ratios`, `Decision Tree Classifier`, `Ordinal Encoder`, `Hyperparameter Tuning`, `Accuracy Score`, `Gini Importance`, Plotting Tree Model
* **RESULT**: A building superstructure made of brick/cement mortar reduced the likelihood of severe damage by 75%. Whereas a superstructure of stone made a building 400% more likely to have suffered severe damage in earthquake. Superstructure as a feature was found to be reponsible for over 60% increase/decrease in impurity in Decision Tree splits from root to leaves. Inn the demographic analysis, it was observed how a model trained on biased data could end up perpetuating systems of social injustice and exacerbate problems.
---------------------------------------------------------------------------------------------------------
## [5. Bankruptcy in Poland](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/5.%20Bankruptcy%20in%20Poland)
**In this project, data collected by a team of Polish economists studying bankruptcy is explored. The goal is to build a model that can predict whether a company will go bankrupt or not. More information on the dataset can be found on [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data) webpage.**

**Key objectives of this Project:**

1. Navigating a file system from the Linux command line
2. Loading and saving files using Python
3. Addressing imbalanced data using resampling techniques
4. Evaluating a model using classification metrics like precision and recall


* **SITUATION**: `Predict` whether a company will go bankrupt or not.
* **TASK**: Formulate ML Solution, `Command Line` and `Context Handler` to decompress `.gz file`, Read-Explore-Inspect data from `JSON`file, `Positive/Negative Class`, Resample data (`Under-/Over-Sampling`), Save to, and Load model from `.pkl` Pickle file
* **ML APPROACH**: `Ensemble Model`, `Random forest Classifier`, `Gradient Boosting`, `Confusion Matrix`, `CrossValidation`, `Hyperparameter Grid Search`, `Accuracy Score`, `Recall Score`, `Precision Score`, `Classification Report`, `Predictor Module`
* **RESULT**: Random Forest Model and Gradient Boosting delivered better performance than a single Decision tree predictor. It was observed that a Confusion Matrix provided more information on model performance than Accuracy Score. Furthermore, Precision Score and Recall Score were seen to be immensely useful depending on the purpose of model: if more confidence in predictions is sought, it was better to focus on Precision Score; if it is imperative to identify all potential positive classes then focus must be on Recall Score.

---------------------------------------------------------------------------------------------------------
## [6. Road Safety in GB](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/6.%20Road%20Safety%20in%20GB)
**In this project, `Road Safety Data - Accidents 2019` published by Department of Transport is explored. The goal is to build a model that can predict whether an accident would be fatal or not, and to identify the most important features which contribute to a fatal accident. More information on the dataset can be found on [data.gov.uk](https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data) webpage.**

**Key objectives of this Project:**

1. Explore the accidents data
2. Apply the Random Forest Classification algorithm to identify most important features which contribute to a fatal accident
3. Design a [Tableau Dashboard](https://public.tableau.com/app/profile/anuj.kumar8584/viz/RoadSafety2019/RoadSafety2019).


* **SITUATION**: `Predict` whether an accident on British Roads is fatal or not and identify key attributes.
* **TASK**: Formulate ML Solution, Exploratory Data Analysis, `Positive/Negative Class`, Resample data (`Under-/Over-Sampling`)
* **ML APPROACH**: `Ensemble Model`, `Random forest Classifier`, `Confusion Matrix`, `CrossValidation`, `Hyperparameter Grid Search`, `Accuracy Score`
* **RESULT**: Random Forest Model failed to predict effectively whether an acident was fatal or not. Perhaps another ML Classification Model would be a better fit. The number of False Negatives was very high. However, we still were able to identify the Key Features which are most often associated with Fatal Accidents. Therein lies the utility of this model.

--------------------------------------------------------------------------------------------------------------
## [7. Heart Attack Binary Classification](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/7.%20Heart%20Attack%20Binary%20Classification)
**In this project, Medical Health data is explored. The goal is to build a Binary Classification model that can predict whether a patient would have a heart attack or not, and to identify the most important features which contribute to a heart attack.

**Key objectives of this Project:**

1. Explore the medical data
2. Apply feature engineering, choose the appropriate ML models to train, and evaluate performance 

* **SITUATION**: `Predict` whether a patient is at a High Risk of a Heart Attack or Not.
* **TASK**: Formulate ML Solution, Exploratory Data Analysis, `Positive/Negative Class`, Feature Engineering, Evaluate Models
* **ML APPROACH**: Logistic Regression, `Ensemble Model`, `Random forest Classifier`, `Gradient Boosting Trees`, `Classification Report`, `CrossValidation`, `Hyperparameter Grid Search`, `ROC Curve, AUC`, `log_loss`
* **RESULT**: Logistic Regression Model was found to be the best performing model out of three. It had the highest AUC at 0.95 and the lowest log loss at 0.29. And above all, it took the least resources to train the data on Logistic Regression model

--------------------------------------------------------------------------------------------------------------
## [8. Household Segmentation in the US](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/8.%20Household%20Segmentation%20in%20the%20US))

In this project, data from the [Survey of Consumer Finances (SCF)](https://www.federalreserve.gov/econres/aboutscf.htm), which is sponsored by the US Federal Reserve is analysed. It tracks financial, demographic, and opinion information about families in the United States. The survey is conducted every three years. An extract of the results from 2019 is chosen for analysis. Here is the [Code Book](https://sda.berkeley.edu/sdaweb/docs/scfcomb2019/DOC/hcbkh01.htm) for the data.

* `OBJECTIVES OF THE PROJECT:`

    * Comparing characteristics across subgroups using a side-by-side bar chart.
    * Building a `k-means clustering` model.
    * Conducting feature selection for clustering based on variance.
    * Reducing high-dimensional data using `principal component analysis (PCA)`.
    * Designing, building and deploying a Dash web application.
