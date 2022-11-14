import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Einlesen des Datensatzes
df = pd.read_excel('data/bev_meld.xlsx')

# Macht man das nicht, heissen die Spalten z.B. 1993 als Zahl. Das kann in Zukunft zu Problemen führen,
# besser ist sie heissen j1993
base = ['Bezirk','Gemnr','Gemeinde']
base.extend('j' + df.columns[3:].astype(str))
df.columns = base
#print(df.j1993) # das funktionert jetzt nämlich

pd.set_option('display.expand_frame_repr', False) # So werden alle Spalten angezeigt

#print(df.describe())

# Kennenlernen und Überprüfen der Daten
# print("Die ersten Datensätze:")
# print(df.head()) # Zeige die ersten Datensätze an
# print("Die letzten Datensätze:")
# print(df.tail(3)) # Man kann die Anzahl als Parameter setzen

# Auswahl bestimmter Zeilen wie gewohnt
#print(df[3:])

#Zugriff Über den Spaltennamen möglich
# print(df.Bezirk)

# Man kann mehrere Spalten auswählen:
# print(df[['Gemnr', 'j1993']])

# Über index Location kann man gleich mehrere Spalten auswählen
#print(df.iloc[:,3:]) # Alle Spalten ab dem Index 3
#print(df.iloc[:,[3,5,7]]) # Die Spalten 3, 5, 7

# Zählen der Bezirke
# print(df.groupby('Bezirk')['Bezirk'].count())


