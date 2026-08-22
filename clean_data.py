import pandas as pd
import os

# ============================================================
# FILE SETTINGS
# ============================================================

INPUT_FILE = "student_dropout_training_dataset.csv"
OUTPUT_FILE = "cleaned_student_dropout_dataset.csv"


# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 60)
print("STUDENT DROPOUT DATASET CLEANING")
print("=" * 60)

if not os.path.exists(INPUT_FILE):
    print(f"\nERROR: File not found: {INPUT_FILE}")
    exit()

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nOriginal Columns:")
print(list(df.columns))


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()

print("\nColumn names cleaned.")


# ============================================================
# REMOVE EMPTY ROWS
# ============================================================

before = len(df)

df = df.dropna(how="all")

after = len(df)

print("\nEmpty rows removed:", before - after)


# ============================================================
# REMOVE DUPLICATES
# ============================================================

duplicate_count = df.duplicated().sum()

print("\nDuplicate rows found:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")
else:
    print("No duplicate rows found.")


# ============================================================
# REQUIRED COLUMNS
# ============================================================

numeric_columns = [
    "Attendance",
    "Study_Hours",
    "Internal_Marks",
    "Assignment_Marks",
    "Previous_Semester_GPA",
    "Backlogs"
]

target_column = "Dropout_Risk"


# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

print("\nChecking required columns...")

missing_columns = []

for col in numeric_columns:
    if col not in df.columns:
        missing_columns.append(col)

if target_column not in df.columns:
    missing_columns.append(target_column)


if missing_columns:

    print("\nERROR!")
    print("Missing columns:")

    for col in missing_columns:
        print("-", col)

    print("\nAvailable columns:")
    print(list(df.columns))

    exit()


print("All required columns are available.")


# ============================================================
# CONVERT NUMERICAL COLUMNS
# ============================================================

print("\nConverting numerical columns...")

for col in numeric_columns:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

print("Numerical conversion completed.")


# ============================================================
# HANDLE MISSING VALUES
# ============================================================

print("\nChecking missing values...")

for col in numeric_columns:

    missing = df[col].isnull().sum()

    if missing > 0:

        print(f"{col}: {missing} missing values")

        median_value = df[col].median()

        df[col] = df[col].fillna(median_value)

        print(f"Filled with median: {median_value}")

    else:

        print(f"{col}: No missing values")


# ============================================================
# CLEAN TARGET COLUMN
# ============================================================

print("\nCleaning Dropout_Risk column...")

df[target_column] = (
    df[target_column]
    .astype(str)
    .str.strip()
    .str.upper()
)

print("\nRisk categories:")

print(df[target_column].value_counts())


# ============================================================
# VALID RISK CATEGORIES
# ============================================================

valid_categories = [
    "LOW",
    "MEDIUM",
    "HIGH"
]

invalid_rows = ~df[target_column].isin(valid_categories)

invalid_count = invalid_rows.sum()

print("\nInvalid risk values:", invalid_count)

if invalid_count > 0:

    print("Removing invalid rows...")

    df = df[~invalid_rows]

else:

    print("No invalid risk values found.")


# ============================================================
# RANGE VALIDATION
# ============================================================

print("\nChecking value ranges...")


# Attendance: 0 - 100
df.loc[df["Attendance"] < 0, "Attendance"] = 0
df.loc[df["Attendance"] > 100, "Attendance"] = 100


# Study Hours: 0 - 24
df.loc[df["Study_Hours"] < 0, "Study_Hours"] = 0
df.loc[df["Study_Hours"] > 24, "Study_Hours"] = 24


# Internal Marks: 0 - 100
df.loc[df["Internal_Marks"] < 0, "Internal_Marks"] = 0
df.loc[df["Internal_Marks"] > 100, "Internal_Marks"] = 100


# Assignment Marks: 0 - 100
df.loc[df["Assignment_Marks"] < 0, "Assignment_Marks"] = 0
df.loc[df["Assignment_Marks"] > 100, "Assignment_Marks"] = 100


# GPA: 0 - 10
df.loc[df["Previous_Semester_GPA"] < 0, "Previous_Semester_GPA"] = 0
df.loc[df["Previous_Semester_GPA"] > 10, "Previous_Semester_GPA"] = 10


# Backlogs: minimum 0
df.loc[df["Backlogs"] < 0, "Backlogs"] = 0


print("Range validation completed.")


# ============================================================
# ROUND VALUES
# ============================================================

df["Attendance"] = df["Attendance"].round(2)

df["Study_Hours"] = df["Study_Hours"].round(2)

df["Internal_Marks"] = df["Internal_Marks"].round(2)

df["Assignment_Marks"] = df["Assignment_Marks"].round(2)

df["Previous_Semester_GPA"] = df[
    "Previous_Semester_GPA"
].round(2)


# ============================================================
# FINAL CHECK
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATASET CHECK")
print("=" * 60)

print("\nRows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nMissing values:")

print(df.isnull().sum())

print("\nDuplicate rows:")

print(df.duplicated().sum())


# ============================================================
# RISK DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("DROPOUT RISK DISTRIBUTION")
print("=" * 60)

print(df[target_column].value_counts())


# ============================================================
# SAVE CLEANED DATASET
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n" + "=" * 60)
print("CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nCleaned file saved as:")
print(OUTPUT_FILE)

print("\nFirst 10 rows:")

print(df.head(10))