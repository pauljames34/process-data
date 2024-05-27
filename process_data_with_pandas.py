from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta

# Specify the file path or URL
file_path = 'data_in/people.csv'

column_types = {
    'First Name': str,
    'Family Name': str,
    'Date of Birth': str,
}

data = pd.read_csv(file_path, dtype=column_types)

data['Date of Birth as Date'] = pd.to_datetime(data['Date of Birth'], errors='coerce')

invalid_dates = data[data['Date of Birth as Date'].isna()].copy()
valid_dates =  data[data['Date of Birth as Date'].notna()].copy()

valid_dates['Age in Years'] = valid_dates['Date of Birth as Date'].apply(lambda x: relativedelta(datetime.now(), x).years)

valid_dates[['First Name', 'Family Name', 'Age in Years']].to_csv('output/valid_dates.csv', index=False)

invalid_dates[['First Name', 'Family Name', 'Date of Birth']].to_csv('output/invalid_dates.csv', index=False)

print('Data processing complete')
print('Check the Output folder for the results')
print(f"Number of rows processed: {data.shape[0]}")
print(f"Number of rows with valid dates: {valid_dates.shape[0]}")
print(f"Number of rows with invalid dates: {invalid_dates.shape[0]}")


