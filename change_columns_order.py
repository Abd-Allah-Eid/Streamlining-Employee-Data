# Declare a list for the new column's order and reorder columns
new_column_order = ["id", "last_name", "first_name", "title", "team", "monthly_salary", 
                    "country", "city", "street", "street_number",
                    "emergency_contact", "emergency_number", "emergency_relationship",
                    "office", "office_country", "office_city", "office_street", "office_street_number"]

# Reorder the columns
df_employees_ordered = df_employees_renamed[new_column_order]

# Take a look at the result
df_employees_ordered.head()