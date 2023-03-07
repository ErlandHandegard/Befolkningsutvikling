import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Filen som starter på 10211 er bak i tid
fileName = "10211_20230306-214644.csv"
#Filen som starter på 13599 er frem i tid
fileNamefuture = "13599_20230307-134301.csv"

#leser filer i pandas som gjør at pandas kan gjøre utprint. Jeg må endre filen slik at plottet blir slik jeg vi ha det. 
data = pd.read_csv("10211_20230306-214644.csv", encoding="ISO-8859-1",sep=";", header = 1)
datafuture = pd.read_csv("13599_20230307-134301.csv", encoding="ISO-8859-1", sep=";", header = 1)

#De fire neste linjene er i par og de gjør det samme
#I linje 15 splitter jeg årstallet med "år" eller "år eller eldre". Metoden er string.split() og den splitter med å
#Derreter bruker jeg astype for å endre det til integer
data["alder"] = data["alder"].str.split("å", expand = True).loc[:,0].astype(int)
data2 = data.pivot_table(index="år", values="Personer", columns="alder")

datafuture["alder"] = datafuture["alder"].str.split("å", expand = True).loc[:,0].astype(int)
#Jeg bruker data.pivot() fra pandas og bestemmer at "år" er index (xverdier). Values (yverdier) er enten folkemengde eller Personer(forskjell i filene)
#Columns har en verdi(folkemengde) som plusses sammen i det tilsvarende året. 
datafuture2 = datafuture.pivot_table(index="år", values="Folkemengde", columns="alder")
#I fremtid filen var 2022 og 2023 lagt til så jeg droppet dem
datafuture2.drop([2022, 2023])
#Legger sammen grafene
dataMerged = pd.concat([data2, datafuture2])

#Cut etablerer intevallene og right false slik at vi fr til og med første (0) og til siste verdi. Slik at vi fr med uendelig på slutten
age_intervals = pd.cut(dataMerged.axes[1], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, np.inf], right=False)
#Her summerer jeg alle aldersgruene slik at andas kan plotte det ut
dataMerged = dataMerged.groupby(by=age_intervals, axis=1).sum()

#plotter omrde under grafen
dataMerged.plot.area()
plt.ylabel('Populasjon')
plt.legend(title='Aldersgruppe')

plt.show()