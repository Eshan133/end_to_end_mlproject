import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


'''
read dataset -> store into `data.csv` file -> train test split -> store into `train.csv`, `test.csv` -> return the path for those 2 .csv files
'''

@dataclass  # to define class variable without the use of __init__
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")  
    test_data_path: str = os.path.join('artifacts', "test.csv")  
    raw_data_path: str = os.path.join('artifacts', "data.csv")  

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        # to read data from the database, for this project we read from the local
        logging.info("Entered the data ingestion method")
        try:

            df = pd.read_csv('notebook\data\stud.csv')  # Reading from the dataset, can be done from any data source
            logging.info('Imported and Read the dataset as dataframe')
            
            # Making the directory(artifacts)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Ingesting the imported data to 'data.csv'
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            

            logging.info("Train Test Split Initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            

            # Ingesting the train_set and test_set into `train.csv` and `test.csv`'
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)


            logging.info("Ingestion Completed")

            # SO that data_transformation can use this path to transform the data available
            return(
                self.ingestion_config.train_data_path,  
                self.ingestion_config.test_data_path,
            )
        
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
