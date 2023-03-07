import pandas as pd
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

#Rolling gjør at 10 år blir printet ut om gangen og ikke vært år for seg selv. 
data3 = data2.rolling(10, win_type='boxcar', axis=1, closed='left', center=False).sum().iloc[:, ::10]
datafuture3 = datafuture2.rolling(10, win_type='boxcar', axis=1, closed='left', center=False).sum().iloc[:, ::10]

#Lager en figur og et subplot
fig, ax = plt.subplots(figsize=(12, 6))

#plotter det første område under grafen (Første fil)
data3.plot.area(ax=ax)
ax.set_title("Befolknings vekst")

#Ploter det andre område under grafen (Andre fil)
datafuture3.plot.area(ax=ax)

#Setter navn på aksene
ax.set_xlabel("År")
ax.set_ylabel("Befolkning")

#Viser grafen
plt.show()