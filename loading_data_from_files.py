# Import the library you need
import pandas as pd

# Load office_addresses.csv
df_office_addresses = pd.read_csv("datasets/office_addresses.csv")

# Load employee_information.xlsx
df_employee_addresses = pd.read_excel("datasets/employee_information.xlsx")

# Take a look at the first rows of the DataFrames
print(df_office_addresses.head())
print(df_employee_addresses.head())