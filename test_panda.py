from time import sleep
import pandas as pd
from datetime import date

fake_humid =[]
dataframe = pd.read_csv("dataset_september.csv")
timestamp = dataframe['Timestamp']
dataframe['Dates'] = pd.to_datetime(timestamp).dt.date
dataframe['Time'] = pd.to_datetime(timestamp).dt.time

date_specify = (dataframe['Dates']>=date(2022,9,1)) & (dataframe['Dates']<=date(2022,9,2))

print(dataframe.loc[date_specify])

# for index, row in dataframe.loc[date_specify].iterrows():
#         fake_humid.append(row['Humidity'])

# pd.DataFrame(fake_humid).to_csv('fake_data.csv',index=False)
