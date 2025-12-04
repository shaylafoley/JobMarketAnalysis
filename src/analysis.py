import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ds_salaries.csv")

# 1. Salary Trends Over Time
print("=== Average Salary by Year ===")
print(df.groupby("work_year")["salary_in_usd"].mean())

# 2. Highest Paying Job Titles
print("=== Top 20 Highest Paying Job Titles ===")
print(df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(20))

# Entry-level jobs only
entry_df = df[df["experience_level"] == "EN"]

print("=== ENTRY LEVEL SALARY ANALYSIS ===")

print("\nNumber of entry-level roles:", len(entry_df))

print("\nAverage entry-level salary in USD:")
print(entry_df["salary_in_usd"].mean())

print("\nTop 20 highest paying entry-level job titles:")
print(entry_df.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False).head(20))
