
import pandas as pd
import numpy as np
import os

from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path




class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_inestion(self):
        logging.info("data ingestion started")

        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","train.csv")))
            logging.info(" i have read a data set as data")

            logging.info("here i have performed train test split")
            train_test_split(data, test_size=0.25)
            logging.info("train test splitcompleted")

        

        except Exception as e:
            pass