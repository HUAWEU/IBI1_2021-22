import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# the code for importing the .csv file works
covid_data = pd.read_csv("full_data.csv")

# the code for showing the first and third columns from rows 10-20(included)
print(covid_data.iloc[9:19,0:4:2])

# use a Boolean to show "total_cases" for all rows corresponding to Afghanistan
location = covid_data.iloc[0:,1]
print(covid_data.loc[location == "Afghanistan","total_cases"])

# compute the mean number of new cases and new deaths in China over time
china_new_data = pd.read_csv("china_new_data.CSV")
print(china_new_data.describe())
# the mean number of new cases
print(np.average(china_new_data.iloc[0:,0]))
# the mean number of new deaths
print(np.average(china_new_data.iloc[0:,1]))

# create a boxplot of new cases and new deaths in China worldwide
score = china_new_data.iloc[0:,0:2]
plt.boxplot(score,vert = True,whis=1.5,patch_artist=True,
            meanline=False,showbox=True,
            showcaps=True,showfliers=True,notch=False)
plt.ylabel('The number of cases or deaths')
plt.title('The new cases and new deaths in China worldwide')
plt.show()

# plot both new cases and new deaths in China over time
china_date = pd.read_csv("china_date.CSV")
china_dates = china_date.iloc[0:, 0]
china_new_cases = china_new_data.iloc[0:, 0]
china_new_deaths = china_new_data.iloc[0:, 1]
plt.plot(china_dates, china_new_cases, 'b+', china_dates, china_new_deaths, 'r+')
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-90)
plt.title('The new cases and new deaths in China over time')
plt.ylabel('The number of cases or deaths')
plt.xlabel('Time')
plt.show()

# the code to answer the question stated in file question.txt
date = covid_data.iloc[354:446,0]
new_cases = covid_data.iloc[354:446,2]
total_cases = covid_data.iloc[354:446,4]
plt.plot(date, total_cases, 'r+', date, new_cases, 'b+')
plt.xticks(date.iloc[0:len(date):4], rotation = -90 )
plt.title('The development of new cases and total cases over time in Australia')
plt.ylabel('The number of cases')
plt.xlabel('Time')
plt.show()