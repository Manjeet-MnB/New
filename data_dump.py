import pandas as pd
import json
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ManjetBilthare:ManjeetBilthare@cluster0.qf43oqf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

DATA_FILE_PATH = (r"C:\Users\MANJEET\OneDrive\Documents\newProject\New\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)