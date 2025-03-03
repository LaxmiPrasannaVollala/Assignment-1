#checking for null values
df.isnull().sum()
# Convert 'Frailty' to binary (0 = No, 1 = Yes)
df['Frailty'] = df['Frailty'].map({'N': 0, 'Y': 1})
df
df.to_csv('cleaned_.csv', index=False)
