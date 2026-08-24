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


DATASET_FILE = "cleaned_student_dropout_dataset.csv"
MODEL_FILE = "dropout_risk_model.pkl"
RANDOM_STATE = 42


print("=" * 70)
print("STUDENT DROPOUT RISK - MODEL COMPARISON")
print("=" * 70)


try:
    df = pd.read_csv(DATASET_FILE)
except FileNotFoundError:
    print(f"\nDataset file not found: {DATASET_FILE}")
    exit()


print("\nDataset loaded successfully!")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nDataset columns:")
print(df.columns.tolist())


features = [
    "Attendance",
    "Study_Hours",
    "Internal_Marks",
    "Assignment_Marks",
    "Previous_Semester_GPA",
    "Backlogs"
]

target = "Dropout_Risk"


missing_columns = [
    column
    for column in features + [target]
    if column not in df.columns
]

if missing_columns:
    print("\nMissing columns:")
    for column in missing_columns:
        print("-", column)

    print("\nPlease check your dataset column names.")
    exit()


df = df[features + [target]].copy()

df = df.dropna()

print("\nRows after removing missing values:", len(df))


X = df[features]
y = df[target]


print("\n" + "=" * 70)
print("TARGET DISTRIBUTION")
print("=" * 70)

print(y.value_counts())


print("\nTarget classes:")

for value in sorted(y.unique()):
    print("-", value)


if len(y.unique()) < 2:
    print("\nError: Target must contain at least 2 classes.")
    exit()


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


results = []
trained_models = {}


print("\n" + "=" * 70)
print("TRAINING MODELS")
print("=" * 70)


for name, model in models.items():

    print("\n" + "-" * 70)
    print("Training:", name)
    print("-" * 70)

    try:
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

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

        class_recall = recall_score(
            y_test,
            y_pred,
            labels=["LOW", "MEDIUM", "HIGH"],
            average=None,
            zero_division=0
        )

        recall_dict = dict(
            zip(
                ["LOW", "MEDIUM", "HIGH"],
                class_recall
            )
        )

        low_recall = recall_dict.get("LOW", 0)
        medium_recall = recall_dict.get("MEDIUM", 0)
        high_recall = recall_dict.get("HIGH", 0)

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

        print(f"Accuracy       : {accuracy * 100:.2f}%")
        print(f"Macro Precision: {precision * 100:.2f}%")
        print(f"Macro Recall   : {recall * 100:.2f}%")
        print(f"Macro F1       : {f1 * 100:.2f}%")
        print(f"LOW Recall     : {low_recall * 100:.2f}%")
        print(f"MEDIUM Recall  : {medium_recall * 100:.2f}%")
        print(f"HIGH Recall    : {high_recall * 100:.2f}%")

    except Exception as error:
        print("Training failed:", error)


if not results:
    print("\nNo model was trained successfully.")
    exit()


results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="Macro_F1",
    ascending=False
).reset_index(drop=True)


print("\n\n" + "=" * 100)
print("FINAL MODEL COMPARISON")
print("=" * 100)


display_df = results_df.copy()

percentage_columns = [
    "Accuracy",
    "Macro_Precision",
    "Macro_Recall",
    "Macro_F1",
    "LOW_Recall",
    "MEDIUM_Recall",
    "HIGH_Recall"
]

for column in percentage_columns:
    display_df[column] = (
        display_df[column] * 100
    ).round(2)


print(display_df.to_string(index=False))


best_model_name = results_df.iloc[0]["Algorithm"]
best_model = trained_models[best_model_name]


print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print("\nSelected Algorithm:", best_model_name)

best_row = results_df.iloc[0]

print(
    f"Accuracy       : "
    f"{best_row['Accuracy'] * 100:.2f}%"
)

print(
    f"Macro Precision: "
    f"{best_row['Macro_Precision'] * 100:.2f}%"
)

print(
    f"Macro Recall   : "
    f"{best_row['Macro_Recall'] * 100:.2f}%"
)

print(
    f"Macro F1       : "
    f"{best_row['Macro_F1'] * 100:.2f}%"
)

print(
    f"LOW Recall     : "
    f"{best_row['LOW_Recall'] * 100:.2f}%"
)

print(
    f"MEDIUM Recall  : "
    f"{best_row['MEDIUM_Recall'] * 100:.2f}%"
)

print(
    f"HIGH Recall    : "
    f"{best_row['HIGH_Recall'] * 100:.2f}%"
)


joblib.dump(
    best_model,
    MODEL_FILE
)


print("\n" + "=" * 70)
print("BEST MODEL SAVED")
print("=" * 70)

print("\nModel saved as:", MODEL_FILE)


y_best_pred = best_model.predict(X_test)


print("\n" + "=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)

print(
    classification_report(
        y_test,
        y_best_pred,
        labels=["LOW", "MEDIUM", "HIGH"],
        zero_division=0
    )
)


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


print("\n" + "=" * 70)
print("SAMPLE PREDICTION TEST")
print("=" * 70)


for i, prediction in enumerate(
    sample_predictions
):

    print(
        f"Student {i + 1}: {prediction}"
    )


print("\n" + "=" * 70)
print("MODEL TRAINING COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nFinal selected model:", best_model_name)
print("Saved model:", MODEL_FILE)

print("\nFeatures used:")

for feature in features:
    print("-", feature)

print("\nYou can now connect this model with ai.py and ui.py.")