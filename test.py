import random
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Pick a number "))
n1 = int(input("How many random numbers "))


rnumber =[random.randint(1,(n)) for x in range(n1)]
new_num = []
print((new_num))

for i in rnumber:
	new_num.append(rnumber)
	print((new_num))
	break

with open ("rnumber.txt", "w") as f:
	for i in new_num:
		f.write("Random Numbers: ")
		f.write('%s, ' % i)


with open ("rnumber.txt", "r") as rf:
	rfdata = rf.read()

import re
reObj=re.compile('\d+')
mo=reObj.findall(rfdata)
n=[]
for i in mo:n.append(int(i))
#print(sum(n))

#calculate the mean 
def mean(number):
	return(sum(number))/len(number)
	
print("The mean of the numbers is: ")
mean_n = [mean(n)]
print((mean_n))
with open ("rnumber.txt", "a") as meanf:
	for i in mean_n:
		meanf.write("Mean Number: ")
		meanf.write('%s, ' % i)

#verify the mean function with numpy 
print("The mean of the number with numpy")
mean_n_np = [np.mean(n)]
print(mean_n_np)

with open ("rnumber.txt", "a") as meannpf:
	for i in mean_n_np:
		meannpf.write("Mean Number using numpy: ")
		meannpf.write('%s, ' % i)


#calcualate the median 


def median(number):
	n_len = len(number)
	number.sort()

	if n_len % 2 == 0:
		median1 = number[n_len//2]
		median2 = number[n_len//2 - 1]
		m = (median1 + median2)/2
	else:
		m = number[n//2]
	return (m)


print("The median of the numbers is: ")
median_n = [median(n)]
print(median_n)

with open ("rnumber.txt", "a") as medianf:
	for i in median_n:
		medianf.write("Median Number: ")
		medianf.write('%s, ' % i)

#verify the median function with numpy 
print("The median of the number with numpy")
median_n_np = [np.median(n)]
print(median_n_np)

with open ("rnumber.txt", "a") as medianpf:
	for i in median_n_np:
		medianpf.write("Median Number using numpy: ")
		medianpf.write('%s, ' % i)




import collections










































## calculate the standard deviation
def st_dev(number):
	mean_a = sum(number)/len(number)
	f = []
	for i in number:
		f.append((i-mean_a)**2)
	g = sum(f)
	h = g/(len(number)-1)
	k = (h)**.5
	return (("The standard deviation is: ")  + str(k))

st_dev_n = [st_dev(n)]
print(st_dev_n)

with open ("rnumber.txt", "a") as sdf:
	for i in st_dev_n:
		sdf.write("standard deviation Number: ")
		sdf.write('%s, ' % i)

# calcualte the max, min, and range 
def range_n(number):
	max_n = max(number)
	print(("The max number is: ") + str(max_n))
	min_n = min(number)
	print("The min number is : " + str(min_n))
	return (max_n - min_n)

range_n = [range_n(n)]
print("The range of numbers is: ")
print(range_n)

with open ("rnumber.txt", "a") as rangef:
	for i in range_n:
		rangef.write("Range Number: ")
		rangef.write('%s, ' % i)