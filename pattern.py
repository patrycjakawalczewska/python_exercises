##Exercise 8: Print the following pattern
#Given:
#1 
#2 2
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

def print_pattern(x):
    for y in range(1, x+1):
        print('#', end='')
        for z in range(1, y+1):
            print(str(y), end =" ")
#new line after each row to display pattern correctly:
        print()
print_pattern(5)

#without hashtags:

#1st option:

def print_pattern(x):
    for y in range(1, x+1):
        for z in range(1, y+1):
            print(str(y), end =" ")
#new line after each row to display pattern correctly:
        print()
print_pattern(5)

#2nd option:


for num in range(10):
    for i in range(num):
        print(num, end=" ")
#new line after each row to display pattern correctly
     print()
