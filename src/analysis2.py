import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df1 = pd.read_csv("data/linkedin_job_postings.csv")


# Find out what types of jobs are most common
print(df1['job_type'].value_counts())


# Find out how many tech jobs are available
tech_jobs = df1[df1['job_title'].str.contains(
   "software|developer|engineer|data|IT|cloud|cyber|machine learning|AI",
   case=False,
   na=False
)]


print("Number of tech-related jobs:", len(tech_jobs))
print(tech_jobs['job_title'].value_counts().head(20))


skills_df = pd.read_csv("data/job_skills.csv")


# Drop missing values
skills_df = skills_df.dropna(subset=["job_skills"])


# Split skills into lists
skills_df["job_skills"] = skills_df["job_skills"].str.split(",")


# Convert lists to separate rows
exploded = skills_df.explode("job_skills")


# Clean whitespace
exploded["job_skills"] = exploded["job_skills"].str.strip()


# Count the top skills
skill_counts = exploded["job_skills"].value_counts()


print("=== TOP 20 MOST REQUIRED SKILLS ===")
print(skill_counts.head(20))
