##Exercise 3: Print characters from a string that are present at an even index number

#Write a program to accept a string from the user and display characters that are present at an even index number.
#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

#1) option:

print('Orginal String is  pynative')
print('Printing only even index chars')
str = "pynative"

#get even letters:
even = str[::2]
#create an iteration
iteration = iter(even)

#print each of the even letters:
print(next(iteration))
print(next(iteration))
print(next(iteration))
print(next(iteration))

#2) option:

#use any input as a string
word = input('Enter word ')
print("Original strong is", word)
print('Printing only even index chars')

#iterate the string and print every 2nd letter
for i in range(0, (len(word))-1, 2):
    print(word[i])

