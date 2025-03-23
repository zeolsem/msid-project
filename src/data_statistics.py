import pandas as pd

# Numerical series: Age, Academic Pressure, Work Pressure, CGPA, Study Satisfaction, Job Satisfaction, Work/Study Hours, Financial Stress
# Categorical series: Gender, City, Profession, Sleep Duration, Dietary Habits, Degree, Suicidal thoughts, FamilyHistoryOfMI, Depression
df = pd.read_csv('../data/student_depression_dataset.csv')

# Drop rows with null values as there are very little of them, and it won't affect the study
df.dropna(inplace = True)

# Delete working students, because there only are 3 of them so no meaningful analysis could be done anyway
df = df[df['Work Pressure'] == 0.0]

numerical_summary = df.describe().T
numerical_summary = numerical_summary.drop('id')
numerical_summary = numerical_summary.drop('count', axis=1)
print(numerical_summary.to_string())
