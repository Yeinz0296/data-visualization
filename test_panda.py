import pandas as pd
from datetime import date

dataframe = pd.read_csv("dataset_september.csv")
timestamp = dataframe['Timestamp']
dataframe['Dates'] = pd.to_datetime(timestamp).dt.date
dataframe['Time'] = pd.to_datetime(timestamp).dt.time

date_specify = (dataframe['Dates']>=date(2022,9,1)) & (dataframe['Dates']<=date(2022,9,2))

print(dataframe['Timestamp'].max())