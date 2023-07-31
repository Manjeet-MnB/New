from Insurance.logger import logging
from Insurance.exception import InsuranceException
import sys, os
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity

'''def test_logger_and_expection():
    try:
        logging.info("Starting the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Stoping the test_logger_and_exception")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)'''
    

if __name__ == "__main__":
    try:
        traning_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_conig = config_entity.DataIngestionConfig(traning_pipeline_config = traning_pipeline_config)
        print(data_ingestion_conig.to_dict())
        #get_collection_as_dataframe(database_name = "INSURANCE",collection_name = "INSURANCE_PROJECT")
    except Exception as e:
        print(e)    