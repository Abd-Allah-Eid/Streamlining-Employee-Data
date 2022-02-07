# Drop the duplicated columns
df_employees_renamed = df_employees.drop(["employee_first_name","employee_last_name"],axis=1)

# New columns names
new_column_names = {"employee_id": "id",
                    "employee_country": "country",
                    "employee_city": "city",
                    "employee_street": "street",
                    "employee_street_number": "street_number",
                    "relationship": "emergency_relationship",
                    "emergency_contact_number": "emergency_number"}

# Rename the columns
df_employees_renamed = df_employees_renamed.rename(columns=new_column_names)

# Take a look at the first rows of the DataFrame
print(df_employees_renamed.head())