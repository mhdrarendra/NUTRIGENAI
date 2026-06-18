import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# =========================
# 📊 DATASET LEBIH REALISTIS
# =========================
data = {
    "age": [25,45,35,50,23,40,30,60,28,55],
    "bmi": [18,30,25,28,21,27,24,32,23,44],
    "sleep": [8,5,6,5,8,6,7,4,8,5],
    "fast_food": [0,1,0,1,0,1,0,1,0,1],
    "activity": [1,0,1,0,1,0,1,0,1,0],
    "family": [0,1,0,1,0,1,0,1,0,1],
    "risk": [0,1,0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

# =========================
# 🎯 FEATURE & TARGET
# =========================
X = df[[
    "age",
    "bmi",
    "sleep",
    "fast_food",
    "activity",
    "family"
]]

y = df["risk"]

# =========================
# 🤖 TRAIN MODEL
# =========================
model = LogisticRegression()
model.fit(X, y)
print(model.coef_)

# =========================
# 💾 SAVE MODEL (FIXED PATH)
# =========================
BASE_DIR = r"C:\Users\RENDRA\OneDrive\Documents\nutrigen_projek\backend"
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "health_model.pkl")

os.makedirs(MODEL_DIR, exist_ok=True)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("Model tersimpan di:", MODEL_PATH)