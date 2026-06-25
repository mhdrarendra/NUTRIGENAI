import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(r"C:\Users\RENDRA\OneDrive\Documents\nutrigen_projek_2_fapi\frontend\chat\obesity.csv")

# =========================
# FEATURE & TARGET
# =========================

X = df.drop("NObeyesdad", axis=1)
y = df["NObeyesdad"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# NUMERIC FEATURES
# =========================

numeric_features = [
    "Age",
    "Height",
    "Weight",
    "FCVC",
    "NCP",
    "CH2O",
    "FAF",
    "TUE"
]

# =========================
# CATEGORICAL FEATURES
# =========================

categorical_features = [
    "Gender",
    "CALC",
    "FAVC",
    "SCC",
    "SMOKE",
    "family_history_with_overweight",
    "CAEC",
    "MTRANS"
]

# =========================
# PREPROCESSOR
# =========================

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# =========================
# PIPELINE MODEL
# =========================

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(
        max_iter=5000,
        random_state=42
    ))
])

# =========================
# TRAINING
# =========================

model.fit(X_train, y_train)

# =========================
# EVALUASI
# =========================

y_pred = model.predict(X_test)

print("=" * 50)
print("ACCURACY")
print("=" * 50)
print(accuracy_score(y_test, y_pred))

print("\nCLASSIFICATION REPORT")
print("=" * 50)
print(classification_report(y_test, y_pred))

# =========================
# SAVE MODEL
# =========================

BASE_DIR = r"C:\Users\RENDRA\OneDrive\Documents\nutrigen_projek_2_fapi\backend"

MODEL_DIR = os.path.join(BASE_DIR, "model")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "obesity_logistic_regression.pkl"
)

os.makedirs(MODEL_DIR, exist_ok=True)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("\nModel berhasil disimpan:")
print(MODEL_PATH)