# scripts/read_raw_data.py
import pandas as pd
from settings import Settings

def read_raw_data():
    url = Settings().get_raw_data_path()
    data = {}
    for sheet in Settings().raw_sheets:
        data[sheet] = pd.read_excel(url, sheet_name=sheet)
    return data

def raw_data_summary(raw_data):
    summary = {}
    for sheet, df in raw_data.items():
        summary[sheet] = {
            'num_rows': df.shape[0],
            'num_columns': df.shape[1],
            'columns': df.columns.tolist()
        }
    return summary

def print_raw_data_summary(summary):
    print("Raw Data Summary:")
    for sheet, info in summary.items():
        print(f"Sheet: {sheet}")
        print(f"  Number of Rows: {info['num_rows']}")
        print(f"  Number of Columns: {info['num_columns']}")
        print(f"  Columns: {info['columns']}")