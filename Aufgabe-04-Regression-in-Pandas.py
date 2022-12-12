import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1
import statsmodels.api as sm

data = pd.read_excel('data/bev_meld.xlsx')
base = ['Bezirk', 'Gemnr', 'Gemeinde']
base.extend(['x' + str(y) for y in range(1993, 1993 + len(data.keys()) - 3)])
data.columns = base

# 2
# 2.1
columns = data.columns[3:]
data_sum_bev = [sum(data[key]) for key in columns]
print(data_sum_bev)
plt.plot(columns, data_sum_bev)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()

# 2.2
np_years = np.array([1993 + year for year in range(len(data.keys()) - 3)])
np_data_sum_bev = np.array(data_sum_bev)
df_reg = pd.DataFrame(
    {"years": np_years, "values": np_data_sum_bev})
df_reg = df_reg.astype({'years': 'int'})

model = sm.OLS.from_formula('values ~ years', df_reg).fit()

a = model.params[1]
b = model.params[0]


def calc(x, a, b):
    return a * x + b


np_years = np.array([year for year in range(np_years[0], 2030)])
np_regression = np.array([calc(a, year, b) for year in np_years])
plt.plot(np_years, np_regression)
plt.plot(np.array([1993 + i for i in range(len(columns))]), data_sum_bev)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.xlim(1992, 2030)
plt.show()

# 3
il_data = np.array(
    [sum([data[key][i] for i in range(len(data[key])) if data['Bezirk'][i] == 'IL']) for key in data.columns[3:]]
)
year_data = np.array([1993 + i for i in range(len(data.columns) - 3)])

df_reg = pd.DataFrame({"years": year_data, "values": il_data})
df_reg = df_reg.astype({'years': 'int'})

model = sm.OLS.from_formula('values ~ years', df_reg).fit()

a = model.params[1]
b = model.params[0]

year_data_prediction = np.array([year for year in range(year_data[0], 2030)])
il_data_prediction = np.array([calc(a, year, b) for year in year_data_prediction])

plt.plot(year_data, il_data)
plt.plot(year_data_prediction, il_data_prediction)
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.xlim(1992, 2030)
plt.show()

# 4

re_data = np.array(
    [sum([data[key][i] for i in range(len(data[key])) if data['Bezirk'][i] == 'RE']) for key in data.columns[3:]]
)

fg, axs = plt.subplots(1, 2)
axs[0].plot(year_data, il_data)
axs[0].set_title("IL")
axs[0].set_xlim([1992, 2022])
axs[0].set_ylim([25000, 190000])
for tick in axs[0].get_xticklabels() + axs[0].get_yticklabels():
    tick.set_rotation(45)

axs[1].plot(year_data, re_data)
axs[1].set_title("RE")
axs[1].set_xlim([1992, 2022])
axs[1].set_ylim([25000, 190000])
for tick in axs[1].get_xticklabels() + axs[1].get_yticklabels():
    tick.set_rotation(45)
fg.tight_layout()
plt.show()
