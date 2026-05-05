import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Manga Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CACHE ----------------
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# ---------------- COLUMN DETECTION ----------------
def find_column(possible_names, columns):
    for name in possible_names:
        for col in columns:
            if name.lower() in col.lower():
                return col
    return None

# ---------------- THEME ----------------
theme = st.sidebar.radio("Theme", ["Dark", "Light"])

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp { background-color: #0f172a; color: white; }
        div[data-testid="metric-container"] {
            background-color: #1e293b;
            padding: 15px;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp { background-color: #ffffff; }
        div[data-testid="metric-container"] {
            background-color: #f5f7fa;
            padding: 15px;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📂 Upload Data")
file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

# ================= MAIN APP =================
if file:
    df = load_data(file)

    # Clean columns
    df.columns = df.columns.str.strip().str.lower()

    # Detect columns
    series_col = find_column(["series", "title"], df.columns)
    sales_col = find_column(["sales"], df.columns)
    volume_col = find_column(["volume"], df.columns)
    publisher_col = find_column(["publisher"], df.columns)
    demo_col = find_column(["demographic"], df.columns)
    collected_vol_col = find_column(["collected"], df.columns)

    st.write("Available Columns:", df.columns.tolist())

    # ---------------- FILTERS ----------------
    st.sidebar.subheader("🎛 Filters")

    search = st.sidebar.text_input("🔍 Search Manga")
    selected_manga = st.multiselect(
    "Select Manga",
    options=df[series_col].unique()
)
    if search and series_col:
        df = df[df[series_col].str.contains(search, case=False, na=False)]

    if publisher_col:
        publisher = st.sidebar.multiselect(
            "Select Publisher",
            df[publisher_col].dropna().unique()
        )
        if publisher:
            df = df[df[publisher_col].isin(publisher)]

    if demo_col:
        demographic = st.sidebar.multiselect(
            "Select Demographic",
            df[demo_col].dropna().unique()
        )
        if demographic:
            df = df[df[demo_col].isin(demographic)]

    top_n = st.sidebar.slider("Select Top N Manga", 5, 20, 10)

    # ---------------- KPIs ----------------
    st.title("📊 Best-Selling Manga Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📚 Total Manga Series",
        df[series_col].nunique() if series_col else "N/A"
    )

    col2.metric(
        "💰 Total Sales (Million)",
        round(df[sales_col].sum(), 2) if sales_col else "N/A"
    )

    col3.metric(
        "📦 Avg Sales / Volume",
        round(df[volume_col].mean(), 2) if volume_col else "N/A"
    )

    col4.metric(
        "🏢 Total Publishers",
        df[publisher_col].nunique() if publisher_col else "N/A"
    )

    st.markdown("---")

    # ---------------- CHARTS ----------------
    col1, col2 = st.columns(2)

    if series_col and sales_col:
        top_manga = df.sort_values(sales_col, ascending=False).head(top_n)

        fig1 = px.bar(
            top_manga,
            x=sales_col,
            y=series_col,
            orientation="h",
            color=sales_col,
            color_continuous_scale="viridis",
            title="🔥 Top Selling Manga"
        )
        col1.plotly_chart(fig1, use_container_width=True)

    if publisher_col and sales_col:
        pub_sales = df.groupby(publisher_col)[sales_col].sum().reset_index()

        fig2 = px.pie(
            pub_sales,
            names=publisher_col,
            values=sales_col,
            hole=0.4,
            title="🏢 Publisher-wise Sales"
        )
        col2.plotly_chart(fig2, use_container_width=True)

    if demo_col and sales_col:
        demo_sales = df.groupby(demo_col)[sales_col].sum().reset_index()

        fig3 = px.bar(
            demo_sales,
            x=demo_col,
            y=sales_col,
            color=demo_col,
            title="👥 Sales by Demographic"
        )
        st.plotly_chart(fig3, use_container_width=True)

    if collected_vol_col and sales_col and demo_col:
        fig4 = px.scatter(
            df,
            x=collected_vol_col,
            y=sales_col,
            size=sales_col,
            color=demo_col,
            trendline="ols",
            title="📈 Sales vs Volumes"
        )
        st.plotly_chart(fig4, use_container_width=True)

    # ---------------- ML FORECASTING ----------------
    st.markdown("---")
    st.subheader("🤖 Sales Forecasting (ML Model)")

    if volume_col and sales_col:

        df_ml = df[[volume_col, sales_col]].dropna()

        if len(df_ml) > 2:

            X = df_ml[[volume_col]]
            y = df_ml[sales_col]

            model = LinearRegression()
            model.fit(X, y)

            future_volumes = np.arange(
                X.min().values[0],
                X.max().values[0] + 50
            ).reshape(-1, 1)

            predictions = model.predict(future_volumes)

            forecast_df = pd.DataFrame({
                "Volumes": future_volumes.flatten(),
                "Predicted Sales": predictions
            })

            growth_percent = ((predictions.mean() - y.mean()) / y.mean()) * 100

            st.metric("📈 Predicted Growth (%)", f"{growth_percent:.2f}%")

            fig_forecast = px.line(
                forecast_df,
                x="Volumes",
                y="Predicted Sales",
                title="📊 Sales Forecast based on Volumes"
            )

            st.plotly_chart(fig_forecast, use_container_width=True)

            # Bonus: model info
            st.write("📊 Model Coefficient:", model.coef_[0])
            st.write("📊 Model Intercept:", model.intercept_)

        else:
            st.warning("⚠️ Not enough data for ML model")

    else:
        st.warning("⚠️ Volume or Sales column not found")

    # ---------------- INSIGHTS ----------------
    st.subheader("📌 Insights")

    if not df.empty and sales_col in df.columns:
        if df[sales_col].notna().any():
            top_series = df.loc[df[sales_col].idxmax(), series_col]
        else:
            top_series = "No valid sales data"
    else:
        top_series = "Data not available"
    if publisher_col:
        top_pub = df[publisher_col].value_counts().idxmax()
        st.write(f"🏢 Most Active Publisher: **{top_pub}**")

    # ---------------- TABLE ----------------
    st.subheader("📋 Data Preview")
    st.dataframe(df, use_container_width=True)

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        "⬇ Download Filtered Data",
        df.to_csv(index=False),
        "manga_dashboard_data.csv",
        "text/csv"
    )

else:
    st.info("⬅ Upload a CSV file to start the dashboard")
