import pandas as pd


# Function to load and prepare data
def load_data():
  df_airlines = pd.read_csv('data/Airlines_data.csv')
  df_loan = pd.read_csv('data/updated_loan.csv')
  data_airlines = df_airlines.to_dict(orient='records')
  data_loan = df_loan.to_dict(orient='records')
  return data_airlines, data_loan
