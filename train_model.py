import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


# ============================================================
# SETTINGS
# ============================================================

DATASET_FILE = "cleaned_student_dropout_dataset.csv"
MODEL_FILE = "dropout_risk_model.pkl"

RANDOM_STATE = 42


# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 70)
print("STUDENT DROPOUT RISK - MODEL COMPARISON")
print("=" * 70)

df = pd.read_csv(DATASET_FILE)

print("\nDataset loaded successfully!")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])


# ============================================================
# FEATURES
# ============================================================

features = [
    "Attendance",
    "Study_Hours",
    "Internal_Marks",
    "Assignment_Marks",
    "Previous_Semester_GPA",
    "Backlogs"
]

target = "Dropout_Risk"


X = df[features]
y = df[target]


# ============================================================
# TARGET DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("TARGET DISTRIBUTION")
print("=" * 70)

print(y.value_counts())


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y
)


print("\n" + "=" * 70)
print("TRAIN / TEST SPLIT")
print("=" * 70)

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


# ============================================================
# DEFINE 5 MACHINE LEARNING ALGORITHMS
# ============================================================

models = {

    "Logistic Regression": Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            LogisticRegression(
                max_iter=2000,
                class_weight="balanced",
                random_state=RANDOM_STATE
            )
        )
    ]),


    "Decision Tree": DecisionTreeClassifier(
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight="balanced",
        random_state=RANDOM_STATE
    ),


    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight="balanced",
        random_state=RANDOM_STATE,
        n_jobs=-1
    ),


    "KNN": Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            KNeighborsClassifier(
                n_neighbors=7
            )
        )
    ]),


    "SVM": Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            SVC(
                kernel="rbf",
                C=1.0,
                class_weight="balanced",
                probability=True,
                random_state=RANDOM_STATE
            )
        )
    ])
}


# ============================================================
# TRAIN AND COMPARE MODELS
# ============================================================

results = []

trained_models = {}

print("\n" + "=" * 70)
print("TRAINING 5 MACHINE LEARNING ALGORITHMS")
print("=" * 70)


for name, model in models.items():

    print("\n" + "-" * 70)
    print("Training:", name)
    print("-" * 70)

    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred,
        average="macro",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="macro",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        average="macro",
        zero_division=0
    )

    # Individual class recall
    class_recall = recall_score(
        y_test,
        y_pred,
        labels=["LOW", "MEDIUM", "HIGH"],
        average=None,
        zero_division=0
    )

    low_recall = class_recall[0]
    medium_recall = class_recall[1]
    high_recall = class_recall[2]


    # Save results
    results.append({

        "Algorithm": name,

        "Accuracy": accuracy,

        "Macro_Precision": precision,

        "Macro_Recall": recall,

        "Macro_F1": f1,

        "LOW_Recall": low_recall,

        "MEDIUM_Recall": medium_recall,

        "HIGH_Recall": high_recall
    })


    trained_models[name] = model


    # Print results
    print(
        f"Accuracy       : {accuracy * 100:.2f}%"
    )

    print(
        f"Macro Precision: {precision * 100:.2f}%"
    )

    print(
        f"Macro Recall   : {recall * 100:.2f}%"
    )

    print(
        f"Macro F1       : {f1 * 100:.2f}%"
    )

    print(
        f"LOW Recall     : {low_recall * 100:.2f}%"
    )

    print(
        f"MEDIUM Recall  : {medium_recall * 100:.2f}%"
    )

    print(
        f"HIGH Recall    : {high_recall * 100:.2f}%"
    )


# ============================================================
# CREATE RESULTS DATAFRAME
# ============================================================

results_df = pd.DataFrame(results)


# ============================================================
# SORT BY MACRO F1
# ============================================================

results_df = results_df.sort_values(
    by="Macro_F1",
    ascending=False
).reset_index(drop=True)


# ============================================================
# DISPLAY FINAL COMPARISON
# ============================================================

print("\n\n" + "=" * 100)
print("FINAL MODEL COMPARISON")
print("=" * 100)

display_columns = [
    "Algorithm",
    "Accuracy",
    "Macro_Precision",
    "Macro_Recall",
    "Macro_F1",
    "LOW_Recall",
    "MEDIUM_Recall",
    "HIGH_Recall"
]

display_df = results_df[display_columns].copy()


# Convert to percentage
for column in display_columns[1:]:

    display_df[column] = (
        display_df[column] * 100
    ).round(2)


print(
    display_df.to_string(index=False)
)


# ============================================================
# SELECT BEST MODEL
# ============================================================

best_model_name = results_df.iloc[0]["Algorithm"]

best_model = trained_models[best_model_name]


print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print(
    "\nSelected Algorithm:",
    best_model_name
)

best_row = results_df.iloc[0]

print(
    f"Accuracy       : {best_row['Accuracy'] * 100:.2f}%"
)

print(
    f"Macro Precision: {best_row['Macro_Precision'] * 100:.2f}%"
)

print(
    f"Macro Recall   : {best_row['Macro_Recall'] * 100:.2f}%"
)

print(
    f"Macro F1       : {best_row['Macro_F1'] * 100:.2f}%"
)

print(
    f"LOW Recall     : {best_row['LOW_Recall'] * 100:.2f}%"
)

print(
    f"MEDIUM Recall  : {best_row['MEDIUM_Recall'] * 100:.2f}%"
)

print(
    f"HIGH Recall    : {best_row['HIGH_Recall'] * 100:.2f}%"
)


# ============================================================
# SAVE BEST MODEL
# ============================================================

joblib.dump(
    best_model,
    MODEL_FILE
)


print("\n" + "=" * 70)
print("BEST MODEL SAVED")
print("=" * 70)

print(
    f"\nModel saved as: {MODEL_FILE}"
)


# ============================================================
# DETAILED CLASSIFICATION REPORT
# ============================================================

y_best_pred = best_model.predict(X_test)


print("\n" + "=" * 70)
print("CLASSIFICATION REPORT - BEST MODEL")
print("=" * 70)

print(
    classification_report(
        y_test,
        y_best_pred,
        labels=["LOW", "MEDIUM", "HIGH"],
        zero_division=0
    )
)


# ============================================================
# SAMPLE PREDICTION
# ============================================================

print("\n" + "=" * 70)
print("SAMPLE PREDICTION TEST")
print("=" * 70)


sample_students = pd.DataFrame({

    "Attendance": [
        90,
        65,
        35
    ],

    "Study_Hours": [
        8,
        4,
        1
    ],

    "Internal_Marks": [
        90,
        60,
        35
    ],

    "Assignment_Marks": [
        90,
        60,
        30
    ],

    "Previous_Semester_GPA": [
        9.0,
        6.5,
        3.5
    ],

    "Backlogs": [
        0,
        2,
        5
    ]
})


sample_predictions = best_model.predict(
    sample_students
)


for i, prediction in enumerate(
    sample_predictions
):

    print(
        f"Student {i + 1}: {prediction}"
    )


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 70)
print("MODEL COMPARISON COMPLETED SUCCESSFULLY!")
print("=" * 70)

print(
    "\nFinal selected model:",
    best_model_name
)

print(
    "Saved model:",
    MODEL_FILE
)

print(
    "\nYou can now connect this model with ai.py / ui.py."
)