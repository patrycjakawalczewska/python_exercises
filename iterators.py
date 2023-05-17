##Exercise 2: Print the sum of the current number and the previous number

#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number and their sum in a range(10):")
previous_num = 0
#print the first 10 numbers:
for a in range(1,10):
    x_sum = previous_num + a
    print('Current number:', a, 'Previous number:', previous_num, 'Sum:', x_sum)
    previous_num = a
