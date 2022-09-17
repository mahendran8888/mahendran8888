import pandas as pd
df = pd.read_csv("C:\\Users\\mahen\\OneDrive\\Documents\\Stock below 100.csv", low_memory=False)
stockcode = df['stockcode'].tolist()
print(len(stockcode))
print(stockcode)