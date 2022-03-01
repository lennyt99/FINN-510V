import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce


timeperiod = 365


HW1DATA = pd.read_csv('C:\\Users\\lenny\\Fin510\\HW1.csv')
HW1DATA.head()
HW1DATA ["Date"] = pd.to_datetime(HW1DATA["Date"])


dfl=[HW1DATA]
df = df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'],
                                            how='outer'), dfl)

plt.plot(df["Date"],df["TSLA"], label="TSLA")
plt.plot(df["Date"],df["MSFT"], label="MSFT")
plt.plot(df["Date"],df["SBUX"], label="SBUX")
plt.plot(df["Date"],df["SBUXNQ"], label="SOFINQ")
plt.plot(df["Date"],df["MSFTNQ"], label="MSFTNQ")
plt.plot(df["Date"],df["TSLANQ"], label="TSLANQ")



plt.tight_layout()
plt.title("YF & BB Data BABA, SOFI, & SPY Stock Returns", size = 20)
plt.legend() 
plt.show()

print (df) 
