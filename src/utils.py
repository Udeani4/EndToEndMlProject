## Here we create custom functions that could be used across the project parts
import os
import sys
import numpy as np
import pandas as pd
import dill ## This is also used to store an object as a pickle file
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        training_report = {}
        test_report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            param=params[list(models.keys())[i]]

            grid=GridSearchCV(model,param_grid=param,cv=3,error_score='raise')
            grid.fit(X_train,y_train)

            model.set_params(**grid.best_params_) ## this will unpack the best_params_ dictionary into keyword arguements. It will now set that param as the parameters in the model
            model.fit(X_train,y_train) ## This s now the model with the best parameters we are training

            ## Another more direct way once the grid search is done fitting..
            # best_model = grid.best_estimator_
            # y_pred = best_model.predict(X_test)
            ## The above is a more generic approach

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            training_report[list(models.keys())[i]]=train_model_score

            test_report[list(models.keys())[i]]=test_model_score

        return training_report, test_report
    
    except Exception as e:
        raise CustomException(e,sys)

def load_object(file_path): 
    '''Responsible for loading the pickle file'''
    try:
        with open(file_path,'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e,sys)