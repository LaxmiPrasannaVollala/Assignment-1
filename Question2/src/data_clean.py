df1.isnull().sum()
df1 = df1.drop_duplicates()
#Compute Final Grade (Average of Math, Reading, and Writing scores)
df1['final_grade'] = df1[['math score', 'reading score', 'writing score']].mean(axis=1)
df1.shape
df1.to_csv('cleaned_data.csv', index=False)
