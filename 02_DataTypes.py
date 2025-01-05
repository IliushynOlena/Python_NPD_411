''' 

print("2")
print('2')
print(2)
# data types :
# numbers : int (1, 25, 239, 1000) , float (3.14 , 1.25, 9.36)
# str - symbols 
# logic types -> boolean True, False
print("int -> ", type(2))
print("float -> ", type(3.14))
print("str -> ", type("2"))
print("str -> ", type("Hello world"))
print("bool -> ", type(True))
print("bool -> ", type(False))


#operators : + , -, /, *,//, %, **
# operator + 
print(2 + 2)
print(2 + 2.) #2. --> 2.0
print(2. + 2)
print(2. + 2.)
# operator - 
print(2 - 2)
print(2. - 2)
print(2 - 2.)
print(2. - 2.)
# operator *
print(2 * 2)
print(2. * 2)
print(2 * 2.)
print(2. * 2.)
# operator / 
print(2 / 2)
print(2. / 2)
print(2 / 2.)
print(2. / 2.)
# operator ** 
print(2 ** 3) 
print(2 ** 3.) 
print(2. ** 3) 
print(2. ** 3.) 
# operator // - ділення націло (відкидаємо значення після коми)
print(6//3)
print(6//3.)
print(6.//3)
print(6.//3.)
print(8//3.0)
# operator % - ділення по модулю (відкидаємо цілу частинку числа, 
# лишаємо кількість одиничок, які не розділились націло)
# 12/4 = 3.0  12%4 = 0 --> 1.12/4= 3.0 2.4*3= 12 3.12-12 = 0
# 15%4 = 3        1.15/4= 3.75  2.3 * 4 = 12 3. 15-12 = 3
# 14%2 = 0     1. 14/2 = 7.0  2. 7*2 = 14  3.14-14 = 0
# 15%2 = 1     1. 15/2 = 7.5  2. 7*2 = 14  3. 15- 14 = 1

print(12%4)
print(15%4)
print(14%2)
print(15%2)
#error
#print(15/0)
#print(15//0)
#print(15%0)

#uno operators (-, +) -5    +5
#binary operators : +, -, *, /, **, //, %
print(2 + 3 * 5 )# <--------- 
print(-5 + 2)# -3
print(2 * 3 * 8)# ----------------->
print( (2 + 3) * 5 )

print(2 ** 2 ** 3 )# <--------- 2 ** 3 = 8  ... 2 ** 8 = 256

print(7 + 2.6) # 7.6
#print(5 + "hello")# error
print(5 + True) #True = 1
print(5 + False) # False = 0
print(1_000_000_000)
print(10_000 * 7.6/100)

'''
#print("Result  = ", result)

112 = "hello"
'''
name = "Bob"
a = 10
a1 = 11
a2 = 12
#3a = 13 # error
b = 5 
c = 7.3
age = 12
Age = 45
ageofman = 33
age_of_man = 32
AgeOfMan = 54
print(age)
print(age)

number = 10
print(1)
print(number)
print("number = ", number)

some_number = 0
print(some_number)

first_number = 10
second_number = 22
print(10 + 22)
print(first_number + second_number)
print("Summa two numbers  = ", first_number + second_number)
result = first_number + second_number
print("Result  = ", result)
print("First number   = ", first_number)
print("Second number  = ", second_number)
#first_number = first_number  + 10
first_number += 10
first_number -= 10
first_number *= 10
first_number /= 10
print("First number   = ", first_number)

user_name = "Ivan"
print(user_name)

line_1 = "Hyper"
line_2 = "Text"
line_3 = "Markup"
line_4 = "Language"
all_line= line_1 + " " + line_2 + " " + line_3 + " " + line_4
print(all_line*3)
print("=" * 30)
print("\033[31m\033[43m\033[2m",line_1, "\033[0m")
print("\033[32m\033[42m\033[3m",line_2, "\033[0m")
print("\033[33m\033[41m\033[4m",line_3, "\033[0m")
print("\033[34m\033[46m\033[1m",line_4, "\033[0m")
print(all_line)

# first_number = input("Enter first number : ") #str  "10"
# second_number = input("Enter second number : ")# str  "145"

first_number = int(input("Enter first number : ")) 
second_number = float(input("Enter second number : ")) 
result = first_number + second_number
print("Result  = ", result)
'''

number = 1234
a = number//1000  #1234/1000
print(a)
b = number//100%10#1234//100 = 12%10 =2 .... 12/10 = 1.2  1*10 = 10 12 - 10 = 2
print(b)
c = number//10%10#1234//10 = 123%10 = 3... 123/10 = 12.3 12*10 = 120 123-120 = 3 
print(c)
d = number%10 #1234%10 = 1234/10= 123.4  123*10 = 1230 1234 - 1230 = 4
print(d)

