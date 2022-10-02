import numpy as np
from matplotlib import pyplot as plt


def clear_nan(values: list):
    return [item for item in values if not np.isnan(item)]


# source: https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data
d = np.genfromtxt('data/london_weather.csv', delimiter=",", skip_header=1)
print(d)
dt = d[:, 0]  # Datum mit folgendem Aufbau: 19790103 (3.Jänner 1979)
# Aufteilen in Tag, Monat, Jahr
day = (dt % 100).astype('i')
month = (dt % 10000 / 100).astype('i')
year = (dt % 100000000 / 10000).astype('i')

# Check ob es funktioniert hat
print("Jahr:", np.unique(year, return_counts=True))
print("Monat", np.unique(month, return_counts=True))
print("Tag:", np.unique(day, return_counts=True))
print("Jahr MIN MAX", np.min(year), np.max(year))

sun = d[:, 2]  # Sonnenstunden
print(sun)

# PLausibilitätscheck
print("Sun MIN MAX", np.min(sun), np.max(sun))
plt.boxplot(sun)
plt.show()

sun1979 = sun[year == 1979]  # Holen der Sonnenstunden im Jahr 1979
sun2020 = sun[
    year == 2020]  # Schreibweise list2 = list0[list1 == value];       "list1 == value" somehow returns the indexes of its element containing that value
plt.close()
plt.boxplot([sun1979, sun2020])  # Gegenüberstellung der Sonnenstunden

plt.xticks([1, 2], ["1979", "2020"])

plt.show()

# Gegenüberstellung als Punkte
plt.close()
plt.plot(sun1979, "r.")
plt.plot(sun2020, "g.")
plt.show()

# 1.1   years 1979, 1993, 2006, 2020 (deltas in years: +14, +13, +14)

temp = d[:, 5]#
# temp = [item for item in d[:, 5] if not np.isnan(item)]
# temp[np.isnan(temp)] = None  # list contained nan-values (nav-values appear when no number  or another type is given )
temp1979 = clear_nan(temp[year == 1979])
temp1993 = clear_nan(temp[year == 1993])
temp2006 = clear_nan(temp[year == 2006])
temp2020 = clear_nan(temp[year == 2020])

plt.close()
plt.boxplot([temp1979, temp1993, temp2006, temp2020])
plt.xticks([1, 2, 3, 4], ["1979", "1993", "2006", "2020"])
plt.show()
