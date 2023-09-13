from src.mlproject.logger import logging
from src.mlproject.exception import CustomException



import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        b = 1
        print(b)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)