import pandas as pd
import numpy as np
import os

INPUT_FILE = "outputs/mergedata.xlsx"
OUTPUT_FILE = "outputs/cleaned_dataset.xlsx"

print("Loading dataset...")

if not os.path.exists(INPUT_FILE):
    print("ERROR: Excel file not found!")
    print("Expected location:", os.path.abspath(INPUT_FILE))
    exit()

df = pd.read_excel(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Original dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())
#Column names.
#Number of non-null values.
#Data types.
#Memory usage.
print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nColumn names:")
print(df.columns.tolist())


df.drop_duplicates(inplace=True)

print("\nDuplicates removed.")
print("Current shape:", df.shape)



df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
)

print("\nColumn names cleaned:")
print(df.columns.tolist())



for col in df.select_dtypes(include=["object"]).columns:

    df[col] = df[col].astype("string").str.strip()

    df[col] = df[col].replace(
        ["", "NA", "N/A", "n/a", "null", "None"],
        pd.NA
    )

print("\nText values cleaned.")



for col in df.columns:

    if df[col].dtype == "object":
        converted = pd.to_numeric(df[col], errors="coerce")

        original_non_missing = df[col].notna().sum()
        converted_non_missing = converted.notna().sum()

        if original_non_missing > 0:
            if converted_non_missing / original_non_missing >= 0.8:
                df[col] = converted

print("\nNumeric columns checked.")



print("\nMissing values before handling:")
print(df.isnull().sum())

for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):

        if df[col].isnull().sum() > 0:
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)

    else:

        if df[col].isnull().sum() > 0:
            mode_value = df[col].mode(dropna=True)

            if not mode_value.empty:
                df[col] = df[col].fillna(mode_value[0])

print("\nMissing values handled.")



print("\nFinal data types:")
print(df.dtypes)



print("\nFinal missing values:")
print(df.isnull().sum())

print("\nFinal duplicates:")
print(df.duplicated().sum())

print("\nFinal dataset shape:")
print(df.shape)



df.to_excel(OUTPUT_FILE, index=False)

print("\n==========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved as:", OUTPUT_FILE)
print("==========================================")
