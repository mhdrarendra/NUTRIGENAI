import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from my_pages import dashboard, nutrisi, prediksi, upload, chat

# st.set_page_config(layout="wide")
# st.markdown("""
# <style>

# /* 🔥 HEADER CONTAINER */
# .header {
#     position: sticky;
#     top: 0;
#     z-index: 999;
#     color: white;
#     padding: 10px 20px;
#     border-bottom: 1px solid #ddd;
#     background: linear-gradient(180deg, #00c853, #00c853);
# }

# /* 🔥 FLEX */
# .header-container {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
# }

# /* 🔥 KIRI */
# .header-left {
#     font-size: 20px;
#     font-weight: bold;
# }

# /* 🔥 KANAN */
# .header-right {
#     display: flex;
#     gap: 15px;
#     align-items: center;
# }

# /* 🔥 ICON STYLE */
# .header-icon {
#     cursor: pointer;
#     padding: 6px 10px;
#     border-radius: 8px;
# }

# .header-icon:hover {
#     background-color: #f0f0f0;
# }

# </style>

# <div class="header">
#     <div class="header-container">
#         <div class="header-left">🍃 NutriGen.AI</div>
#         <div class="header-right">
#             <div class="header-icon">🔔</div>
#             <div class="header-icon">👤 Admin</div>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# hide bawaan streamlit
st.markdown("""
<style>

/* ❌ Hapus header default Streamlit */
header[data-testid="stHeader"] {
    display: transparent;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR STYLE
# =========================

# =========================
# SIDEBAR STYLE
# =========================

# =========================
# SIDEBAR STYLE
# =========================

# =========================
# SIDEBAR STYLE
# =========================

st.markdown("""
<style>

/* Background sidebar */
section[data-testid="stSidebar"] {
    background: #00c853 !important;;
}

/* Semua text sidebar putih */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Judul sidebar */
section[data-testid="stSidebar"] h1 {
    font-size: 28px !important;
    font-weight: 800 !important;
}

/* Caption sidebar */
section[data-testid="stSidebar"] div[data-testid="stSidebarUserContent"] p {
    font-size: 14px !important;
    font-weight: 700 !important;
}

/* Tombol menu */
section[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    justify-content: flex-start !important;
    text-align: left !important;
    padding: 12px 20px !important;
    border-radius: 8px !important;
    border: none !important;
    margin-bottom: 6px !important;

    background: #00c853 !important;
    color: white !important;
}

/* Font tombol */
section[data-testid="stSidebar"] div.stButton > button p {
    font-size: 18px !important;
    font-weight: 600 !important;
    text-align: left !important;
    width: 100% !important;
    margin: 0 !important;
}

/* Hover */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: #2e7d32 !important;
}

/* Tombol aktif */
section[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background: #2e7d32 !important;
    color: white !important;
}

/* Hilangkan border & shadow bawaan */
section[data-testid="stSidebar"] div.stButton > button:focus,
section[data-testid="stSidebar"] div.stButton > button:active {
    box-shadow: none !important;
    border: none !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MENU STATE
# =========================

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🥗 NutriGen.AI")
st.sidebar.caption("AI Nutrisi & Kesehatan")


def menu_button(label, page):
    active = st.session_state.menu == page

    if st.sidebar.button(
        label,
        key=page,
        use_container_width=True,
        type="primary" if active else "secondary"
    ):
        st.session_state.menu = page
        st.rerun()


menu_button("📊 Dashboard", "Dashboard")
menu_button("🥗 Analisis Nutrisi", "Analisis Nutrisi")
menu_button("📈 Prediksi Kesehatan", "Prediksi Kesehatan")
menu_button("🤖 Chatbot AI", "Chatbot AI")
menu_button("📷 Deteksi Makanan", "Deteksi Makanan")

menu = st.session_state.menu

# =========================
# ROUTING
# =========================

if menu == "Dashboard":
    dashboard.show()

elif menu == "Analisis Nutrisi":
    nutrisi.show()

elif menu == "Prediksi Kesehatan":
    prediksi.show()

elif menu == "Chatbot AI":
    chat.show()

elif menu == "Deteksi Makanan":
    upload.show()