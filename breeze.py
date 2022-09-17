from breeze_connect import BreezeConnect
import pandas as pd
# import xlwings as xw
from datetime import datetime, timedelta
# import breezelogin
Login details here
# stockcode = ['LUPIN', 'ASTPOL', 'INDMAR', 'CADHEA', 'LAULAB', 'AUSMA', 'IPCLAB', 'MAHFIN', 'PIIND', 'DIXTEC', 'TORPHA', 'CIPLA', 'NESIND', 'VOLTAS', 'DEENIT', 'MARLIM', 'UNIBR', 'JINSP', 'SYNINT', 'MINLIM', 'KPITEC', 'FIRSOU', 'METHEA', 'ICIPRU', 'HONAUT', 'LTINFO', 'NAVFLU', 'AURPHA', 'HINDAL', 'HAVIND', 'SUNPHA', 'INFTEC', 'MPHLIM', 'GNFC', 'APOHOS', 'JSWSTE', 'GLEPHA', 'BHAELE', 'DRLAL', 'PERSYS', 'LTTEC', 'DIVLAB', 'DRREDD', 'RAMCEM', 'BIOCON', 'PAGIND', 'SUNTV', 'UNISPI', 'SIEMEN', 'SBICAR', 'ODICEM', 'BOSLIM', 'BERPAI', 'TATCHE', 'RELNIP', 'INDHO', 'TVSMOT', 'ADAENT', 'APOTYR', 'SAIL', 'RAIIND', 'DABIND', 'ZEEENT', 'ALKLAB', 'PIDIND', 'NATMIN', 'NIITEC', 'WHIIND', 'ITC', 'MAHMAH', 'CHOINV', 'EICMOT', 'BAJFI', 'NATALU', 'COLPAL', 'INTAVI', 'POLI', 'WIPRO', 'HINPET', 'INDOIL', 'AARIND', 'BRIIND', 'CORINT', 'HINLEV', 'ASIPAI', 'ABB', 'RBLBAN', 'ESCORT', 'TRENT', 'HERHON', 'ADAPOR', 'BAFINS', 'UNIP', 'MARUTI', 'BAAUTO', 'LTFINA', 'INTDES', 'HDFSTA', 'VEDLIM', 'TORPOW', 'TCS', 'INDGAS', 'SBILIF', 'ATUL', 'ULTCEM', 'AMBCE', 'SRF', 'ONGC', 'TITIND', 'INDBA', 'BHAPET', 'HDFBAN', 'MRFTYR', 'GSPL', 'JKCEME', 'SHRTRA', 'IDFBAN', 'MANAFI', 'LARTOU', 'AMARAJ', 'MOTSUM', 'CROGR', 'ABBIND', 'MAHGAS', 'HDFC', 'HCLTEC', 'BHAAIR', 'MUTFIN', 'TATMOT', 'ORAFIN', 'INDRAI', 'RURELE', 'BALCHI', 'POWFIN', 'IDFC', 'CHAFER', 'ICIBAN', 'TECMAH', 'JUBFOO', 'EXIIND', 'GAIL', 'CUMIND', 'ADICAP', 'MAXFIN', 'BHEL', 'ASHLEY', 'HINCOP', 'PVRLIM', 'GRASIM', 'KOTMAH', 'ADIFAS', 'GMRINF', 'OBEREA', 'HDFAMC', 'HINAER', 'ACC', 'GODCON', 'AXIBAN', 'DELCOR', 'MCX', 'SHRCEM', 'FEDBAN', 'INDHOT', 'POWGRI', 'STABAN', 'PIRENT', 'CITUNI', 'BHAINF', 'DLFLIM', 'INDCEM', 'PUNBAN', 'RELIND', 'INDEN', 'TATPOW', 'BANBAR', 'BANBAN', 'ICILOM', 'INFEDG', 'TATCOM', 'COALIN', 'GRANUL', 'PETLNG', 'LICHF', 'BHAFOR', 'CANHOM', 'BATIND', 'TATGLO', 'GODPRO', 'BALIND', 'CANBAN', 'CONCOR', 'NTPC', 'IDECEL', 'GUJGA']
stockcode = ['BPL','ACC','BEML','ITC','ABB','TCS']
print(len(stockcode))
appended_data = []
for i in stockcode:
    data1 = breeze.get_historical_data(interval="1minute", from_date="2022-08-05T07:00:00.000Z", to_date="2022-08-08T18:00:00.000Z", stock_code=i, exchange_code="NSE", product_type="cash")
    # data1 = breeze.get_historical_data(interval="1minute", from_date="2022-08-04T07:00:00.000Z", to_date="2022-08-04T18:00:00.000Z", stock_code=i, exchange_code="NSE", product_type="cash")
    df = pd.DataFrame(data1["Success"])
    appended_data.append(df)
appended_data = pd.concat(appended_data)
print(appended_data)

# breeze.get_historical_data(interval="1minute",
#                             from_date= "2021-11-15T07:00:00.000Z",
#                             to_date= "2021-11-17T07:00:00.000Z",
#                             stock_code="ICIBAN",
#                             exchange_code="NFO",
#                             product_type="futures",
#                             expiry_date="2021-11-25T07:00:00.000Z",
#                             right="others",
#                             strike_price="0")









# df=df.to_list()
# print(df.loc[df['datetime'] == '2022-08-03 15:49:00']['close'])

# wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\Test.xlsx')
# sht1 = wb.sheets['Sheet1']
#
# xw.Range('A1').value = df = put_data
# xw.Range('A1').options(pd.DataFrame, expand='table').value
