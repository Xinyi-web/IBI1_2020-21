import matplotlib.pyplot as plt
labels='USA','India','Brazil','Russia','UK'
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
