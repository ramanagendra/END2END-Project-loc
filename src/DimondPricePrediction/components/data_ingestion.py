
import pandas as pd
import numpy as np

import os
import sys
from src.DimondPricePrediction.logger import logging


from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifects","raw.csv")
    train_data_path:str= os.path.join("artifects", "train.csv")
    test_data_path:str=os.path.join("artifects","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_conf=DataIngestionConfig()

    def initiate_data_inestion(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info(" i have read a data set as data")

            os.makedirs(os.diname((os.path.join(self.ingestion_conf.raw_data_path)),exist_ok=True))
            data.to_csv(self.ingestion_conf.raw_data_path, index=False)
            logging.info("I ahve saved the raw data into artifect folder")

            logging.info("here i have performed train test split")
            train_test_split(data, test_size=0.25)
            logging.info("train test splitcompleted")

            "train".to_csv(self.ingestion_conf.tarin_data_path,index=False)
            "test".to_csv(self.ingestion_conf.test_data_path, index=False)

            logging.info("Data Ingestion part completed")


        

        except Exception as e:
            logging.info("exception occurs during data ingestion stage")
            raise customexception(e,sys)