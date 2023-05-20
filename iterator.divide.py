##Exercise 6: Display numbers divisible by 5 from a list
#Iterate the given list of numbers and print only those numbers which are divisible by 5

list = [10, 20, 33, 46, 55]
print('Given list is [10, 20, 33, 46, 55]')
print('Divisible by 5:')
for x in list:
# % is also called 'modulo' and means 'the remainder'
    if x % 5 == 0:
        print(x)
