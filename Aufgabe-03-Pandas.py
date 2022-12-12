import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 1.3
my_data = pd.read_excel('data/Zeitreihe-Winter-2022092012.xlsx')
print(my_data.describe())
base = ['Bezirk', 'Gemnr', 'Gemeinde']
print(len(my_data.keys()))
base.extend(['x' + str(y) for y in range(2000, 2000 + len(my_data.keys()) - 3)])

# [base.append('x' + str(y)) for y in range(2000, 2000 + len(my_data.keys()) - 3)]
my_data.columns = base
print(my_data.keys())

df = pd.DataFrame(my_data, columns=my_data.columns)
print(df.keys()[3:])
print(df)

# 2
# 2.1
plt.plot(df.keys()[3:], df.loc[3][3:], "r")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
# 2.2
print(df['Bezirk'])
_index = [i for i in range(len(df['Bezirk'])) if df['Bezirk'][i] == "IL"]
print(_index)
_sums = [sum(df[year][i] for i in _index) for year in df.keys()[3:]]
print(_sums)
plt.plot(df.keys()[3:], _sums, "m")
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
# 3
# 3.1
# print([[df[key][i] for key in df.keys()[3:]] for i in range(len(df['Gemeinde'][3:]))])
print(df.keys()[3:])
_min = [min(df[key][3 + i] for key in df.keys()[3:]) for i in range(len(df['Gemeinde'][3:]))]
print(_min)
print(len(_min))
_max = [max(df[key][3 + i] for key in df.keys()[3:]) for i in range(len(df['Gemeinde'][3:]))]
_range = [_max[i] - _min[i] for i in range(len(_min)) if len(_min) == len(_max)]
_avg = [sum(df[key][3 + i] for key in df.keys()[3:]) / len([df[key][3 + i] for key in df.keys()[3:]])
        for i in range(len(df['Gemeinde'][3:]))]
print(df.keys()[3:])
df['min'] = pd.Series(_min, index=df.index[3:])
df['max'] = pd.Series(_max, index=df.index[3:])
df['range'] = pd.Series(_range, index=df.index[3:])
df['avg'] = pd.Series(_avg, index=df.index[3:])

# 3.2
sum_per_year = {key: sum([_value for _value in df[key] if not np.isnan(_value)]) for key in df.keys()[3:4]}
sum_overall = sum(sum_per_year[key] for key in sum_per_year.keys())
print(df.loc[3][:])
sum_per_bezirk = {key: sum(sum(df.loc[i][3:-4]) for i in range(len(df['Bezirk'])) if df.loc[i][0] == key) for key in
                  set(df['Bezirk'][3:])}
print(sum_per_bezirk)
# 3.2.1
df['range_standardized'] = pd.Series([df['range'][3 + i] - df['avg'][3 + i] for i in range(len(df['Bezirk'][3:]))],
                                     index=df.index[3:])
print(df['range_standardized'])

# 4
# 4.1
range_standardized_per_bezirk = {
    df['Bezirk'][3 + i]:
        [
            df['range_standardized'][3 + j]
            for j
            in range(len(df['range_standardized'][3:]))
            if df['Bezirk'][3 + j] == df['Bezirk'][3 + i]
        ]
    for i
    in range(len(df['Bezirk'][3:]))
}
# plt.boxplot([range_standardized_per_bezirk[key] for key in range_standardized_per_bezirk.keys()])
labels = range_standardized_per_bezirk.keys()
# fig, (ax0) = plt.subplot(nrows=1, ncols=1)
bplot = plt.boxplot(
    [range_standardized_per_bezirk[key] for key in range_standardized_per_bezirk.keys()],
    vert=True,
    patch_artist=True,
    labels=labels
)
colors = ['pink', 'lightblue', 'lightgreen', 'red', 'yellow', 'green', 'blue', 'purple', 'grey']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.show()

# 4.2
plt.bar(df.keys()[3:-5], [df[key][3] for key in df.keys()[3:-5]], align='center')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

# 5
new_data = pd.read_excel('data/bev_meld.xlsx')
base = ['Bezirk', 'Gemnr', 'Gemeinde']
base.extend(['b' + str(y) for y in range(1993, 2022)])
new_data.columns = base
df = pd.DataFrame(new_data, columns=my_data.columns)
both = pd.merge(my_data, new_data, how='inner', on='Gemnr')
print(both.keys())
# Achtung, lehre zeilen in my_data

