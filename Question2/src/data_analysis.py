# 1. Distribution of Final Grades
plt.figure(figsize=(10, 6))
sns.histplot(df1['final_grade'], bins=10, kde=True)
plt.title('Distribution of Final Grades')
plt.xlabel('Final Grade')
plt.ylabel('Number of Students')
plt.show()
plt.savefig("Distribution of Final Grades.png")
plt.close()

# 2. Gender vs. Average Scores
plt.figure(figsize=(10, 6))
gender_avg_scores = df1.groupby('gender')[['math score', 'reading score', 'writing score']].mean().reset_index()
gender_avg_scores.plot(kind='bar', x='gender', figsize=(10, 6))
plt.title('Average Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.show()
plt.savefig("Average Scores by Gender.png")
plt.close()

# 3. Parental Education Level vs. Student Performance
plt.figure(figsize=(12, 8))
sns.boxplot(x='parental level of education', y='final_grade', data=df1)
plt.title('Parental Education Level vs. Student Performance')
plt.xlabel('Parental Education Level')
plt.ylabel('Final Grade')
plt.xticks(rotation=45)
plt.show()
plt.savefig('Parental Education Level vs. Student Performance.png')
plt.close()
# Categorizing Final Grade into Pass/Fail
df1['grade_category'] = df1['final_grade'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')

# 4. Test Preparation Course vs. Final Grade Rate
plt.figure(figsize=(8, 8))
prep_course_counts = df1.groupby('test preparation course')['grade_category'].value_counts().unstack()
prep_course_counts.plot(kind='pie', subplots=True, figsize=(12, 6), autopct='%1.1f%%')
plt.title('Test Preparation Course vs. Pass/Fail Rate')
plt.ylabel('')
plt.show()
plt.savefig("Test Preparation Course vs Pass or Fail Rate.png")
plt.close()

# 5. Lunch Type vs. Final Grade
plt.figure(figsize=(10, 6))
sns.scatterplot(x='lunch', y='final_grade', data=df1)
plt.title('Lunch vs. Final Grade')
plt.xlabel('Lunch')
plt.ylabel('Final Grade')
plt.show()
plt.savefig('Lunch vs. Final Grade.png')
plt.close()
