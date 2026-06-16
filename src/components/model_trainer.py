## We will train with different models and derive the accuracy score

import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

## NOTE: for every component we want tot work on eg data_transformation, data_ingestion and now model_trainer, We have to create a configurations file 


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Slitting Training and Test impute data')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],## all rows and columns exept the last column
                train_array[:,-1], ## all row and the last column
                test_array[:,:-1],
                test_array[:,-1]
            )

            # create a dictionary of models
            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'K-Neighbors Classifier': KNeighborsRegressor(),
                'XGBClassifier': XGBRegressor(),
                'CatBoosting Classifier': CatBoostRegressor(verbose=False),
                'AdaBoost Classifier': AdaBoostRegressor()
            }

            train_model_report:dict
            test_model_report:dict
            
            train_model_report,test_model_report=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models) ## we created the evaluate_model function in utils.py

            ## To get best model score from dict
            best_test_model_score=max(sorted(test_model_report.values()))

            ## get the best model 
            best_test_model_name=list(test_model_report.keys())[
                list(test_model_report.values()).index(best_test_model_score)
            ]

            best_test_model = models[best_test_model_name]

            if best_test_model_score<0.6:
                raise CustomException('No best model found')
            
            logging.info(f'Best found model on borth training and testing dataset')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_test_model
            ) ## saved the model object as a pickle file

            y_pred=best_test_model.predict(X_test)
            r2_square=r2_score(y_test, y_pred)

            return r2_square


        except Exception as e:
            raise CustomException(e,sys)