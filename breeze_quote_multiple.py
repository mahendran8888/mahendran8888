from breeze_connect import BreezeConnect
import pandas as pd
import datetime
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

Login details here
# stockcode = ['LUPIN', 'ASTPOL', 'INDMAR', 'CADHEA', 'LAULAB', 'AUSMA', 'IPCLAB', 'MAHFIN', 'PIIND', 'DIXTEC', 'TORPHA', 'CIPLA', 'NESIND', 'VOLTAS', 'DEENIT', 'MARLIM', 'UNIBR', 'JINSP', 'SYNINT', 'MINLIM', 'KPITEC', 'FIRSOU', 'METHEA', 'ICIPRU', 'HONAUT', 'LTINFO', 'NAVFLU', 'AURPHA', 'HINDAL', 'HAVIND', 'SUNPHA', 'INFTEC', 'MPHLIM', 'GNFC', 'APOHOS', 'JSWSTE', 'GLEPHA', 'BHAELE', 'DRLAL', 'PERSYS', 'LTTEC', 'DIVLAB', 'DRREDD', 'RAMCEM', 'BIOCON', 'PAGIND', 'SUNTV', 'UNISPI', 'SIEMEN', 'SBICAR', 'ODICEM', 'BOSLIM', 'BERPAI', 'TATCHE', 'RELNIP', 'INDHO', 'TVSMOT', 'ADAENT', 'APOTYR', 'SAIL', 'RAIIND', 'DABIND', 'ZEEENT', 'ALKLAB', 'PIDIND', 'NATMIN', 'NIITEC', 'WHIIND', 'ITC', 'MAHMAH', 'CHOINV', 'EICMOT', 'BAJFI', 'NATALU', 'COLPAL', 'INTAVI', 'POLI', 'WIPRO', 'HINPET', 'INDOIL', 'AARIND', 'BRIIND', 'CORINT', 'HINLEV', 'ASIPAI', 'ABB', 'RBLBAN', 'ESCORT', 'TRENT', 'HERHON', 'ADAPOR', 'BAFINS', 'UNIP', 'MARUTI', 'BAAUTO', 'LTFINA', 'INTDES', 'HDFSTA', 'VEDLIM', 'TORPOW', 'TCS', 'INDGAS', 'SBILIF', 'ATUL', 'ULTCEM', 'AMBCE', 'SRF', 'ONGC', 'TITIND', 'INDBA', 'BHAPET', 'HDFBAN', 'MRFTYR', 'GSPL', 'JKCEME', 'SHRTRA', 'IDFBAN', 'MANAFI', 'LARTOU', 'AMARAJ', 'MOTSUM', 'CROGR', 'ABBIND', 'MAHGAS', 'HDFC', 'HCLTEC', 'BHAAIR', 'MUTFIN', 'TATMOT', 'ORAFIN', 'INDRAI', 'RURELE', 'BALCHI', 'POWFIN', 'IDFC', 'CHAFER', 'ICIBAN', 'TECMAH', 'JUBFOO', 'EXIIND', 'GAIL', 'CUMIND', 'ADICAP', 'MAXFIN', 'BHEL', 'ASHLEY', 'HINCOP', 'PVRLIM', 'GRASIM', 'KOTMAH', 'ADIFAS', 'GMRINF', 'OBEREA', 'HDFAMC', 'HINAER', 'ACC', 'GODCON', 'AXIBAN', 'DELCOR', 'MCX', 'SHRCEM', 'FEDBAN', 'INDHOT', 'POWGRI', 'STABAN', 'PIRENT', 'CITUNI', 'BHAINF', 'DLFLIM', 'INDCEM', 'PUNBAN', 'RELIND', 'INDEN', 'TATPOW', 'BANBAR', 'BANBAN', 'ICILOM', 'INFEDG', 'TATCOM', 'COALIN', 'GRANUL', 'PETLNG', 'LICHF', 'BHAFOR', 'CANHOM', 'BATIND', 'TATGLO', 'GODPRO', 'BALIND', 'CANBAN', 'CONCOR', 'NTPC', 'IDECEL', 'GUJGA']
# stockcode = ['BPL', 'ACC', 'BEML', 'ITC', 'ABB', 'TCS','LUPIN', 'ASTPOL', 'INDMAR', 'CADHEA', 'LAULAB', 'AUSMA', 'IPCLAB', 'MAHFIN', 'PIIND', 'DIXTEC', 'TORPHA', 'CIPLA', 'NESIND', 'VOLTAS', 'DEENIT', 'MARLIM', 'UNIBR', 'JINSP', 'SYNINT', 'MINLIM', 'KPITEC', 'FIRSOU']
# stockcode = ['GMRINF', 'SRF', 'ASHLEY', 'BAFINS', 'CORINT', 'TVSMOT', 'CUMIND', 'ABB', 'AUSMA', 'INDHOT', 'BHAELE', 'GUJGA', 'TATGLO', 'SBICAR', 'GODPRO', 'ASTPOL', 'OBEREA', 'ASIPAI', 'DEENIT', 'BALCHI', 'PIDIND', 'DLFLIM', 'BHAAIR', 'BANBAR', 'SIEMEN', 'NAVFLU', 'PVRLIM', 'CANBAN', 'RAMCEM', 'STABAN', 'MOTSUM', 'EICMOT', 'INDMAR', 'GRASIM', 'BOSLIM', 'TATCOM', 'UNIBR', 'MAXFIN', 'AARIND', 'CHAFER', 'ESCORT', 'HERHON', 'TATCHE', 'TITIND', 'MAHGAS', 'BHAPET', 'CHOINV', 'TORPOW', 'INTAVI', 'FEDBAN', 'PUNBAN', 'IDECEL', 'MARLIM', 'UNISPI', 'INTDES', 'JUBFOO', 'ATUL', 'PIIND', 'LICHF', 'MARUTI', 'CONCOR', 'HINAER', 'BERPAI', 'GAIL', 'MAHFIN', 'MAHMAH', 'ALKLAB', 'ULTCEM', 'ADAENT', 'HINPET', 'INDBA', 'GSPL', 'BHAINF', 'TATPOW', 'TORPHA', 'CANHOM', 'HONAUT', 'JSWSTE', 'SYNINT', 'INDRAI', 'BAAUTO', 'MCX', 'METHEA', 'IDFBAN', 'AXIBAN', 'MUTFIN', 'KOTMAH', 'LTFINA', 'GRANUL', 'ACC', 'HDFSTA', 'BHAFOR', 'NATMIN', 'DIVLAB', 'CITUNI', 'HAVIND', 'KPITEC', 'AMBCE', 'GLEPHA', 'TRENT', 'BANBAN', 'EXIIND', 'SAIL', 'INDGAS', 'INDOIL', 'APOTYR', 'ODICEM', 'INDCEM', 'APOHOS', 'PAGIND', 'ADAPOR', 'IDFC', 'COLPAL', 'ADIFAS', 'GNFC', 'DELCOR', 'BALIND', 'ADICAP', 'SHRCEM', 'HDFBAN', 'RAIIND', 'DRREDD', 'INDEN', 'POLI', 'WHIIND', 'CADHEA', 'PETLNG', 'TATMOT', 'MRFTYR', 'AMARAJ', 'CROGR', 'POWGRI', 'SUNTV', 'BRIIND', 'AURPHA', 'ICIBAN', 'BHEL', 'SHRTRA', 'LAULAB', 'INDHO', 'IPCLAB', 'BATIND', 'ABBIND', 'CIPLA', 'WIPRO', 'RURELE', 'ORAFIN', 'ICILOM', 'JKCEME', 'POWFIN', 'HINCOP', 'ITC', 'NESIND', 'LUPIN', 'HDFC', 'DIXTEC', 'FIRSOU', 'RBLBAN', 'LARTOU', 'BAJFI', 'ICIPRU', 'GODCON', 'JINSP', 'VOLTAS', 'NTPC', 'COALIN', 'MPHLIM', 'INFEDG', 'HCLTEC', 'TECMAH', 'SUNPHA', 'HDFAMC', 'NIITEC', 'VEDLIM', 'LTINFO', 'DRLAL', 'RELIND', 'UNIP', 'HINLEV', 'LTTEC', 'SBILIF', 'NATALU', 'MINLIM', 'INFTEC', 'PIRENT', 'TCS', 'DABIND', 'BIOCON', 'HINDAL', 'ONGC', 'MANAFI', 'PERSYS', 'ZEEENT']
stockcode = ['GMRINF', 'ASHLEY', 'INDHOT', 'BANBAR', 'CANBAN', 'MOTSUM', 'FEDBAN', 'PUNBAN', 'IDECEL', 'GAIL', 'MAHFIN', 'HINPET', 'GSPL', 'BHAINF', 'TATPOW', 'IDFBAN', 'LTFINA', 'NATMIN', 'CITUNI', 'BANBAN', 'EXIIND', 'SAIL', 'INDOIL', 'APOTYR', 'INDCEM', 'IDFC', 'DELCOR', 'ADICAP', 'RAIIND', 'INDEN', 'PETLNG', 'POWGRI', 'BHEL', 'INDHO', 'RURELE', 'POWFIN', 'HINCOP', 'FIRSOU', 'RBLBAN', 'NTPC', 'COALIN', 'VEDLIM', 'NATALU', 'ONGC', 'MANAFI', 'ZEEENT']

appended_data = []
for i in stockcode:
    data1 = breeze.get_quotes(stock_code=i,
                            exchange_code="NSE",
                            expiry_date="",
                            product_type="cash",
                            right="others",
                            strike_price="0")
    # print(data1)
    df = pd.DataFrame(data1["Success"])
    df1 = df.loc[df['exchange_code'] == 'NSE']
    # df1 = pd.DataFrame(df["stock_code"])
    appended_data.append(df1)
    time.sleep(1)
appended_data = pd.concat(appended_data)
print(appended_data)
