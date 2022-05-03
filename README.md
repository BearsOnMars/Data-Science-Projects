# Data Science Projects

## 1. Housing in Mexico
**In this project, a dataset with 21,000 properties for sale in Mexico is analysed to determine whether sale prices are influenced more by property size or location.**

**Key objectives of this project are:**

1. Organising information using Python data structures.
2. Importing data from CSV files and cleaning it using the pandas library.
3. Creating data visualizations such as scatter and box plots.
4. Examining the relationship between two variables using correlation.

* **SITUATION**: Analyse and describe which of the two factors influence House Prices in Mexico more: Location or House Size
* **TASK**: Python Programming, Prepare and Clean Data, Perform Exploratory Data Analysis (EDA), Create Visualisations for in-depth analysis
* **APPROACH**: Data Wrangling with Pandas library in Python, Matplotlib and Plotly Express libraries for visualising data
* **RESULT**: It was discovered that house prices per sq.m (i.e. size) is a more realistic representation of housing prices than location
---------------------------------------------------------------------------------------------------------

## 2. Housing in Buenos Aires
**This project involves creating a Machine Learning Linear Regression model that predicts apartment prices in Buenos Aires, Argentina -- with a focus on apartments that cost less than $400,000. The model examines how Apartment Size, Location and Neighbourhood influence prices**

Key objectives of this project are:

1. Creating a linear regression model using the scikit-learn library.
2. Building a data pipeline for imputing missing values and encoding categorical features.
3. Improving model performance by reducing overfitting.
4. Creating a dynamic dashboard for interacting with completed model.

* **SITUATION**: Forecast Apartment Prices in Buenos Aires, Argentina for apartments that cost less than $400,000
* **TASK**: Formulate ML solution, Python Programming, Wrangle data from .csv file, Prepare Data, Build-Iterate-Evaluate Model, Impute missing values
* **ML APPROACH**: Linear Regression Modeling, OneHotEncoding categorical data, deploying Prediction Function and an interactive dashboard for a Minimum Viable Product (MVP)
* **RESULT**: Neighbourhood is much stronger influence in apartment prices than size. The posher the neighbourhood, the higher the apartment price.
---------------------------------------------------------------------------------------------------------

## 3. Air Quality in Nairobi
**In this project, data is pulled from Africa's largest open data platforms openAfrica. Air quality data is analysed from Nairobi, Lagos, and Dar es Salaam; and a time-series model is built to predict PM2.5 readings throughout the day. More information on PM2.5 and its effects on respiratory system can be found on [Taskforce for Lung Health's webpage.](https://www.blf.org.uk/taskforce/data-tracker/air-quality/pm25)**

**Key Big-Picture Objectives of this project are:**

1. Getting data by querying a MongoDB database.
2. Preparing time series data for analysis.
3. Building an autoregression model.
4. Improving a model by tuning its hyperparameters.

* **SITUATION**: Forecast hourly PM 2.5 reading for Nairobi based on data collected from sensors
* **TASK**: Formulate ML solution, Python Programming, Wrangle NoSQL data from MongoDB, Prepare for timeseries analysis,
* **ML APPROACH**: Autoregression (AR)/ARIMA Modeling, Walk-Forward Validation, Hyperparameter Tuning, Visualization with Plotly Express
* **RESULT**: Mean Absolute Error in final predictions was brought down from 3.89 to at Baseline to 1.96 on test data. ARMA model, although resource intesive, performed much better than vanilla Linear Regression
---------------------------------------------------------------------------------------------------------
