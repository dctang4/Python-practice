#### Print in Python ####

# print('My name is Chun, my age is', 30)
# print('Welcome')

######################################
#### Variables in Python ####

# name = 'Tim'
# age = 18

# print(name + ' is a boy')
# print(name + ' is', age)
# print(name, 'is from turkey')
# print(name)

######################################
#### Strings in Python ####

# name = 'Tim'

# #  \n creates line break
# # print('Hi. \nHow are you')

# # \' adds a ' to the string
# # \ adds a \ to the string
# print('Hi. \How are you')
# print(name.upper())
# print(name.isupper())
# print(name.lower())
# print(name.islower())
# print(name.lower().islower())
# print(len(name))
# print(name.index('i'))
# print(name.replace('m', 'k'))

######################################
#### Numbers in Python

# num = 32
# num2 = str(num)

# print(30)
# print(num)
# print('number is ' + num2)

# print(30 + 70.2) # addition
# print(30 - 17.2) # subtraction
# print(30 / 2) # division
# print(30 % 7) # remainder after division
# print(30 * 2) # multiplication
# print(30 ** 2) # exponents

# print(abs(-16)) # absolute value
# print(max(4,2,3,12)) # the max value
# print(min(2,3,1,5)) # the min value
# print(round(3.5)) # round the number
# print(bin(5)) # the binary string eg: bin(3) is 0b11
# print(pow(4,3)) # take 4 to power of 3

# # import math
# # print(math.sqrt(4))

# from math import *
# print(sqrt(4))

################################################
#### User Input ####

# name = input('Input Your Name: ')
# age = input('Input Your Age: ')
# ageint = int(age)
# print('your name is ' + name + ' and your are ' + age + ' years old')
# print('your name is ' + name + ' and your are', ageint ,'years old')

################################################
#### Simple Word Replacement Program ####

# sentence = input('Enter your sentence: ')
# print('Your sentence is: ' + sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1, word2))

################################################
#### List in Python ####

# # List can mix data types such as str, int, and bool
# countries = ['USA', "China", 'Italy', 'Japan', "Vietnam", "Korea"]
# countries2 = list(("France", "Brazil", 'Taiwan'))
# print(countries) ## ['USA', 'China', 'Italy', 'Japan', 'Vietnam', 'Korea']
# print(countries2) ## ['France', 'Brazil', 'Taiwan']
# print(countries[3]) ## Japan
# print(countries[-1]) ## Korea
# print(countries[3][2]) ## p
# print(countries[1:]) ## ['China', 'Italy', 'Japan', 'Vietnam', 'Korea']
# print(countries[1:4]) ## ['China', 'Italy', 'Japan']
# print(type(countries)) ## <class 'list'>
# print(type(countries[3])) ## <class 'str'>
# print(len(countries)) # len gives the length of a str or list  ## 6

# countries[0] = "UK"
# print(countries) # ['UK', 'China', 'Italy', 'Japan', 'Vietnam', 'Korea']

################################################
#### List Methods ####

# list1 = [4, 3, 5, 1, 2]
# list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
# list3 = list2.copy()

# list1.sort()
# print(list1)
# list1.extend(list2)  #  add list2 to the end of list1
# print(list1)


# list2.append('cherry') # add cherry to the end of list2
# print(list2)
# list2.insert(1, 'grapes') # add grapes at index 1
# print(list2)
# list2.remove('banana') # removes banana
# print(list2)
# print(list2.index('mango'))
# print(list2.count('mango'))
# list2.reverse() # reverse the list
# print(list2)
# list2.clear() # clear everything from the list 
# print(list2)

# print(list3)
# print(list3.pop()) # prints the values of the last element which is being removed from the llst
# print(list3) 
# del list3[0] # deletes an element from the list
# print(list3)
# del list3 # deletes the whole list so it no longer exist
# print(list3)

###################################################
#### Tuples in Python ####

# Tuples are immutable so it cannot be changes
