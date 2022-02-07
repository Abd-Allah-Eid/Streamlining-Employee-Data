# Load data from the second sheet of employee_information.xlsx
import pandas as pd
df_emergency_contacts = pd.read_excel("datasets/employee_information.xlsx",sheet_name=1, header=None)

# Declare a list of new column names
emergency_contacts_header = ["employee_id", "last_name", "first_name", "emergency_contact", "emergency_contact_number","relationship"]

# Rename the columns
df_emergency_contacts.columns = emergency_contacts_header

print(df_emergency_contacts.head())