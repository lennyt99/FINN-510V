import pandas as pd
from matplotlib import pyplot as plt
from functools import reduce


timeperiod = 365


HW1DATA = pd.read_csv('C:\\Users\\lenny\\Fin510\\HW1.csv')
HW1DATA.head()
HW1DATA ["Date"] = pd.to_datetime(HW1DATA["Date"])

#Now we merge using a list that we have created above

dfl=[HW1DATA]
df = df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'],
                                            how='outer'), dfl)

#Since we have what we need to graph, lets plot the returns calculated in xle
#Stock column = Price Today (Clse Day 2) / Price Yesterday (Clse D1) - 1

plt.plot(df["Date"],df["TSLA"], label="TSLA")
plt.plot(df["Date"],df["MSFT"], label="MSFT")
plt.plot(df["Date"],df["SBUX"], label="SBUX")
plt.plot(df["Date"],df["SBUXNQ"], label="SOFINQ")
plt.plot(df["Date"],df["MSFTNQ"], label="MSFTNQ")
plt.plot(df["Date"],df["TSLANQ"], label="TSLANQ")


#This is pretty much the design of the plot
plt.tight_layout()
plt.title("YF & BB Data BABA, SOFI, & SPY Stock Returns", size = 20)
plt.legend() 
plt.show()

print (df) 
