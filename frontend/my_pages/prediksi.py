import streamlit as st
import requests
from backend.services.prediction_service import predict_health

# =========================
# 🧠 REKOMENDASI ENGINE
# =========================
def get_rekomendasi(bmi):
    rec = []

    # =========================
    # KURUS
    # =========================
    if bmi < 18.5:
        rec.append("Tingkatkan asupan kalori sehat (karbohidrat kompleks & protein)")
        rec.append("Perbanyak frekuensi makan (3–5 kali sehari)")
        rec.append("Konsumsi makanan tinggi protein seperti telur, ayam, ikan")
        rec.append("Lakukan latihan kekuatan (strength training) ringan")
        rec.append("Periksa kondisi kesehatan jika berat sulit naik")

    # =========================
    # NORMAL
    # =========================
    elif bmi < 25:
        rec.append("Pertahankan aktivitas fisik secara rutin")
        rec.append("Pertahankan pola tidur 7–8 jam per hari")
        rec.append("Jaga pola makan seimbang")
        rec.append("Perbanyak konsumsi sayur dan buah")

    # =========================
    # OVERWEIGHT
    # =========================
    elif bmi < 30:
        rec.append("Kurangi makanan tinggi kalori dan gula")
        rec.append("Rutin olahraga 3–4 kali seminggu")
        rec.append("Kurangi konsumsi fast food")
        rec.append("Perbanyak air putih dan sayur")

    # =========================
    # OBESITAS
    # =========================
    else:
        rec.append("Kurangi makanan cepat saji secara signifikan")
        rec.append("Rutin olahraga minimal 4–5 kali seminggu")
        rec.append("Perbaiki pola tidur")
        rec.append("Konsultasi ke tenaga kesehatan")
        rec.append("Turunkan berat badan secara bertahap")

    return rec


# =========================
# 🚀 MAIN PAGE
# =========================
def show():
    st.header("⚠️ Prediksi Risiko Kesehatan")

    # ================= INPUT USER =================
    nama = st.text_input("Nama Lengkap", "Masukkan Nama Anda")

    umur = st.number_input("Umur", 0, 120, 23)

    gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])

    tinggi = st.number_input("Tinggi Badan (cm)", 100, 220, 160)

    berat = st.number_input("Berat Badan (kg)", 30, 200, 55)

    aktivitas = st.selectbox("Aktivitas Fisik", [
        "Jarang",
        "1–2 Kali/Minggu",
        "3–4 Kali/Minggu",
        "Hampir Setiap Hari"
    ])

    tidur = st.number_input("Durasi Tidur (Jam/Hari)", 0, 24, 7)

    riwayat = st.selectbox("Riwayat Diabetes Keluarga", ["Tidak", "Ada"])

    fast_food = st.selectbox("Konsumsi Makanan Cepat Saji", [
        "Tidak Pernah",
        "1–2 Kali/Minggu",
        "3–4 Kali/Minggu",
        "Setiap Hari"
    ])

    # ================= PREDIKSI =================
    if st.button("Prediksi"):
        bmi = berat / ((tinggi / 100) ** 2)

        with st.spinner("🔍 Menganalisis kesehatan..."):

            hasil = predict_health({
                "umur": umur,
                "bmi": bmi,
                "tidur": tidur,
                "fast_food": fast_food,
                "aktivitas": aktivitas,
                "riwayat": riwayat
            })

        if "error" in hasil:
            st.error(hasil["error"])
            return

        if bmi < 18.5:
            kategori = "Kurus"
        elif bmi < 25:
            kategori = "Normal"
        elif bmi < 30:
            kategori = "Overweight"
        else:
            kategori = "Obesitas"

        if bmi < 18.5:
            risiko_text = "Sangat Rendah"
        elif bmi < 25:
            risiko_text = "Rendah/Aman"
        elif bmi < 30:
            risiko_text = "Sedang/Waspada"
        elif bmi < 35:
            risiko_text = "Tinggi/Resiko"
        else:
            risiko_text = "Sangat Tinggi/Bahaya"

        rekomendasi = get_rekomendasi(bmi)

        # ================= OUTPUT =================
        st.subheader("📊 Hasil Analisis Kesehatan")

        st.markdown(f"""
**Nama Lengkap**    : {nama}  
**Umur**            : {umur} Tahun  
**Jenis Kelamin**   : {gender}  
**Tinggi Badan**    : {tinggi} cm  
**Berat Badan**     : {berat} kg  
**Aktivitas Fisik** : {aktivitas}  
**Durasi Tidur**    : {tidur} Jam/Hari  
**Riwayat Diabetes Keluarga** : {riwayat}  
**Konsumsi Fast Food** : {fast_food}  

---

### 🧮 BMI : {bmi:.1f} ({kategori})

### ⚠️ Prediksi Risiko Kesehatan : {risiko_text}
""")

        # ================= REKOMENDASI (FIXED) =================
        st.markdown("### 💡 Rekomendasi")

        for r in rekomendasi:
            st.success("✓ " + r)