import os
import pickle
import pandas as pd

# =========================
# LOAD MODEL
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "obesity_logistic_regression.pkl"
)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# =========================
# PREDICT
# =========================

def predict_health(data):
    try:

        # =====================
        # MAPPING INPUT STREAMLIT
        # =====================

        age = data["umur"]

        gender = "Male" if data["gender"] == "Laki-laki" else "Female"

        height = data["tinggi"] / 100
        weight = data["berat"]

        # Aktivitas Fisik → FAF
        aktivitas_map = {
            "Jarang": 0,
            "1–2 Kali/Minggu": 1,
            "3–4 Kali/Minggu": 2,
            "Hampir Setiap Hari": 3
        }

        faf = aktivitas_map.get(data["aktivitas"], 1)

        # Fast Food → FAVC
        favc = (
            "yes"
            if data["fast_food"] != "Tidak Pernah"
            else "no"
        )

        # Riwayat keluarga
        family = (
            "yes"
            if data["riwayat"] == "Ada"
            else "no"
        )

        # =====================
        # DATAFRAME INPUT
        # =====================

        input_df = pd.DataFrame([{
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight,

            # default value
            "CALC": "Sometimes",
            "FAVC": favc,
            "FCVC": 2.5,
            "NCP": 3,
            "SCC": "no",
            "SMOKE": "no",
            "CH2O": 2,

            "family_history_with_overweight": family,

            "FAF": faf,
            "TUE": 1,

            "CAEC": "Sometimes",
            "MTRANS": "Public_Transportation"
        }])

        # =====================
        # PREDIKSI
        # =====================

        prediction = model.predict(input_df)[0]

        probabilities = model.predict_proba(input_df)[0]

        return {
            "prediction": prediction,
            "probability": float(max(probabilities))
        }

    except Exception as e:
        return {
            "error": str(e)
        }