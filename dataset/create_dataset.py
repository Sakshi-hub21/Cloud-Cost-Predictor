#Importing libraries
import pandas as pd
import numpy as np

#Number of rows
n = 6000

# Generate synthetic data

data = {
    "CPU_Usage (%)": np.random.randint(10,100,n),
    "Memory_Usage (%)":np.random.randint(10,100,n),
    "Storage_Usage (GB)":np.random.randint(50,500,n),
    "Network_Traffic (MB/s)":np.random.randint(100,1000,n),
    "Instance_Type":np.random.choice(["t2.micro","t2.small","t2.medium","t2.large"],n)
}

#Converting dictionary to table
df = pd.DataFrame(data)

print(df)

# Generate cost based on realistic logic

def calculate_cost(row):
#Each instance type has fixed base price
    base = {
        "t2.micro":10,
        "t2.small":20,
        "t2.medium":40,
        "t2.large":80
    }

#Cost formula- Cost = Base + usage_impact
# 0.5, 0.3.0.05 & 0.03 are weights based on impact on output feature will have


    cost = (
        base[row["Instance_Type"]] + 0.7 * row["CPU_Usage (%)"] + 0.5 * row["Memory_Usage (%)"] + 0.1 * row["Storage_Usage (GB)"]
        + 0.05 * row["Network_Traffic (MB/s)"]
    )


# Add Noise (Realism factor)
    cost += np.random.normal(0,2)

    return round(cost,2)

# Applying Functions to all rows
df["Cost"] = df.apply(calculate_cost,axis=1)
print(df['Cost'].min())
# #Save Dataset
# df.to_csv("G:\Real-World-Project\cloud-cost-pedictor\dataset\cloud_data.csv",index=False)
#
# print("Dataset create with shape:",df.shape)