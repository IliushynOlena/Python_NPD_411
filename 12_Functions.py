
# # print("Hello")
# # print("Hello",4545)
# # print("Hello",4545,True)
# # print("Hello",4545,True,"red")

# # input()
# # max()
# # min()
# # sorted()

# # help(print)


# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

def showHello():
    print("Hello")


# showHello()
# showHello()
# showHello()
# showHello()

# a = 100
# print(f"a = {a}")

def sayHello(name):
    b = 15
    print(f"b = {b}")
    print(f"Hello, {name}")
    print(f"a = {a}")

# sayHello("Olena")
# sayHello("Sasha")
# sayHello("Illia")
# sayHello("Andriy")
# print(f"a = {a}")
# # name = input("Enter name : ")
# # sayHello(name)

# #1.1
def summa(a,b):
    print(a+b)

#1.2   
def summa(a,b):
    res = a + b 
    print(res)

#1.3
def summa(a,b):
    res = a + b 
    return res
#1.4
def summa(a,b):
    return a + b     

# # print(summa(3,8))
# # res = summa(1,2)
# # print(f"Res = {res}")
# # res = summa(7,9)
# # print(f"Res = {res}")
# print("-----------------Calculator-----------------------")
# #Calculator
# def summa(a,b):
#     return a + b  

# def sub(a,b):
#     return a - b  

# def multy(a,b):
#     return a * b  

# def div(a,b):
#     if b == 0:
#         return  #return == break
#     return a / b  

def calculator(a,b,op):
    if op == '+':
        return summa(a,b)
    if op == '-':
        return sub(a,b)
    if op == '*':
        return multy(a,b)
    if op == '/':
        return div(a,b)
    
# def getOperation(example):
#     if example.find('+') != -1:
#         return '+'
#     if example.find('-') != -1:
#         return '-'
#     if example.find('*') != -1:
#         return '*'
#     if example.find('/') != -1:
#         return '/'
    
# res = calculator(5,2,'+')
# print(f"Res = {res}")
# res = calculator(5,2,'-')
# print(f"Res = {res}")
# res =calculator(5,2,'*')
# print(f"Res = {res}")
# res = calculator(5,2,'/')
# print(f"Res = {res}")

# example = input("Enter example (2 + 2)")  #"2 2"
# op = getOperation(example)


# a = float( example.split(op)[0])
# b = float(example.split(op)[1])

# res = calculator(a,b,op)
# print(f"Res = {res}")

import random
def fillList( count_elements = 15, min = 1, max = 10):
    return [ random.randint(min,max)  for i in range(count_elements)]


numbers = []
print(numbers)
numbers = fillList( 10, 20,50)
print(numbers)

numbers = fillList()
print(numbers)

numbers = fillList(5)
print(numbers)

numbers = fillList(7,10)
print(numbers)