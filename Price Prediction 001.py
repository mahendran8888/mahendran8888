import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from sklearn.preprocessing import MinMaxScaler
from breeze_connect import BreezeConnect
from datetime import datetime,date,time,timedelta

breeze = BreezeConnect(api_key=
breeze.generate_session(api_secret= session_token="1596317")

apidata = breeze.get_historical_data(interval="1minute",
                                       from_date="2022-9-6T07:00:00.000Z",
                                       to_date="2022-9-6T18:00:00.000Z",
                                       stock_code="TCS",
                                       exchange_code="NSE",
                                       product_type="others")
df = pd.DataFrame(apidata['Success'])

# print(df)

df["datetime"]=pd.to_datetime(df.datetime,format="%Y-%m-%d")
df.index=df['datetime']

plt.figure(figsize=(16,8))
plt.plot(df["close"],label='Close Price history')


data=df.sort_index(ascending=True,axis=0)
new_dataset=pd.DataFrame(index=range(0,len(df)),columns=['datetime','close'])

for i in range(0,len(data)):
    new_dataset["datetime"][i]=data['datetime'][i]
    new_dataset["close"][i]=data["close"][i]

scaler = MinMaxScaler(feature_range=(0, 1))
final_dataset = new_dataset.values

train_data = final_dataset[0:987, :]
valid_data = final_dataset[987:, :]

new_dataset.index = new_dataset.datetime
new_dataset.drop("datetime", axis=1, inplace=True)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(final_dataset)

x_train_data, y_train_data = [], []

for i in range(60, len(train_data)):
    x_train_data.append(scaled_data[i - 60:i, 0])
    y_train_data.append(scaled_data[i, 0])

x_train_data, y_train_data = np.array(x_train_data), np.array(y_train_data)

x_train_data = np.reshape(x_train_data, (x_train_data.shape[0], x_train_data.shape[1], 1))


lstm_model=Sequential()
lstm_model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train_data.shape[1],1)))
lstm_model.add(LSTM(units=50))
lstm_model.add(Dense(1))

inputs_data=new_dataset[len(new_dataset)-len(valid_data)-60:].values
inputs_data=inputs_data.reshape(-1,1)
inputs_data=scaler.transform(inputs_data)

lstm_model.compile(loss='mean_squared_error',optimizer='adam')
lstm_model.fit(x_train_data,y_train_data,epochs=1,batch_size=1,verbose=2)
