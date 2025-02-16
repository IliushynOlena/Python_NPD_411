

def modifyName(userName):
    newName1 = userName.upper()
    newName2 = userName.lower()
    return newName1,newName2
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

# name = input("Enter name : ")
# print(modifyName(name))
# print(modifyName(name)[0])
# print(modifyName(name)[1])
# userUpper, userLower = modifyName(name)
# print(userUpper)
# print(userLower)


def checkLogin(userLog):
    if userLog == 'admin':
        return userLog.upper()
    elif userLog == 'user':
        return userLog.lower()
    else:
        return "Wrong login!!!!"
    
print(checkLogin("admin"))
print(checkLogin("user"))
print(checkLogin("manager"))

def average(*numbers):
    print(numbers)
    summa = 0
    count = 0
    for num in numbers:
        summa+= num
        count +=1
    return summa/count

print(average(1,5,8))
print(average(1,5,8,14,78,9))
list_numbers = [1,5,8,14,78,9,23,25,26]
print(average(*list_numbers))
print(type(list_numbers[0]))


# def sayHello():
#     print("Hello world")
#     sayHello()

# def Test():
#     print("Test message")
    
#5! = 1 * 2 * 3 * 4 * 5
#8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8
def Factorial(num):#5
    factorial = 1 # 120
    for n in range(1,num+1):#range = 1 2 3 4 5 
        factorial *= n# 1 * 1 = 1...1*2=2...2*3=6...6*4=24...24*5=120
    return factorial

print(f"Factorial = {Factorial(5)}")

def factorialRecursion(num):#num = 3
    if num == 0 or num == 1:
        return 1 
    #num = 5 ---> 5 * ........4 *..... 3 *.... 2 *..... 1 
    return num * factorialRecursion(num-1)


print(f"Factorial = {factorialRecursion(5)}")
