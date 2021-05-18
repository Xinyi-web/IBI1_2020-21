import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.getcwd()
os.chdir("C:/Users/Administrator/Desktop/大一下/IBI1/Practical7")
os.listdir()
#code for importing the .csv file works
covid_data = pd.read_csv("full_data.csv")
#code for showing all colimns, and every second row between 0 and 10
a = covid_data.iloc[0:12:2,:]
print(a)

#code for using a Boolean to show “total_cases” for all rows corresponding to Afghanistan
data1 = []
#choose data in covid_data in Afghanistan
for i in range (0,7996):
	if covid_data.iloc[i,1] == "Afghanistan":
		data1.append(True)
	else:
		data1.append(False)
b=covid_data.loc[data1,"total_cases"]
print(b)

#code for the worldwide new cases
data2 = []
#choose data in covid_data in the world
for i in range (0,7996):
     if covid_data.iloc[i,1] == "World":
             data2.append(True)
     else:
             data2.append(False)
world_new_cases = covid_data.loc[data2,"new_cases"]

#calculate the mean and median 
mean = str(np.mean(world_new_cases))
median = str(np.median(world_new_cases))
print("the mean and median of new cases worldwide are "+mean+" and "+median)

#draw the boxplot
plt.title('Worldwide new cases')
plt.ylabel('word new case number')
plt.xlabel('date')
plt.boxplot(world_new_cases,vert=True,whis=2,patch_artist=True,showmeans=True,meanline=True,showbox=True,showcaps=True)
plt.show()

#code for File question.txt
data3 = []
#choose data in covid_data in Albania
for i in range (0,7996):
     if covid_data.iloc[i,1] == "Albania":
             data3.append(True)
     else:
             data3.append(False)
Albania_new_cases = covid_data.loc[data3,"new_cases"]
mean = str(np.mean(Albania_new_cases))
print("the mean of Albania new case is "+mean)
