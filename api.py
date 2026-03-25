from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np
import joblib

model = joblib.load("G:\Real-World-Project\cloud-cost-pedictor\model\model.pkl")
scaler = joblib.load("G:\Real-World-Project\cloud-cost-pedictor\model\scaling.pkl")
encoder = joblib.load("G:\Real-World-Project\cloud-cost-pedictor\model\encoding.pkl")
anomaly = joblib.load("G:/Real-World-Project/cloud-cost-pedictor/model/anomaly.pkl")
app = FastAPI(title="Cloud Cost Prediction API")

class InputData(BaseModel):
    CPU_Usage:float
    Memory_Usage:float
    Storage_Usage:float
    Network_Traffic:float
    Instance_Type:str

@app.get("/")
def home():
    return {"message":"API is running"}

@app.post("/prediction")
def predict(data:InputData):
    instance_encoded = encoder.transform([data.Instance_Type])[0]

    input_array = np.array([[
        data.CPU_Usage,
        data.Memory_Usage,
        data.Storage_Usage,
        data.Network_Traffic,
        instance_encoded
    ]])

    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)[0]

    return {"Prediction_cost":round(float(prediction),2)}

@app.post("/anomaly-prediction")

def anomaly_predict(data:InputData):
    instance_encoded = encoder.transform([data.Instance_Type])[0]

    input_array = np.array([[
        data.CPU_Usage,
        data.Memory_Usage,
        data.Storage_Usage,
        data.Network_Traffic,
        instance_encoded
    ]])

    input_scaled = scaler.transform(input_array)

    prediction = anomaly.predict(input_scaled)[0]

    if prediction == -1:
        return {"Anomaly":True}
    else:
        return {"Anomaly":False}


