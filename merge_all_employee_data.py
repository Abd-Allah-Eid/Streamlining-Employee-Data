import pandas as pd
# Load employee_information.xlsx
df_employee_addresses = pd.read_excel("datasets/employee_information.xlsx")

# Load data from the second sheet of employee_information.xlsx
df_emergency_contacts = pd.read_excel("datasets/employee_information.xlsx",sheet_name=1, header=None)

# Declare a list of new column names
emergency_contacts_header = ["employee_id", "last_name", "first_name", "emergency_contact", "emergency_contact_number","relationship"]

# Rename the columns
df_emergency_contacts.columns = emergency_contacts_header

# Merge df_employee_addresses with df_emergency_contacts
df_employees = df_employee_addresses.merge(df_emergency_contacts, how="left", on="employee_id", copy=False)

# Load employee_roles.json
df_employee_roles = pd.read_json("datasets/employee_roles.json",orient="index")
df_employee_roles = df_employee_roles.reindex(sorted(df_employee_roles.columns), axis=1)
# Load office_addresses.csv
df_office_addresses = pd.read_csv("datasets/office_addresses.csv")
# Merge df_employees with df_employee_roles
df_employees = df_employees.merge(df_employee_roles, how="left", left_on="employee_id", right_on=df_employee_roles.index, copy=False)

# Merge df_employees with df_office_adresses
df_employees = df_employees.merge(df_office_addresses, how="left", left_on="employee_country", right_on="office_country", copy=False)

# Take a look at the first rows of the DataFrame and its columns
print(df_employees.head())
print(df_employees.columns)