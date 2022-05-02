#!/usr/bin/env python3
#################################################
#
# Import weather data from Everest
# https://nationalgeographic.org/earthpulse/weather/api/v1/history/combined
#
##################################################
import requests
import json
import pandas as pd
import sys
from datetime import datetime

url = 'https://nationalgeographic.org/earthpulse/weather/api/v1/history/combined'

resp = requests.get(url=url)
data = json.loads(resp.text)


####################################################
# Print the date

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("**************(", dt_string,")****************")	


### Create two dataframes
# df    => dataframe received from the website
# df2   => empty dataframe where the data from internet will be stored temporarily

df = pd.DataFrame(data["measurements"])
df2 = pd.DataFrame(columns=['timestamp', 'location', 'temperature', 'relative_humidity', 'WS_Max_h', 'wind_direction', 'pressure', 'wind_speed_sec', 'precipitation','WS_Average','SW_IN_AVG','SW_OUT_AVG','LW_IN_AVG','LW_OUT_AVG','SR50'])


### fill df2 from the inputs captured in df
l = -1
i = 0

for m in df["measurements"].items():
    l = l + 1
    for mm in m[1].items():
        df2.loc[i] = [df["timestamp"][l], mm[1]['location_id'], mm[1]['temperature'], mm[1]['relative_humidity'], mm[1]["wind_speed"], mm[1]["wind_direction"], mm[1]["pressure"], mm[1]["wind_speed_sec"],'','','','','','','']
        i = i + 1

print("New imported data: ",len(df2.index))

### load previous database
try:
    with open('./database.csv') as f:
        db = pd.read_csv(r'./database.csv',index_col=0)
        print('Rows in the db before merge: ', len(db.index))
except IOError:
    with open('database.csv', 'w+') as file:
        file.write('id,timestamp,location,temperature,relative_humidity,WS_Max,wind_direction,pressure,wind_speed_sec,precipitation,WS_Average','SW_IN_AVG','SW_OUT_AVG','LW_IN_AVG','LW_OUT_AVG','SR50')
    print('New database file created')
    db = pd.read_csv(r'./database.csv',index_col=0)

### ensure the timestamps are loaded properly
db["timestamp"] = pd.to_datetime(db["timestamp"])
df2["timestamp"] = pd.to_datetime(df2["timestamp"])

### merge df2 in db while removing the duplicate
#new_db = db.append(df2, ignore_index=True)
new_db = pd.concat([db, df2], ignore_index=True)
new_db["timestamp"] = pd.to_datetime(new_db["timestamp"])

print("DB size after combining: ", len(new_db.index))
print("Duplicate timestamp and location: ", new_db.duplicated(subset=['timestamp', 'location']).sum())

new_db = new_db.drop_duplicates()
print("Final db rows after removing duplicates: ", len(new_db.index))
#new_db = new_db.rename({'wind_speed': 'WS_Max_h'}, axis=1)

### write db to disk
new_db.to_csv('./database.csv')
print("DB written on database.csv")
