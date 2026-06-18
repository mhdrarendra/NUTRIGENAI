import os
import pickle

# =========================
# LOAD MODEL
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model", "health_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


# =========================
# PREDICTION FUNCTION
# =========================
def predict_health(data):
    try:
        age = data["umur"]
        bmi = data["bmi"]
        sleep = data["tidur"]
        fast_food = data["fast_food"]
        activity = data["aktivitas"]
        family = data["riwayat"]

        # mapping string → numeric
        fast_food_val = 1 if fast_food in ["Setiap Hari", "3–4 Kali/Minggu"] else 0
        activity_val = 1 if activity in ["Hampir Setiap Hari", "3–4 Kali/Minggu"] else 0
        family_val = 1 if family == "Ada" else 0

        result = model.predict([[
            age,
            bmi,
            sleep,
            fast_food_val,
            activity_val,
            family_val
        ]])

        return {
            "umur": age,
            "bmi": bmi,
            "risiko": int(result[0])
        }

    except Exception as e:
        return {"error": str(e)}