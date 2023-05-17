## Exercise 1: Calculate the multiplication and sum of two numbers

#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

#Given 1:

#number1 = 20
#number2 = 30

def multiplication_or_sum(x,y):
    result = x*y
    if result <= 1000:
        return result
    else:
        return x+y
      
result = multiplication_or_sum(20,30)
print(result)

#Given 2:

#number1 = 40
#number2 = 30

def multiplication_or_sum(x,y):
    result = x*y
    if result <= 1000:
        return result
    else:
        return x+y
      
result = multiplication_or_sum(30,40)
print(result)
