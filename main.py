import pandas as pd
import matplotlib.pyplot as plt

fileName = "10211_20230306-214644.csv"
fileNamefuture = "13599_20230307-134301.csv"

data = pd.read_csv("10211_20230306-214644.csv", encoding="ISO-8859-1",sep=";", header = 1)
datafuture = pd.read_csv("13599_20230307-134301.csv", encoding="ISO-8859-1", sep=";", header = 1)

data["alder"] = data["alder"].str.split("å", expand = True).loc[:,0].astype(int)
data2 = data.pivot_table(index="år", values="Personer", columns="alder")

datafuture["alder"] = datafuture["alder"].str.split("å", expand = True).loc[:,0].astype(int)
datafuture2 = datafuture.pivot_table(index="år", values="Folkemengde", columns="alder")

data3 = data2.rolling(10, win_type='boxcar', axis=1, closed='left', center=False).sum().iloc[:, ::10]
data3.plot.area()
plt.show()

datafuture3 = datafuture2.rolling(10, win_type='boxcar', axis=1, closed='left', center=False).sum().iloc[:, ::10]
datafuture3.plot.area()
plt.show()