# Summary Statistics
print("Summary Statistics:")
summary_stats = df.describe()
# Visualizations
sns.histplot(df['Grip strength'],bins=5, kde=True)
plt.title('Distribution of Grip Strength')
plt.xlabel('Grip Strength (kg)')
plt.show()
plt.savefig("Distribution of Grip Strength.png")  
plt.close()

sns.boxplot(x=df['Frailty'], y=df['Grip strength'])
plt.title('Grip Strength by Frailty')
plt.xlabel('Frailty (0 = No, 1 = Yes)')
plt.ylabel('Grip Strength (kg)')
plt.show()
plt.savefig("Grip Strength by Frailty.png")
plt.close()
# Scatter plot: Grip Strength vs. Age
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Age'], y=df['Grip strength'])
plt.title('Grip Strength vs. Age')
plt.xlabel('Age (years)')
plt.ylabel('Grip Strength (kg)')
plt.show()
plt.savefig("Grip Strength vs Age.png")
plt.close()

# Scatter plot: Grip Strength vs. Weight
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Weight'], y=df['Grip strength'])
plt.title('Grip Strength vs. Weight')
plt.xlabel('Weight (lbs)')
plt.ylabel('Grip Strength (kg)')
plt.show()
plt.savefig("Grip Strength vs Weight.png")
plt.close()
# Correlation Analysis
corr_grip_age, _ = pearsonr(df['Grip strength'], df['Age'])
corr_grip_weight, _ = pearsonr(df['Grip strength'], df['Weight'])
print(f'Correlation (Grip Strength vs Age): {corr_grip_age:.2f}')
print(f'Correlation (Grip Strength vs Weight): {corr_grip_weight:.2f}')
with open("results.txt", "w") as file:
    file.write("Summary Statistics:\n")
    file.write(summary_stats.to_string())  # Save summary statistics
    
    file.write("\n\nCorrelation Analysis:\n")
    file.write(f"Correlation (Grip Strength vs Age): {corr_grip_age:.2f}\n")
    file.write(f"Correlation (Grip Strength vs Weight): {corr_grip_weight:.2f}\n")
    
    file.write("\n\nT-test Analysis:\n")
    file.write(f"T-test: t-statistic = {t_stat:.2f}, p-value = {p_value:.4f}\n")
if p_value < 0.05:
    print("Significant difference in grip strength between frail and non-frail groups.")
else:
    print("No significant difference in grip strength between frail and non-frail groups.")
  #output:No significant difference in grip strength between frail and non-frail groups.
