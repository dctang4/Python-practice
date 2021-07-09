#### Building Simple Calculator ####

# num1 = float(input('Enter first number: '))
# num2 = float(input('Enter second number: '))
# op = input('Enter Operator: ')

# if op == '+':
#   print(num1+num2)
# elif op == '-':
#   print(num1-num2)
# elif op == '*':
#   print(num1*num2)
# elif op == '/':
#   print(num1/num2)
# elif op == '**':
#   print(num1**num2)
# else:
#   print('Invalid operator')

##########################################
#### Try Except in Python ####

# try:
#   x = int(input('Input an integer: '))
#   print(x)
# except:
#   print('Something went wrong')
# else:
#   print('nothing went wrong')
# finally:
#   print('try except finished')

############################################
#### Reading Files ####

# # 'r' - read file; 'w' - write/edit file; 'a' - append to end of file; 'r+' - read and write
# coun_file = open('countries.txt', 'r') 
# # coun_file = open('../country.txt', 'r') 

# print(coun_file.readable())
# # print(coun_file.readlines()[3])

# # print(coun_file.readline())
# # print(coun_file.readline())

# for line in coun_file.readlines():
#   print(line)

# coun_file.close()

#############################################
#### Write Files ####

# 'r' - read file; 'w' - write/edit file; 'a' - append to end of file; 'r+' - read and write
# coun_file = open('country.txt', 'w') 

# coun_file.write('This is the new country file')

# coun_file.close()

# coun_file = open('countries.txt', 'a') 

# # coun_file.write('This is a new line')
# coun_file.write('\nThis is a new line')

# coun_file.close()

# coun_file = open('new.py', 'w') 

# # coun_file.write('print("This is a new file")')
# coun_file.write('print(\'This is a new file\')')

# coun_file.close()

##############################################
#### Classes and Objects in Python ####

# class Myclass:
#   x = 5

# p1 = Myclass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person('John', 87)

# # name = input('Enter your name: ')
# # age = int(input('Enter your age: '))
# # p1 = Person(name, age)

# print(p1.name)
# print(p1.age)

# del p1.age
# print(p1.age)

# class Person:
#   pass # pass is used for an empty class so an error doesn't occur

###########################################
#### Inheritance in Python ####

# from new import Student

# class Person(Student):
#   pass

# p1 = Person()
# print(p1.name)

###########################################
#### Python Shell ####

# in terminal type python3
# after that you will be able to test python code in the terminal

###########################################################
#### Build Simple Login and Signup System with Python ####

print('Create your account')
username = input('Input username: ')
password = input('Input password: ')
print('user \'' + username + '\' created successfully') 
print('Login now')
loginUser = input('Input username: ')
loginPass = input('Input password: ')
if username == loginUser and password == loginPass:
  print('User logged  in successfully')
else:
  print('Invalid credentials')