from google.cloud import bigquery
import os
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/user/Desktop/credentials.json"

client = bigquery.Client()
dataset_ref = client.dataset("iowa_liquor_sales", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)
table_ref = dataset_ref.table("sales")
table = client.get_table(table_ref)

df = client.list_rows(table=table, max_results=1000).to_dataframe()
print(df.head(20))
print(df.describe())
print(df.columns.tolist())
df.volume_sold_gallons = df.volume_sold_gallons.astype('float64')
df.to_csv("C:/Users/user/Desktop/data.csv", sep=';')


#tables = list(client.list_tables(dataset))

#for table in tables:
#   print(table.table_id)




