import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
sizes = (29862124,11285561,11205972,4360823,4234924)
# Do not use explode to get a relatively objective figure
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
