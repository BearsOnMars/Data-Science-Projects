# Importing libraries

import json
import pickle

import pandas as pd

def wrangle(filename):
    # Opening json file and loading it into dictionary
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Loading dictionary into a DataFrame and setting index as `company_id`
    df = pd.DataFrame().from_dict(data['data']).set_index('company_id')
    
    return df

def make_predictions(data_filepath, model_filepath):
    
    # Wrangling JSON file
    X_test = wrangle(data_filepath)
    
    # Loading model
    with open(model_filepath, 'rb') as f:
        model = pickle.load(f)
    
    # Generating predictions
    y_test_pred = model.predict(X_test)
    
    # Putting predictions into Series with name "bankrupt", and same index as X_test
    y_test_pred = pd.Series(y_test_pred, index = X_test.index, name = 'bankrupt')
    
    return y_test_pred