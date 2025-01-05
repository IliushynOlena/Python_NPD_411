# #ініціалізація  =  присвоєння
# number = 5 #ініціалізація 
# print(number)

# number = 100#  присвоєння
# print(number)


# a,b,c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# a = b = c = 5
# print(a)
# print(b)
# print(c)


# value = 48
# print("1 == 1:", 1 == 1)         #True
# print("1 == 2:", 1 == 2)         #False
# print("1 != 1:", 1 != 1)         #False
# print("1 != 2:", 1 != 2)         #True
# print("1 > 1:", 1 > 1)           #False
# print("1 > 2:", 1 > 2)           #False
# print("2 > 1:", 2 > 1)           #True
# print("1 < 1:", 1 < 1)           #False
# print("1 < 2:", 1 < 2)           #True
# print("2 < 1:", 2 < 1)           #False
# print("1 >= 1:", 1 >= 1)         #True
# print("1 >= 2:", 1 >= 2)         #False
# print("2 >= 1:", 2 >= 1)         #True
# print("1 <= 1:", 1 <= 1)         #True
# print("1 <= 2:", 1 <= 2)         #True
# print("2 <= 1:", 2 <= 1)         #False

# print(bool(0))
# print(bool(0.0))
# print(bool(""))
# print(bool(None))

# print(bool(1))
# print(bool(3.14))
# print(bool(5))
# print(bool(-41))
# print(bool("It step"))
# print("-----------------------------------------------")
# # and 
# competent = False
# responsible = False
# print(competent and responsible)# True and True = True
# # print(competent and responsible)# False and True = False
# # print(competent and responsible)# True and False = False
# # print(competent and responsible)# True and False = False
# # print(competent and responsible)# False and False = False
# print((5 > 2) and 1 == 1)

# # or 
# competent = False
# responsible = True
# print(competent or responsible)#True or True = True
# # print(competent or responsible)#False or True = True
# # print(competent or responsible)#True or False = True
# # print(competent or responsible)#False or False = False

# #not 
# competent = True
# print(not competent)# True ---> False
# responsible = False
# print(not responsible)# Flase ---> True

# print("Age = ", age)
# print("Age = {} {} {} {}".format(age, 5, 40, "Hello"))
# print("Age = {} {} {} {}".format(5, 40 ,"Hello",age ))
# print(f"Age = {age}")


# print("Hello")
# age = int (input("Enter age : "))
# #if age >= 18 and age <= 125: #age > 18 ---> 19..20.21.21   age < 5 --> 4...3
# if 18 <= age <= 125:
#     print("Welcome to my game!!!!")
# else:
#     print("You are too young or too old!")


# day = int (input("Enter number of day [1-7] : "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Truesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Error number day")

# login = input("Enter login : ")
# if login == "admin" :
#     password = input("Enter password : ")
#     if password == "qwerty123":
#         print("Welcome to system")
#     else:
#         print("Password is error")
# elif login == "exit":
#     print("Goodbye!!!!")
# else:
#     print("Error login")

'''
login = input("Enter login : ")
password = input("Enter password : ")
if login == "admin" and password == "qwerty123":  
    print("Welcome to system")
elif login == "exit":
    print("Goodbye!!!!")
else:
    print("Error login or Password is error")
'''

# import math
# import random

# print(math.ceil(2.5))#2.5 --> 3 ceiling
# print(math.floor(2.5))#2.5 --> 2 
# print(math.pow(2,5))#2*2*2*2*2
# print(math.sqrt(64))#64 = 8

# print(random.random())# 0.........1 float
# print(random.random())# 0.........1 float
# print(random.random())# 0.........1 float
# print(random.randint(0,1))# 0,1
# print(random.randint(10,100))# 0,1
# print(random.randint(-5,5))# 0,1

# Уявіть, що ви прийшли в магазин, де продають магічні карамельки по 270 монет за 1 кг. 
# Зараз у магазині проходить акція: при покупці більше, 
# ніж 500 г карамелек, їхня вартість дорівнює 200 монетам за 1 кг..

# price_full = 270
# price_sale = 200

# gramm = int(input("Enter weight of candies [gramm]: "))
# kg = gramm /1000
# print(f"Your weight : {kg} kg of candies . ")
# if kg < 0.5 :
#     total = kg*price_full
# else:
#     total = kg * price_sale

# total = math.ceil(total)
# print(f"Your total price : {total} coin")

#if elif else
day = int (input("Enter number of day [1-7] : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Truesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Error number day")

#match()
day = int (input("Enter number of day [1-7] : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Truesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Error number day")