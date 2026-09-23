# print("hello world")
# name = "shubham "
# age = 20
# price = 100.5
# print(name)
# print(age)
# print(price)
# name = input("what is your name? ")
# print(len(name))
# fruit1 = input("enter first fruit: ")
# fruit2 = input("enter second fruit: ")
# fruit3 = input("enter third fruit: ")
# print(fruit1, fruit2, fruit3) 
  
# dictonaries

# student = {
#     "name": "shubham",
#     "age": 20,
#     "courses": ["python", "java", "c++"],
#     "subjects" :{
#         "math": 90,
#         "english": 85,
#         "science": 95
#     }
# }
# print(student)
# print(list(student.keys()))           #to print the keys of the dictonary
# print(list(student.values()))         #to print the values of the dictonary 
# print (len(student))                  #to print the length of the dictonary
# print(student.items())                #to print the items of the dictonary in the form of list of tuples


#sets
# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# my_set.add(6)                        #to add an element to the set
# print(my_set)
# my_set.remove(3)                     #to remove an element from the set   
# print(my_set)
# my_set.add(2)                        #to add an element to the set but it will not add because set does not allow duplicate values
# print(my_set)
# my_set.add(7)                        #to add an element to the set
# print(my_set)
 

 #for loop 
 
# for i in range(1, 11): #to print the square of the numbers from 1 to 10
#     print(i * i)

#range function
# for i in range(11):
#     print(i)

#pass statement
# for i in range(5):
#     pass    #it is used when we want to write a loop but we don't want to write anything inside the loop 
# for a in [10]:
#     run = True
#     while run:
#         if a > 0:
#             print(a)
#             a -= 1
#     else:
#         run = False

# input/output file
# with open("file.txt", "w") as file:   #to write to a file     #with open() is used to open a file and it automatically closes the file after the block of code is execu ted
#     file.write("hello world\n")   
# with open("file.txt", "r") as file:   #to read from a file
#     content = file.read()
#     print(content)

# oops 
# class Person:      #to create a class named Person
#     def __init__(self, name, age):   #to initialize the class with name and age
#         self.name = name    #to assign the name to the instance variable self.name
#         self.age = age      #to assign the age to the instance variable self.age

#     def greet(self):     #to create a method named greet
#         print(f"hello my name is {self.name} and I am {self.age} years old")   #to print the greeting message with the name and age of the person
# person1 = Person("shubham", 20)   #to create an instance of the class Person with the name "shubham" and age 20
# person1.greet()    #to call the greet method of the person1 instance    


# to create a class that takes name and represent marks of 3  subjects as arguments in construcrot.
# class student:
#     def __init__(self, name, math, english, science):
#         self.name = name
#         self.math = math
#         self.english = english
#         self.science = science

#     def average(self):
#         avg = (self.math + self.english + self.science) / 3
#         return avg
# student1 = student("shubham", 90, 85, 95)
# print(student1.name)
# print(student1.average())


# Attributes
# class account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"deposited {amount}. new balance is {self.balance}")   #f is used to format the string and it allows us to insert the value of the variables inside the string using curly braces {}

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"withdrawn {amount}. new balance is {self.balance}")
# account1 = account("shubham", 1000)
# account1.deposit(500)
# account1.withdraw(200)


#delete statement
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# person1 = person("shubham", 20)
# print(person1.name)
# del person1.name    #to delete the name attribute of the person1 instance
# print(person1.name)   #this will give an error because the name attribute has been deleted

# private attributes
# class person:
#     def __init__(self, name, age):
#         self.__name = name   #to make the name attribute private by adding double underscore before the attribute name
#         self.__age = age     #to make the age attribute private by adding double underscore before the attribute name

#     def get_name(self):     #to create a getter method to access the private name attribute
#         return self.__name

#     def get_age(self):      #to create a getter method to access the private age attribute
#         return self.__age
# person1 = person("shubham", 20)
# print(person1.get_name())   #to access the private name attribute using the getter method
# print(person1.get_age())    #to access the private age attribute using the getter method

# inheritance
# class animal:
#      def __init__(self, name):
#          self.name = name

#      def speak(self):
#          pass    #to create a method named speak that does nothing
#      class dog(animal):   
#            def speak(self):
#                return "woof"    #to override the speak method of the animal class and return "woof"
#     class cat(animal):
#            def speak(self):
#                return "meow"    #to override the speak method of the animal class and return "meow"
# dog1 = dog("buddy")   #to create an instance of the dog class with the name "buddy"
# cat1 = cat("whiskers")   #to create an instance of the cat class with the name "whiskers"
# print(dog1.name)    #to print the name of the dog1 instance
# print(dog1.speak())   #to call the speak method of the dog1 instance and print the result
# print(cat1.name)    #to print the name of the cat1 instance
# print(cat1.speak())   #to call the speak method of the cat1 instance and print the result


#class

