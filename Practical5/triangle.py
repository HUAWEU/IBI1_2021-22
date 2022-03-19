# Calculate the triangle sequence
# the initial value of the total dots number called n
# a for-loop of order of numbers
#        calculate the value of the triangle sequence
#        print the result

# the initial value of the total dots number called n
n = 0
#a for-loop of order of munbers, i is the order of the value.
for i in range(1,11):
#   calculate the value of the triangle sequence
    n = i+n
#   print the result
    print("value",str(i)," ",n)
