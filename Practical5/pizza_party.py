# cutting pizza
#if the total number of pieces of pizza less than 64?
#     yes:keep cutting
#     no: done!
# the number of pieces of pizza is storted in p.
# the given number of straight cuts is storted in n
n = 0
p =1
#if the total number of pieces of pizza less than 64?
while p < 64:
   n = n+1
   p = (n**2 + n + 2) / 2
# keep cutting
   if n == 1:
     print(str(n), "straight cut can make", str(p), "pieces of pizza.")
   else:
     print(str(n), "straight cuts can make", str(p), "pieces of pizza.")

# done!
print(str(n), "straight cuts can make", str(p), "pieces of pizza, there is enough pizza for each member of the class.")
