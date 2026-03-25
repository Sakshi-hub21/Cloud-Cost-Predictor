import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder,StandardScaler
df = pd.read_csv("G:\Real-World-Project\cloud-cost-pedictor\dataset\cloud_data.csv")

print(df)


le = LabelEncoder()
df["Instance_Type"] = le.fit_transform(df["Instance_Type"])

print(df)

# Feature & Target

X = df.drop(["Cost"],axis=1)
y = df["Cost"]

print(X)
print(y)


#Scaling features

sd = StandardScaler()
X_Scaler = sd.fit_transform(X)
print(X_Scaler)

#Model training

anamoly_model = IsolationForest(n_estimators=100, contamination=0.05,random_state=42)

anamoly_model.fit(X_Scaler)

joblib.dump(anamoly_model,"../model/anomaly.pkl")