import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# 🔥 WAJIB (biar full width)
st.set_page_config(layout="wide")


def load_data():
    base_dir = os.path.dirname(os.getcwd())
    print(base_dir)
    path = os.path.join(base_dir, "nutrigen_projek", "backend", "data", "nutrition_clean.csv")

    if os.path.exists(path):
        return pd.read_csv(path)

    return pd.DataFrame()


def show():
    st.header("📊 Dashboard NutriGen.AI")

    df = load_data()

    # ==============================
    # 🎯 HITUNG DATA
    # ==============================
    total_makanan = len(df)

    avg_calories = 0
    avg_protein = 0
    avg_fat = 0
    avg_carb = 0

    if not df.empty:
        avg_calories = round(df["calories"].mean(), 2)
        avg_protein = round(df["proteins"].mean(), 2)
        avg_fat = round(df["fat"].mean(), 2)
        avg_carb = round(df["carbohydrate"].mean(), 2)

    # ==============================
    # 🎨 STYLE
    # ==============================
    st.markdown("""
    <style>
    .card {
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-family: sans-serif;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    .blue { background: linear-gradient(135deg, #36A2EB, #007bff); }
    .red { background: linear-gradient(135deg, #ff4b5c, #c0392b); }
    .green { background: linear-gradient(135deg, #2ecc71, #27ae60); }
    .purple { background: linear-gradient(135deg, #7E57C2, #5E35B1); }
    .orange { background: linear-gradient(135deg, #FFA726, #FB8C00); }

    /* 🔥 BOLD TITLE */
    .title {
        font-size: 18px;
        margin-bottom: 10px;
        font-weight: bold;
    }

    .value {
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==============================
    # 🎯 CARD (5 KOLOM)
    # ==============================
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"""
        <div class="card blue">
            <div class="title">Total Makanan</div>
            <div class="value">{total_makanan}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card orange">
            <div class="title">Avg Calories</div>
            <div class="value">{avg_calories}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card green">
            <div class="title">Avg Protein</div>
            <div class="value">{avg_protein} g</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="card red">
            <div class="title">Avg Fat</div>
            <div class="value">{avg_fat} g</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
        <div class="card purple">
            <div class="title">Avg Carbs</div>
            <div class="value">{avg_carb} g</div>
        </div>
        """, unsafe_allow_html=True)


    # ==============================
    # 🏆 TOP RANKING (GRADIENT HORIZONTAL)
    # ==============================
    st.markdown("")
    st.subheader("🏆 Top Ranking Nutrisi")

    col1, col2 = st.columns(2)

    # =========================
    # 🍗 CALORIES (BLUE GRADIENT)
    # =========================
    with col1:
        top_calories = df.sort_values("calories", ascending=True).tail(10)

        fig1 = px.bar(
            top_calories,
            x="calories",
            y="name",
            orientation="h",
            title="🍗 Top Calories",
            color="calories",
            color_continuous_scale=[
                "#FFE5B4",  # light orange (low)
                "#FFA726",  # medium orange
                "#FF6F00"   # dark orange (high)
            ]
        )
        st.plotly_chart(fig1, use_container_width=True)

        # =========================
        # 💪 PROTEIN (GREEN GRADIENT)
        # =========================
        top_protein = df.sort_values("proteins", ascending=True).tail(10)

        fig2 = px.bar(
            top_protein,
            x="proteins",
            y="name",
            orientation="h",
            title="💪 Top Protein",
            color="proteins",
            color_continuous_scale=[
                "#d4f8dd",
                "#2ecc71",
                "#27ae60"
            ]
        )
        st.plotly_chart(fig2, use_container_width=True)


    # =========================
    # 🥑 FAT (RED GRADIENT)
    # =========================
    with col2:
        top_fat = df.sort_values("fat", ascending=True).tail(10)

        fig3 = px.bar(
            top_fat,
            x="fat",
            y="name",
            orientation="h",
            title="🥑 Top Fat",
            color="fat",
            color_continuous_scale=[
                "#ffd6d6",
                "#ff4b5c",
                "#c0392b"
            ]
        )
        st.plotly_chart(fig3, use_container_width=True)

        # =========================
        # 🍞 CARBS (PURPLE GRADIENT)
        # =========================
        top_carb = df.sort_values("carbohydrate", ascending=True).tail(10)

        fig4 = px.bar(
            top_carb,
            x="carbohydrate",
            y="name",
            orientation="h",
            title="🍞 Top Carbs",
            color="carbohydrate",
            color_continuous_scale=[
                "#e6dcff",
                "#7E57C2",
                "#5E35B1"
            ]
        )
        st.plotly_chart(fig4, use_container_width=True)

    # ==============================
    # 🔥 CHART
    # ==============================
    st.markdown("")

    if df.empty:
        st.info("Belum ada data")
        return

    # 📈 Trend Protein
    st.markdown("### 💪 Trend Protein")
    # urutkan biar lebih natural (trend naik turun)
    df_plot = df.copy()

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_plot["name"],
        y=df_plot["proteins"],
        mode="lines",
        line=dict(color="#27ae60", width=3),
        marker=dict(
            size=6,
            color=df_plot["proteins"],
            colorscale=[
                [0, "#d4f8dd"],
                [1, "#27ae60"]
            ],
            showscale=False
        )
    ))

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Nama Makanan",
        yaxis_title="Protein (g)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)

    # 📊 Kalori per makanan
    st.markdown("### 🔥 Trend Kalori")
    df_plot = df.reset_index(drop=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_plot["name"],
        y=df_plot["calories"],
        mode="lines",
        line=dict(color="#FB8C00", width=3),
        marker=dict(
            size=6,
            color=df_plot["calories"],
            colorscale=[
                [0, "#FFE0B2"],
                [1, "#FB8C00"]
            ],
            showscale=False
        )
    ))

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Nama Makanan",
        yaxis_title="Kalori",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)

    #trend fat
    st.markdown("### 🥑 Trend Fat")

    df_plot = df.reset_index(drop=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_plot["name"],
        y=df_plot["fat"],
        mode="lines",
        line=dict(color="#e53935", width=3),
        marker=dict(
            size=6,
            color=df_plot["fat"],
            colorscale=[
                [0, "#ffcdd2"],
                [1, "#e53935"]
            ],
            showscale=False
        )
    ))

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Nama Makanan",
        yaxis_title="Fat (g)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)

    #trend carbs
    st.markdown("### 🍞 Trend Carbohydrate")

    df_plot = df.reset_index(drop=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_plot["name"],
        y=df_plot["carbohydrate"],
        mode="lines",
        line=dict(color="#8e24aa", width=3),
        marker=dict(
            size=6,
            color=df_plot["carbohydrate"],
            colorscale=[
                [0, "#e1bee7"],
                [1, "#8e24aa"]
            ],
            showscale=False
        )
    ))

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Nama Makanan",
        yaxis_title="Carbohydrate (g)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)


    # ==============================
    # ⚠️ DISTRIBUSI RISIKO (DONUT GRADIENT)
    # ==============================
    st.markdown("### ⚠️ Seberapa Aman Makanan Anda? ")
    st.caption("Diagram ini menunjukkan perbandingan makanan yang tergolong aman dan berisiko berdasarkan kalori.")

    aman = len(df[df["calories"] <= 300])
    risiko = len(df[df["calories"] > 300])

    chart_data = pd.DataFrame({
        "Kategori": ["Aman", "Risiko"],
        "Jumlah": [aman, risiko]
    })

    fig = px.pie(
        chart_data,
        names="Kategori",
        values="Jumlah",
        hole=0.6,
        color="Kategori",
        color_discrete_map={
            "Aman": "#FFB74D",   # orange terang (safe)
            "Risiko": "#E65100"  # 🔥 orange tua gelap (warning kuat)
        }
    )

    fig.update_traces(
        textinfo="percent+label",
  # garis putih biar clean
    )

    fig.update_layout(
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)