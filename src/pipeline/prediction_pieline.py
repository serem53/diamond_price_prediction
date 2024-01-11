import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logging import logging  
from src.utils.utils import load_object

class PredictPipeline:
    
    def __init__(self):
        print("init... the object")
     
     #feature = data
    def predict(self,feature):
        try:
            preprocessor_path = os.path.join("artificats","preproceesor.pkl")
            model.pkl = os.path.join("artificats","model.pkl")

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            scaled_feature = preprocessor.transform(feature)

            prediction = model.predict(scaled_feature)

            return prediction
        except Exception as e:
            raise customexception(e,sys)


class CustomData:
    def __init__(self):
        pass

    def get_data+as_dataframe(self):
        pass


