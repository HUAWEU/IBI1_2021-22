import numpy as np
import matplotlib.pyplot as plt

# creating the lists to store the data
parernl_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]

# creating a dictionary to store the two lists above
effect = {}
# store the two lists into the dictionary in right order.
for i in range(0, len(parernl_age)):
    effect[str(parernl_age[i])] = chd[i]
print(effect)

# creating a scatter plot to describe the data
# the import modules is from the IBI1 lecture 2.6.1
# creating a scatter plot and the code is from the lecture 2.6.1
x = np.array(parernl_age)
y = np.array(chd)
plt.ylabel('The risk of congenitial heart disease in the offspring')
plt.title('The effect of paternal age on offspring health')
plt.xlabel('The age of a father')
plt.scatter(x, y, marker='o')
plt.show()

# print the risk of congenitial heart disease in the offspring of a father of given from the input list.
risk = input('Please type a paternal age (30, 35, 40, 45, 50, 55, 60, 65, 70, 75):')
print(effect[risk])