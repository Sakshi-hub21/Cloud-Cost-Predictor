#Importing Libraries

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler

#reading data

df = pd.read_csv("G:\Real-World-Project\cloud-cost-pedictor\dataset\cloud_data.csv")
print(df)

#Label encoding - text-> numbers

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

# Spliting Dataset

X_train,X_test,y_train,y_test = train_test_split(X_Scaler,y,test_size=0.2,random_state=42)


# Model Training

model = RandomForestRegressor()
model.fit(X_train,y_train)

# Saving model

joblib.dump(model,"../model/model.pkl")

# Saving encoding
joblib.dump(sd,"../model/scaling.pkl")

# Saving scaler
joblib.dump(le,"../model/encoding.pkl")

print("Model,Scaling and Encoding.....")


