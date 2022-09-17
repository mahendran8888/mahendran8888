import nsepy
from datetime import datetime,date,time,timedelta
import pandas as pd

# Get VIX value using NSEPy Package
def get_vix_value():

    # Assume yesterday as today
    yesterday = date.today();
    while True:
        # Get yesterday date as we are going to run this before market hours
        yesterday = yesterday - timedelta(1)

        # Get VIX value of yesterday
        df = pd.DataFrame(nsepy.get_history(symbol="INDIAVIX", start=yesterday, end=yesterday, index=True));
        # IF no data found on yesterday, go back to previous day because it may be weekend
        if (df.empty == False):
            break

    # Return VIX value based on close
    return df.iloc[1][3]
print(get_vix_value())