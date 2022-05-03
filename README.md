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

Key objectives of this project are:

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
2. Preparing time series data for analysis.
3. Building an `autoregression` model.
4. Improving a model by tuning its hyperparameters.

* **SITUATION**: `Forecast` hourly PM 2.5 reading for Nairobi based on data collected from sensors
* **TASK**: Formulate ML solution, Python Programming, Wrangle `NoSQL data` from MongoDB, Prepare for timeseries analysis,
* **ML APPROACH**: Autoregression (AR)/`ARIMA Modeling`, `Walk-Forward Validation`, `Hyperparameter Tuning`, Visualization with Plotly Express
* **RESULT**: `Mean Absolute Error` in final predictions was brought down from 3.89 to at Baseline to 1.96 on test data. ARMA model, although resource intesive, performed much better than vanilla Linear Regression
---------------------------------------------------------------------------------------------------------

## [4. Earthquake Damage in Nepal](https://github.com/BearsOnMars/Data-Science-Projects/tree/main/4.%20Earthquake%20Damage%20in%20Nepal)
**This project involves building a `Classification model` to predict building damage from the Nepal 2015 Earthquake using data from Open Data Nepal.**

**Key Objectives of Project:**
1. Getting data by `querying a SQL database`. Exploring SQL commands e.g.(`SELECT`, `LIMIT`, `COUNT`, `JOIN` etc.)
2. Building a `logistic regression model` for `classification`
3. Building a `decision tree model` for classification
4. Incorporating `ethical considerations` into model building


* **SITUATION**: `Predict` building damage by the 2015 Earthquake in Nepal's Gorkha district.
* **TASK**: Formulate ML Solution, `Query SQL database`, `Sqlite` to import data to Python, `Docstrings`, Drop `Leaky Features`, `Binary Classfication`, Explore `Majority/Minority Classes`, `Pivot Tables`, examine `Multicollinearity`, `Randomised Train-Test Split`, `Validation set`, 
* **ML APPROACH**: `Logistic Regression`, `Extracting Feature Importances`, `Odds Ratios`, `Decision Tree Classifier`, `Ordinal Encoder`, `Hyperparameter Tuning`, `Accuracy Score`, `Gini Importance`, Plotting Tree Model
* **RESULT**: A building superstructure made of brick/cement mortar reduced the likelihood of severe damage by 75%. Whereas a superstructure of stone made a building 400% more likely to have suffered severe damage in earthquake. Superstructure as a feature was found to be reponsible for over 60% increase/decrease in impurity in Decision Tree splits from root to leaves. Inn the demographic analysis, it was observed how a model trained on biased data could end up perpetuating systems of social injustice and exacerbate problems.
---------------------------------------------------------------------------------------------------------
