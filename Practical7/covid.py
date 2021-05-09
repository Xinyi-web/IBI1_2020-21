import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.getcwd()
os.chdir("C:/Users/Administrator/Desktop/IBI1/Practical7")
os.listdir()
#code for importing the .csv file works
covid_data = pd.read_csv("full_data.csv")
#code for showing all colimns, and every second row between 0 and 10
covid_data.iloc[0:10:2,:]
#code for using a Boolean to show “total_cases” for all rows corresponding to Afghanistan
Afghanistan_cases = covid_data[covid_data['location']=="Afghanistan"]
target_cases = Afghanistan_cases.loc[0:81,"total_cases"]
#code for computing the mean and median of new cases for the entire world
world_cases = covid_data[covid_data['location']=="World"]
world_new_cases =  world_cases.loc[:,"new_cases"]
np.mean(world_new_cases)
np.median(world_new_cases)
#code for creating a boxplot of new cases worldwide
plt.boxplot(world_new_cases)
plt.show()
#code for plotting both new cases and new deaths worldwide（before here the code is right)
effect_cases = covid_data[covid_data['location']!="World"]
world_dates = effect_cases.loc[:,"date"]
world_new_deaths = effect_cases.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_cases, 'bo')
plt.show()
plt.plot(world_dates, world_new_deaths, 'bo')
plt.show()
#code for File question.txt
world_specific_cases = covid_data[covid_data['location']!="World"]
day_data = world_specific_cases[covid_data['date']=="2019/3/14"]
total_case = day_data.loc[:,"total_cases"]
plt.boxplot(total_case)
plt.show()
