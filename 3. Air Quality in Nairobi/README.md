**In this project, data is pulled from Africa's largest open data platforms openAfrica. Air quality data is analysed from Nairobi, Lagos, and Dar es Salaam; and a time-series model is built to predict PM 2.5 readings throughout the day**

**Key Big-Picture Objectives of this project are:**

1. Getting data by querying a MongoDB database.
2. Preparing time series data for analysis.
3. Building an autoregression model.
4. Improving a model by tuning its hyperparameters.
---------------------------------------------------------------------------------------------------------
* **SITUATION**: Forecast hourly PM 2.5 reading for Nairobi based on data collected from sensors
* **TASK**: Formulate ML solution, Python Programming, Wrangle NoSQL data from MongoDB, Prepare for timeseries analysis,
* **ML APPROACH**: Autoregression (AR)/ARIMA Modeling, Walk-Forward Validation, Hyperparameter Tuning, Visualization with Plotly Express
* **RESULT**: Mean Absolute Error in final predictions was brought down from 3.89 to at Baseline to 1.96 on test data. ARMA model, although resource intesive, performed much better than vanilla Linear Regression
