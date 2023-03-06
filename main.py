import pandas as pd
import matplotlib.pyplot as plt

fileName = "tabell_bak_i_tid.csv"
fileNamefuture = "tabell_frem_i_tid.csv"

data = pd.read_csv(filepath_or_buffer="tabell_bak_i_tid.csv", encoding="utf-8")
print(data)