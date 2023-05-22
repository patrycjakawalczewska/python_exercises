##Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

list = [7, 5, 3, 6]
list.reverse()

#print only the elements of the list
print(' '.join(map(str, list))) 
