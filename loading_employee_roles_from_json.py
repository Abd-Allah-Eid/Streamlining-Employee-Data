import pandas as pd
# Load employee_roles.json
df_employee_roles = pd.read_json("datasets/employee_roles.json",orient="index")
df_employee_roles = df_employee_roles.reindex(sorted(df_employee_roles.columns), axis=1)

# Take a look at the first rows of the DataFrame
df_employee_roles.head()