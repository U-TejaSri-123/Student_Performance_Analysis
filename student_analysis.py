import pandas as pd

df = pd.read_csv("student_performance.csv")

print("Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\nRows after removing duplicates:")
print(df.shape)

print("\nDataset Statistics:")
print(df.describe())

avg_score = df["total_score"].mean()

print("\nAverage Score:")
print(avg_score)

grade_count = df["grade"].value_counts()

print("\nGrade Distribution:")
print(grade_count)

import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))

grade_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")

plt.ylabel("")

plt.savefig("grade_distribution.png")

plt.close()

print("Grade chart saved successfully")

# Study Hours vs Total Score

sample_df = df.sample(5000)

plt.figure(figsize=(8,5))

plt.scatter(
    sample_df["weekly_self_study_hours"],
    sample_df["total_score"]
)

plt.xlabel("Weekly Self Study Hours")
plt.ylabel("Total Score")
plt.title("Study Hours vs Total Score")

plt.savefig("study_hours_vs_score.png")

plt.close()

print("Study Hours chart saved successfully")

# Attendance vs Total Score

sample_df = df.sample(5000)

plt.figure(figsize=(8,5))

plt.scatter(
    sample_df["attendance_percentage"],
    sample_df["total_score"]
)

plt.xlabel("Attendance Percentage")
plt.ylabel("Total Score")
plt.title("Attendance vs Total Score")

plt.savefig("attendance_vs_score.png")

plt.close()

print("Attendance chart saved successfully")

# Class Participation vs Total Score

sample_df = df.sample(5000)

plt.figure(figsize=(8,5))

plt.scatter(
    sample_df["class_participation"],
    sample_df["total_score"]
)

plt.xlabel("Class Participation")
plt.ylabel("Total Score")
plt.title("Class Participation vs Total Score")

plt.savefig("participation_vs_score.png")

plt.close()

print("Participation chart saved successfully")
correlation = df[
[
    "weekly_self_study_hours",
    "attendance_percentage",
    "class_participation",
    "total_score"
]
].corr()

print("\nCorrelation Matrix:")
print(correlation)
correlation.to_csv("correlation_matrix.csv")

print("Correlation Matrix Saved")
