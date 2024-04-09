
import pandas as pd
from pymongo import MongoClient
iris_data = pd.read_csv("C:\\PROGRAMS 2021-22\\Python\\MongoDb\\iris.csv")
client = MongoClient('mongodb://localhost:27017/')
db = client['iris_database']
collection = db['iris_collection']
data_dict = iris_data.to_dict(orient='records')
collection.insert_many(data_dict)
print("Data inserted successfully into MongoDB.")

'''



client = MongoClient('mongodb://localhost:27017/')
db = client['iris_database']
collection = db['iris_collection']


cursor = collection.find()

for index, document in enumerate(cursor, start=1):
    row_sum = document['sepal_length']+document['sepal_width']+document['petal_length']+document['petal_width']
    print(f"r{index}-sum: {row_sum}")
'''