##Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. 
#If numbers are different then return False.

#Given:
#numbers_1 = [10, 20, 30, 40, 10]

numbers_1 = [10, 20, 30, 40, 10]
def list(numbers_1):
    if numbers_1[0] == numbers_1[-1]:
        return True
    else:
        return False
print("result is", list(numbers_1))

#numbers_2 = [75, 65, 35, 75, 40]

numbers_2 = [75, 65, 35, 75, 40]
def list(numbers_2):
    if numbers_2[0] == numbers_2[-1]:
        return True
    else:
        return False
print("result is", list(numbers_2))

