#creating a list to store the marks
marks=[45,36,86,57,53,92,65,45]
#creating a box plot to display the distribution of the marks
#the import mosuled and the code below are from the IBI1 lecture 2.6.1
import numpy as np
import matplotlib.pyplot as plt
score = np.array(marks)
plt.title('The distribution of the marks')
plt.ylabel('Marks')
plt.boxplot(score,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
               )
plt.show()
#calculate the average mark and show the result
average = np.average(marks)
print(average)
#judge whether the average mark is higher than the pass mark of 60%
if average > 60:
   print("Pass")
else:
   print("Failed")
# Rob has failed this ICA
