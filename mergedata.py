import pandas as pd  

main = pd.read_excel("data/ai_impact_student_performance_dataset.xlsx")
ai = pd.read_excel("data/Ai_Impact.xlsx")

ai_selected = ai[
    [
        "User_ID",
        "Accuracy_Rating",
        "Satisfaction_Score",
        "Time_Saved_Hours_Per_Week"
    ]
]


merged = pd.merge(
    main,
    ai_selected,
    left_on="student_id",
    right_on="User_ID",
    how="left"
)

merged = merged.drop(columns=["User_ID"])
merged.to_excel("outputs/mergedata.xlsx", index=False)