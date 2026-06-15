## Here we create custom functions that could be used across the project parts
import os
import sys
import numpy as np
import pandas as pd
import dill ## This is also used to store an object as a pickle file

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)



