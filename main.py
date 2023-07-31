from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
import sys, os
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation
#from Insurance.components.data_transformation import DataTransformation
#from Insurance.components.model_trainer import ModelTrainer
#from Insurance.components.model_evaluation import ModelEvaluation
#from Insurance.components.model_pusher import ModelPusher

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
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_conig)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=traning_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        #data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()
    except Exception as e:
        print(e)    