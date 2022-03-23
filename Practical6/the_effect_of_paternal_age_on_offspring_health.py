#creating the lists to store the data
parernl_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

#creating a dictionary to store the two lists above
effect = {'30':1.03,'35':1.07,'40':1.11,'45':1.17,'50':1.23,'55':1.32,
          '60':1.42,'65':1.55,'70':1.72,'75':1.94}
#print the risk of congenitial heart disease in the offspring of a father of given from the input list.
print(effect['50'])

#creating a scatter plot to describe the data
#the import modules is from the IBI1 lecture 2.6.1
import numpy as np
import matplotlib.pyplot as plt
#creating a scatter plot and the code is from the lecture 2.6.1
x = np.array(parernl_age)
y = np.array(chd)
plt.ylabel('The risk of congenitial heart disease in the offspring')
plt.title('The effect of paternal age on offspring health')
plt.xlabel('The age of a father')
plt.scatter(x,y,marker='o')
plt.show()
