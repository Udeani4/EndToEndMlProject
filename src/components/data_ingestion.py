## We will read te data here
## We will start with the local data, later we will learn to read from remote database like hadoop, mongodb etc

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ## This is usually used to creete class variables

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig



## We need a way to store inputs that come from the ...

## Normally inside the class, to define a class variable you will use init. But this @dataclass decorator hels you do that directly

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv') # This is where all taining data will be saved. Later on the the train.csv will be saved in this particular path
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv') 

    ## All these files will be saved in the artifacts folder

## NOTE: If you are just defining varables you can use the decorator @dataclass but you have some other functions within the class it is suggested you use the __init__() constructor

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() ## This will consist of those three variables defined in the DataIngestionConfig class 

    def initiate_data_ingestion(self): ## We us this to read the dataset in a very easy way (this is just for simplicity, for now)
        logging.info('Enter the data ingestion method or component')

        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')
            # create the artifact folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) ## Try to understand this code

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

        
if __name__=="__main__":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path,test_data_path)


## you can now execute in your terminal (python src/compomnents/data_ingestion.py)