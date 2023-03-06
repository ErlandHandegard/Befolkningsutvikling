import csv
import matplotlib.pyplot as plt

fileName = "tabell_bak_i_tid.csv"
fileNamefuture = "tabell_frem_i_tid.csv"

with open(fileName, encoding = "utf-8-sig") as file:
    fileContent = csv.reader(file, delimiter=";")
    
    while count > 2022-1846:
        count =+ 1


    desiredRowIndex = 3
    for i in range(desiredRowIndex):
        next(fileContent)

    desiredRow = next(fileContent)
    output = desiredRow[2]
    print(output)
