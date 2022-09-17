import pandas as pd
# df = pd.read_csv("C:\\Users\\mahen\\OneDrive\\Documents\\SecurityMaster\\NSEScripMaster.csv", low_memory=False)
df = pd.read_csv("C:\\Users\\mahen\\OneDrive\\Documents\\fno.csv", low_memory=False)
# print(df)
symbol = df['stockcode'].tolist()
print(symbol)
# for i in symbol:
#     print(i)


# C:\Users\mahen\OneDrive\Documents\SecurityMaster
# C:\Users\mahen\OneDrive