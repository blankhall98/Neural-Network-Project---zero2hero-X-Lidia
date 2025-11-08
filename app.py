# app.py

## Import necessary modules
from settings import Settings
from scripts.read_raw_data import read_raw_data, raw_data_summary, print_raw_data_summary

## Initialize Settings
settings = Settings()

## 01. Read Raw Data
### Raw Data is a dictionary, each key is a sheet
raw_data = read_raw_data()

### Primer Proyecto
#print(raw_data["1er proyecto"].head())

### Segundo Proyecto
#print(raw_data["proyecto 2"].head())

### Raw data summary
summary = raw_data_summary(raw_data)
print_raw_data_summary(summary)
