import xlwings as xw

wb = xw.Book('C:\\Users\\mahen\\OneDrive\\Desktop\\Test.csv')
# wb.api.RefreshAll()
sht1 = wb.sheets['Sheet1']
xw.Range('A1').value = df = optionchain
xw.Range('A1').options(pd.DataFrame, expand='table').value