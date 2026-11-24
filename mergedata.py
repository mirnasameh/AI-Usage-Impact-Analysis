import pandas as pd

# Read both Excel files
main = pd.read_excel("data/ai_impact_student_performance_dataset.xlsx")
ai = pd.read_excel("data/Ai_Impact.xlsx")

# Select only the columns we need
ai_selected = ai[
    [
        "User_ID",
        "Accuracy_Rating",
        "Satisfaction_Score",
        "Time_Saved_Hours_Per_Week"
    ]
]

# Merge the datasets
merged = pd.merge(
    main,
    ai_selected,
    left_on="student_id",
    right_on="User_ID",
    how="left"
)

# Remove the duplicate ID column
merged = merged.drop(columns=["User_ID"])

# Export the result
merged.to_excel("mergedata.xlsx", index=False)