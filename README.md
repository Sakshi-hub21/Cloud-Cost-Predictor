# 🚀 Cloud Cost Prediction & Anomaly Detection System

## 📌 Project Overview

This project is an end-to-end Machine Learning system designed to predict cloud infrastructure costs and detect anomalies in usage patterns. It simulates real-world cloud monitoring scenarios by analyzing metrics such as CPU usage, memory consumption, storage, and network traffic.

The system helps in proactive cost optimization and identifying unusual behavior in infrastructure usage.

---

## 🎯 Problem Statement

Cloud environments often face unexpected cost spikes due to inefficient resource utilization. Manual monitoring is not scalable.

This project aims to:

* Predict cloud cost based on usage metrics
* Detect anomalies in resource usage
* Provide real-time predictions via API
* Enable user interaction through a UI

---

## 🧠 Solution Approach

### 🔹 Cost Prediction

* Implemented **Random Forest Regression** to predict cloud cost

### 🔹 Anomaly Detection

* Used **Isolation Forest** to detect abnormal patterns

### 🔹 End-to-End Pipeline

* Data preprocessing
* Feature engineering
* Model training
* API deployment
* UI integration

---

## 🏗️ Project Architecture

```text
User Input (UI)
        ↓
FastAPI Backend
        ↓
Preprocessing (Scaling + Encoding)
        ↓
ML Model (Prediction / Anomaly)
        ↓
Response to UI
```

---

## 🛠️ Tech Stack

* **Programming:** Python
* **Machine Learning:** Scikit-learn (Random Forest, Isolation Forest)
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Model Storage:** Joblib
* **Version Control:** Git, GitHub

---

## 📂 Project Structure

```text
cloud-cost-predictor/
│
├── app/
│   ├── api.py
│   ├── model.py
│   ├── utils.py
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── encoder.pkl
│
├── data/
│   └── cloud_data.csv
│
├── notebooks/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/cloud-cost-predictor.git
cd cloud-cost-predictor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### 🔹 Start FastAPI Backend

```bash
uvicorn app.api:app --reload
```

👉 API will run on:

```
http://127.0.0.1:8000
```

---

### 🔹 Start Streamlit UI

```bash
streamlit run app.py
```

---

## 📡 API Endpoints

### 🔹 Predict Cost

```http
POST /predict
```

**Input:**

```json
{
  "cpu_usage": 50,
  "memory_usage": 60,
  "storage_usage": 100,
  "network_usage": 20
}
```

---

### 🔹 Detect Anomaly

```http
POST /anomaly
```

---

## 📊 Features

* ✔ End-to-end ML pipeline
* ✔ Real-time prediction API
* ✔ Anomaly detection system
* ✔ Interactive UI using Streamlit
* ✔ Production-ready project structure

---

## 🚀 Future Improvements

* Add Docker support
* Deploy on cloud (AWS / Azure)
* Integrate real-time monitoring data
* Improve model accuracy with larger datasets

---

## 📌 Key Learnings

* Machine Learning lifecycle
* Model deployment using FastAPI
* Building real-world ML applications
* Data preprocessing and feature engineering
* Anomaly detection techniques

---

## 👩‍💻 Author

**Sakshi Shinde**
Aspiring AI/ML Engineer

---
