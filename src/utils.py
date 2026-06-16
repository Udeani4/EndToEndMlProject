## Here we create custom functions that could be used across the project parts
import os
import sys
import numpy as np
import pandas as pd
import dill ## This is also used to store an object as a pickle file
from sklearn.metrics import r2_score

from src.exception import CustomException


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        training_report = {}
        test_report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]

            model.fit(X_train,y_train) #Train model

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            training_report[list(models.keys())[i]]=train_model_score
            
            test_report[list(models.keys())[i]]=test_model_score

        return training_report, test_report
    
    except Exception as e:
        raise CustomException(e,sys)

