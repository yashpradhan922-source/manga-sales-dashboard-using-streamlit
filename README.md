# 📊 Manga Sales Dashboard

An interactive **Manga Sales Analytics Dashboard** built using **Streamlit, Pandas, and Plotly**.
This project helps users explore manga sales data, identify trends, and generate insights through dynamic visualizations and basic machine learning forecasting.

---

# 🚀 Features

✅ Upload your own CSV dataset
✅ Automatic column detection (no strict schema required)
✅ Interactive filters (Search, Publisher, Demographic)
✅ Dark / Light theme toggle 🌙☀️
✅ Key Performance Indicators (KPIs)
✅ Multiple interactive visualizations
✅ Sales forecasting using Machine Learning 🤖
✅ Download filtered dataset

---

# 🧠 Problem Statement

Raw sales data is difficult to interpret and analyze efficiently.
This dashboard converts raw manga sales data into **visual insights**, enabling users to:

* Identify top-performing manga
* Analyze publisher contributions
* Understand demographic trends
* Forecast future sales

---

# 🛠️ Tech Stack

* **Python**
* **Streamlit** – UI & dashboard
* **Pandas** – Data processing
* **Plotly Express** – Interactive charts
* **Scikit-learn** – Linear Regression (ML model)
* **NumPy**

---

# 📂 Project Structure

```
manga-sales-dashboard/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── sample_data.csv
│
├── requirements.txt
├── README.md
```

---

# 📥 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/manga-sales-dashboard-using-streamlit/manga-sales-dashboard.git
cd manga-sales-dashboard
```

### 2️⃣ Create virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app/streamlit_app.py
```

---

# 📊 Dashboard Functionalities

## 🔍 Filters

* Search Manga by name
* Filter by Publisher
* Filter by Demographic
* Select Top N Manga

---

## 📈 Visualizations

* 🔥 Top Selling Manga (Bar Chart)
* 🏢 Publisher-wise Sales (Donut Chart)
* 👥 Demographic-wise Sales (Bar Chart)
* 📈 Sales vs Volume (Scatter Plot with Trendline)

---

## 📌 KPIs

* Total Manga Series
* Total Sales
* Average Sales per Volume
* Total Publishers

---

# 🤖 Machine Learning Feature

The dashboard includes a **Linear Regression model** that:

* Predicts future sales based on volumes
* Displays growth percentage
* Visualizes forecast trends

---

# 📁 Dataset Requirements

The dashboard automatically detects columns. However, your dataset should ideally contain:

* `Series / Title`
* `Sales`
* `Volume`
* `Publisher`
* `Demographic`
* `Collected Volumes` (optional)

---

# 📸 Preview

*Add screenshots here (recommended for GitHub visibility)*

---

# 🔥 Key Highlights

* Dynamic column detection (no fixed schema required)
* Interactive UI with real-time filtering
* Built-in ML forecasting
* Clean and modern UI with theme toggle

---

# 📌 Future Improvements

* Add advanced ML models (XGBoost, Time Series)
* Deploy on cloud (Streamlit Cloud / AWS)
* Add user authentication
* Real-time data integration

---

# 🙌 Author

**Yash Pradhan**
📧 [yashpradhan922@gmail.com](mailto:yashpradhan922@gmail.com)
🔗 GitHub: https://github.com/yashpradhan922-source

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!


## 📸 Screenshots

<img width="1919" height="972" alt="image" src="https://github.com/user-attachments/assets/611fac24-e456-46bc-8813-fadc1aae3de6" />
<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/c7715195-a171-4341-8da2-4b28b1a26d48" />
<img width="1916" height="969" alt="image" src="https://github.com/user-attachments/assets/1f995c2d-c21d-4459-8660-c674c8608c46" />
<img width="1918" height="968" alt="image" src="https://github.com/user-attachments/assets/77bcd94a-4766-46bd-a38a-30eaee42967f" />
<img width="1917" height="965" alt="image" src="https://github.com/user-attachments/assets/1d7b41bc-c5cd-42cc-8605-e7009d782315" />








