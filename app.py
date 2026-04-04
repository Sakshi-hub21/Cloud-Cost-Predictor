import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Cloud Cost Predictor",
    layout="centered"
)

# Title
st.title("☁️ Cloud Cost Prediction Dashboard")
st.markdown("### Predict cost & detect anomalies in real-time")

st.divider()

# Input Section
st.subheader("📥 Enter Cloud Usage Details")

col1, col2 = st.columns(2)

with col1:
    cpu = st.slider("CPU Usage (%)", 0, 100, 50)
    memory = st.slider("Memory Usage (%)", 0, 100, 50)
    instance = st.selectbox(
        "Instance Type",
        ["t2.micro", "t2.small", "t2.medium", "t2.large"]
    )

with col2:
    storage = st.number_input("Storage Usage (GB)", 50, 1000, 200)
    network = st.number_input("Network Traffic (MB)", 100, 2000, 500)

st.divider()

# Button
if st.button("🚀 Predict"):

    data = {
        "CPU_Usage": cpu,
        "Memory_Usage": memory,
        "Storage_Usage": storage,
        "Network_Traffic": network,
        "Instance_Type": instance
    }

    try:
        # Call APIs
        cost_res = requests.post("http://127.0.0.1:8000/prediction", json=data)
        anomaly_res = requests.post("http://127.0.0.1:8000/anomaly-prediction", json=data)

        if cost_res.status_code == 200 and anomaly_res.status_code == 200:

            cost = cost_res.json()["Prediction_cost"]
            anomaly = anomaly_res.json()["Anomaly"]

            st.subheader("📊 Results")

            # Display metrics
            col1, col2 = st.columns(2)

            with col1:
                st.metric(label="💰 Predicted Cost ($)", value=cost)

            with col2:
                if anomaly:
                    st.error("⚠️ Anomaly Detected!")
                else:
                    st.success("✅ Normal Usage")

        else:
            st.error("API Error! Please check backend.")

    except Exception as e:
        st.error(f"Error: {str(e)}")