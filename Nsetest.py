from nsepython import *
currentExpiry=nse_expirydetails(nse_optionchain_scrapper('BANKNIFTY'),0)[0]
print(currentExpiry)