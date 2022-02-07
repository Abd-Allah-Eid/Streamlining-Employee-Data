# Reset the index and drop the column
df_employees_final = df_employees_ordered.set_index(df_employees_ordered["id"]).drop(columns=["id"])

status_list = []

# Loop through the row values and append to status_list accordingly
for column,value in df_employees_final.iterrows():
   if pd.isnull(value["office"]):
        status_list.append("Remote")
   else:
        status_list.append("On-site")


# # Insert status_list as a new column
df_employees_final.insert(loc=5, column="status", value=status_list)

# # Take a look at the first rows of the DataFrame
df_employees_final.head()